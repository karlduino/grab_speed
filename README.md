## Grab speed from nagios server

I'm using a raspberry pi to monitor 3 routers, including
using [this internet speed test code](https://github.com/jonwitts/nagios-speedtest).

In the present repository is a python script to pull out the speed test results
on an hourly basis. It's made more complicated because the primary tool occasionally
spits out not the speed but rather a bunch of trace information, so here
I'm just grepping the primary data file and then adding it to the bottom of another
file provided that it's less then so many characters

To make this run hourly, I put a copy of the script in `/usr/local/bin` and
added a line like the following using `crontab -e`:

```
59 * * * * /usr/local/bin/grab_speed.py
```

### License

Released under the [MIT license](LICENSE.md).
