# P-Rabbit Patcher
Patch expiry dates and trial time limits in PinkRabbit and other P-Rabbit family email software.

## Usage
```
prabbit-patcher.py [--trial-filename NAME] <executable.exe>
```

Point prabbit-patcher.py at the installed executable (not the installer) for PinkRabbit or
(hopefully) any other P-Rabbit family software.

PinkRabbit creates a file in `%WINDIR%` called `SRABBIT.001` and expires 31 days after the file's
creation date. Other P-Rabbit family software tested does not have a trial limit, but the
`--trial-filename` option is provided in case some other software does with a different filename.
Defaults to `SRABBIT.001`.

## Tested software
* [PinkRabbit CUTiE](https://web.archive.org/web/20011202024451/http://prabbit.colabo.co.jp:80/index.html) (COLABO)
* PinkRabbit Classic (COLABO)
* [DreamFlyer for PC](https://web.archive.org/web/20010429170125/http://www.isao.net/dreamflyer/) (ISAO)
* [Kumo Mail / くもメール](https://web.archive.org/web/20031008235046/http://www.fujitv.co.jp/jp/kumomail/index.html) (Fuji TV)
* FINAL FANTASY VIII Mail (DigiCube)
  * Patcher not needed, no expiry or trial

## Untested software
If you find a copy of any of these, please archive it and let me know!
* [Trihoo Mail](https://web.archive.org/web/19991008021017/http://www.town.hi-ho.ne.jp/trihoo/core.htm) (Panasonic Hi-HO)
* [Kimuemi Mail / きむえみめーる](https://web.archive.org/web/19990912052744/http://town.hi-ho.ne.jp/trihoo/kimuemi/) (Panasonic Hi-HO)
* [Shino Mail / しのめ～る](https://web.archive.org/web/20030204034146/http://www.oracion.co.jp/shinora/04/04index.html) (Oracion)
* [Paris Angel Tokyo Angel / パリ天使東京天使](https://web.archive.org/web/20001006000809/http://www.dice-net.com/pre/index.htm) (Dice)
* [EDE Mail / 絵DEメール](https://web.archive.org/web/20010607083849/http://www.sphere.ne.jp:80/ede/) (NTTPC InfoSphere)
* [PinkRabbit Parfait / PinkRabbitパフェ](https://web.archive.org/web/20070225115802/prabbit.colabo.co.jp/pub/parfait/) (COLABO)

## Credit
Based on work by Jessica Stokes and Ninji:
https://jessicastokes.net/blog/2021/06/10/unlocking-pinkrabbit/

## Contact
Send me a P-Rabbit TransMediaLetter (or ordinary email) at <m@kfarwell.org>!
