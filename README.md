# blinkt-daemon

This is a python daemon script for pimoroni blinkt!

blinkt-daemon has been written to control blinkt! LEDs from P4wnP1 A.L.O.A.

## Get it

You can download blinkt-daemon with git:

```
cd /root
git clone --depth=1 https://github.com/sirrus/blinkt-daemon.git
```

## Install pimoroni blintk!

You can install the needed blinkt! tools with:

```
wget http://ftp.debian.org/debian/pool/main/r/rpi.gpio/python-rpi.gpio_0.6.5-1+b2_armel.deb
wget http://ftp.debian.org/debian/pool/main/r/rpi.gpio/python3-rpi.gpio_0.6.5-1+b2_armel.deb
wget http://ftp.debian.org/debian/pool/main/r/rpi.gpio/rpi.gpio-common_0.6.5-1+b2_armel.deb
dpkg -i python-rpi.gpio_0.6.5-1+b2_armel.deb
dpkg -i python3-rpi.gpio_0.6.5-1+b2_armel.deb
dpkg -i rpi.gpio-common_0.6.5-1+b2_armel.deb
curl https://get.pimoroni.com/blinkt | bash
```

## Enable it

```
cp /root/blinkt-daemon/blinkt-daemon.service /etc/systemd/system/
cp /root/blinkt-daemon/blinkt-daemon-logrotate /etc/logrotate.d/
cp /root/blinkt-daemon/blinkt-daemon-rsyslog.conf /etc/rsyslog.d/
systemctl enable blinkt-daemon
systemctl start blinkt-daemon
```

## Access it

Enable SSH LED

```
/root/blinkt-daemon/blinkt-client.py SSH
```

Enable any LED (6 colors r=1 g=1 b=1 - white)

```
/root/blinkt-daemon/blinkt-client.py LED 6 1 1 1
```

## LED definitions

- 0 green - Power
- 1 green - SSH login
- 2 green - WIFI AP
- 2 blue - WIFI Client
- 7 green 1 second blinking - status

## P4wnP1 A.L.O.A.

Copy the scripts to P4wnP1 with:

```
cp /root/blinkt-daemon/scripts/* cd /usr/local/P4wnP1/scripts/
```

## Contents

- LICENSE
- README.md - this document
- blinkt-client.oy - client for sending command to the blinkt-daemon
- blinkt-daemon-logrotate.sh - logrotate settings
- blinkt-daemon-rsyslog.cond - rsyslog configuration
- blinkt-daemon.py - blinkt-daemon
- blinkt-daemon.service - systemd service file
- scripts folder - scripts for P4wnP1 A.L.O.A.

