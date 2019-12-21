# blinkt-daemon

This is a python daemon script for pimoroni blinkt!

## Get it

cd /root
git clone https://github.com/sirrus/blinkt-daemon.git

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
