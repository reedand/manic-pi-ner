# Manic-pi-ner

A screensaver homage to Matthew Smith's [Manic Miner](https://en.wikipedia.org/wiki/Manic_Miner) intended for use with the Raspberry Pi Zero W<sup>1</sup> and @pimoroni's [Display-o-tron 3000](https://github.com/pimoroni/displayotron).

![screensaver image](https://raw.githubusercontent.com/reedand/manic-pi-ner/master/manic.jpeg)

<sup>1</sup> May work with other Raspberry Pi models compatible with Pimoroni's dot3k but I have tested only with the Pi Zero W.

## License

See [license](https://github.com/reedand/manic-pi-ner/master/license.md)

## Pre-requisites

You'll need...

- [x] a willingness to overlook a really bad word play in the repository name :unamused:
- [x] a Raspberry Pi Zero W with Pimoroni Displayotron 3000 (dot3k) installed and working per the Pimoroni [documentation](https://learn.pimoroni.com/tutorial/display-o-tron/getting-started-with-display-o-tron)
- [x] git installed
```bash
sudo apt-get install git
```

## Usage

Change directory to the ../dot3k/advanced/ dir, clone the Python file, make it executable then execute it:
```bash
cd ~/Pimoroni/displayotron/examples/dot3k/advanced
git clone https://github.com/reedand/manic-pi-ner/master/manic.py ./
chmod +X manic.py
./manic.py
```
Use the joystick/button or break out of the Python script to exit.
