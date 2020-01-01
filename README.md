# blinkt-daemon

This is a python daemon script for pimoroni blinkt!

blinkt-daemon has been written to control blinkt! LEDs from P4wnP1 A.L.O.A.

## Get it

You can download blinkt-daemon with git:

```
cd /root
git clone --depth=1 https://github.com/sirrus/blinkt-daemon.git
```

## Install pimoroni blinkt!

This project was build for [P4wnP1 A.L.O.A.](https://github.com/mame82/P4wnP1_aloa).

You can install the needed blinkt! tools on P4wnP1 A.L.O.A. via ssh with:


```
apt-get update
apt-get upgrade
curl https://get.pimoroni.com/blinkt > /root/blinkt.sh
patch --verbose < /root/blinkt-daemon/blinkt.sh.patch
bash blinkt.sh
```

## Enable blinkt-daemon

```
cp /root/blinkt-daemon/blinkt-daemon.service /etc/systemd/system/
cp /root/blinkt-daemon/blinkt-daemon-logrotate /etc/logrotate.d/
cp /root/blinkt-daemon/blinkt-daemon-rsyslog.conf /etc/rsyslog.d/
systemctl enable blinkt-daemon
systemctl start blinkt-daemon
```

## Control blinkt with blinkt-daemon

Enable SSH LED:

```
/root/blinkt-daemon/blinkt-client.py SSH
```

Enable any LED (LED numbe 0-7, colors r=0-255 g=0-255 b=0-255 - white):

```
/root/blinkt-daemon/blinkt-client.py LED 6 1 1 1
```

## LED definitions

- 0 green - Power
- 1 green - SSH login
- 2 green - WIFI AP
- 2 blue - WIFI Client
- 7 green 5 second blinking and blue status of P4wnP1 webpage - status

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
- blinkt.sh.patch - patch for blinkt installer on Nano PI
- scripts folder - scripts for P4wnP1 A.L.O.A.
