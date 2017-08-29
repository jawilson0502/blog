After having my raspberry pi webserver up for quite some time, I've been able 
to watch the different things that are thrown at it. It made me start thinking, 
what vulnerabilities do I already have that can be exploited? What have I 
inadvertently misconfigured to make things that much easier to break in, 
and crash my pi?

## Vulnerability Management

The biggest question becomes, how do I identify the vulnerabilities I've 
created, or defaults I've left default without realizing I should/could change 
them. My solution -[Lynis](https://cisofy.com/documentation/lynis/#installation), 
an open source vulnerability auditing tool. It uses typical security standards, 
and creates a nice neatly packaged report.

Lynis is quite easy to install and run. You can either use a package manager 
such as yum or apt-get, or download the tarball and install that way. I would 
highly recommend downloading the tarball to install, as it will always be the 
most up to date method. You can use the method below to download Lynis

```
wget https://cisofy.com/files/lynis-2.1.1.tar.gz
tar zxvf lynis-2.1.1.tar.gz
cd lynis
```

Do note - that is the most up to date version as of this post. After performing 
the above commands, you have to change ownership of a few files to ensure you 
can run this propery as root. By running it as root, Lynis is able to create logs.

```
sudo chown root:root -R include/<br>
sudo chown root:root lynis<br>
sudo ./lynis audit system
```

Once Lynis starts running, you will have to press `Enter` through each section. 
You can run it with `-Q` for "Quick" and have it run automatically, however, I 
personally would rather review each section before continuing, which is why I 
omitted it. Keep in mind, all vulnerability scanners can do is go through basic 
configurations and essentially only catch the lower hanging fruits, as it were. 
There is no way it could catch the next major Zero Day. I decided I wanted to 
pursue this because after reviewing my logs, the malicious attempts on my pi 
would have been low hanging fruit had I not updated my pi frequently, or allowed 
directory transversal, etc. This gave me a great way to clean up the little things.

## So what were the results?

Of course, I will not reveal all my results, but an interesting one that I found 
was that I had left "Expose PHP" set to on, which was default. According to 
[PHP.net](http://php.net/manual/en/ini.core.php#ini.expose-php) the expose_php 
boolean "Exposes to the world that PHP is installed on the server, which includes 
the PHP version within the HTTP header (e.g., X-Powered-By: PHP/5.3.7)." While 
this is not a critical area an attacker can get in at, it does give an attack 
intimate knowledge of my webserver which in turn can use to compromise my pi. 
While I could have done more research, and possibly discovered this flaw on my 
own, using Lynis was much more convenient way to find it. It was default 
configurations such as that I was worried about. Fixing this bad configuration 
was quite simple, I used the following steps:

```
vim /etc/php*/apache*/php.ini
```

Next I found this section in the file, and changed the option from "on" to "off"
![option](/static/blog/SecuringPi2_001.jpg)

That was it! Again, such a simple thing to fix, but I am not sure I would have 
found it without the help of Lynis.

## What's the plan from now on?

I'm going to continue to fix what Lynis already found for me. After that, I will 
most likely do a scan once a month or so, or whenever I start up a new service. 
If I am not constantly changing and updating things, I won't get any new results 
from the scan. So to me, it would be useless to run it too often. Unless of 
course, I want to see all the green okay messages, letting me know my system 
is fine :-) 
