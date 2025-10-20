#!/usr/bin/env python3

import sys
import re
import os
import argparse

def find_expiry_dates(data):
    found_dates = []

    for offset in range(len(data) - 22):
        length = int.from_bytes(data[offset:offset+2], 'little')

        if not (8 <= length <= 10):
            continue

        string_offset = offset + 2
        string_bytes = data[string_offset:string_offset + length*2]

        if len(string_bytes) < length * 2:
            continue

        try:
            string = string_bytes.decode('utf-16-le')
        except:
            continue

        if re.match(r'^\d{4}/\d{1,2}/\d{1,2}$', string):
            found_dates.append({
                'offset': string_offset,
                'date_str': string,
                'date_bytes': string_bytes
            })

    return found_dates

def find_trial_registration(data, pattern):
    trial_limits = []
    pattern_bytes = pattern.encode('utf-16-le')

    pos = 0
    while True:
        pos = data.find(pattern_bytes, pos)
        if pos == -1:
            break

        if pos >= 2:
            length = int.from_bytes(data[pos-2:pos], 'little')
            string_bytes = data[pos:pos + length*2]

            try:
                string = string_bytes.decode('utf-16-le')
                trial_limits.append({
                    'offset': pos,
                    'string': string,
                    'bytes': string_bytes
                })
            except:
                pass

        pos += 1

    return trial_limits

def patch_prabbit(filename, trial_filename):
    # Read file
    with open(filename, 'rb') as f:
        data = bytearray(f.read())

    # Find expiry dates
    # length-prefixed UTF-16LE date strings (length 8-10, format YYYY/M/D)
    expiry_dates = find_expiry_dates(data)

    if expiry_dates:
        expiry = expiry_dates[0]
        print(f"Found expiry at 0x{expiry['offset']:06x}: {expiry['date_str']}")
    else:
        print("No expiry string found")

    # Find trial registration
    # <trial_filename>,<# days>
    trial_limits = find_trial_registration(data, trial_filename)

    if trial_limits:
        trial = trial_limits[0]
        print(f"Found trial at 0x{trial['offset']:06x}: {trial['string']}")
    else:
        print("No trial string found")

    # Exit if nothing to patch
    if not expiry_dates and not trial_limits:
        return False

    # Patch expiry dates to latest date that fits
    for expiry in expiry_dates:
        original_date = expiry['date_str']

        parts = original_date.split('/')
        month_len = len(parts[1])
        day_len = len(parts[2])

        # Match original length
        if month_len == 1 and day_len == 1:
            new_expiry = "9999/9/9"
        elif month_len == 1:
            new_expiry = "9999/9/30"
        elif day_len == 1:
            new_expiry = "9999/12/9"
        else:
            new_expiry = "9999/12/31"

        new_bytes = new_expiry.encode('utf-16-le')
        data[expiry['offset']:expiry['offset']+len(new_bytes)] = new_bytes

        print(f"Patched expiry: {new_expiry}")

    # Patch trial registration to null
    for trial in trial_limits:
        null_bytes = b'\x00' * len(trial['bytes'])
        data[trial['offset']:trial['offset']+len(null_bytes)] = null_bytes
        print("Patched trial: removed")

    # Write patched file
    base, ext = os.path.splitext(filename)
    patched_filename = f"{base}.patched{ext}"

    with open(patched_filename, 'wb') as f:
        f.write(data)

    print(f"Wrote {len(data):,} bytes to {patched_filename}")

    return True

def main():
    parser = argparse.ArgumentParser(description='Patch P-Rabbit family email software')
    parser.add_argument('executable', help='path to the executable to patch')
    parser.add_argument('--trial-filename', default='SRABBIT.001',
                       help='trial registration file pattern (default: SRABBIT.001)')

    args = parser.parse_args()

    if not os.path.exists(args.executable):
        print(f"Error: File '{args.executable}' not found")
        sys.exit(1)

    success = patch_prabbit(args.executable, args.trial_filename)
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
