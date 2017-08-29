Having a presence online comes with all sorts of perils in the world of IT 
security. Everyday somewhere something is scanning various parts of the internet 
to take advantage of any weakness they can find. With that in mind, I wanted to 
make sure my raspberry pi was secure enough to handle whatever was thrown at it. 
By all means, this is not the final form of security, but steps in the right 
direction.

## What services do I really need open?

The first question when it came down to designing a security plan for my 
raspberry pi hosting my website was deciding what were the necessary services 
I needed access from an external perspective? I decided the answer to that was 
SSH and HTTP.

##Sooo SSH? It's already secure right?

The first service I needed up and running was SSH. My raspberry is not hooked 
up to a monitor, keyboard or mouse. It is a small little box sitting next to 
my router. That is it. The only way I interact with it is through an SSH session. 
So what happens when I open up my firewall to allow port 22 into my raspberry? 
Well, because I tend to be a total dork when it comes to logs.. I wrote a script 
to analyze that. (Check it out through my github! Link at the bottom of the page). 
Here are a few of my results.. 

![results](/static/blog/accesslog1.jpg)

A little extreme right? Just my lowly little raspberry hanging out and it 
received almost 6,000 SSH hits!That isn't even the most I've received... 

![accesslog](/static/blog/accesslog2.jpg)

Yeah, I think it is fair to say if you have port 22 open, someone is trying 
to get in. Just because the name is "Secure Shell" doesn't mean this service 
is free from attacks. You have to secure your box before you can assume your 
SSH is actually secure. I decided the best route was to ensure the configuration 
settings in SSH permitted no root logins and to use a non-standard port. My 
results were outstanding! 

![accesslog2](/static/blog/accesslog3.jpg)

One silly caveat - if you are going to switch to a non-standard port, make 
sure you change your iptables rules first to allow yourself to connect through 
that port. Otherwise.. You will have a bad time.

## Now for the biggie: HTTP

Clearly the next big service I need is to enable is HTTP. Without that, you 
wouldn't be reading this blog right now. I decided I wanted to take a tried 
and true method to handling security threats this. I installed 
[fail2ban](http://www.fail2ban.org/wiki/index.php/Main_Page) This handy little 
service uses your already existant logs to determine what people are trying 
access, and block them based on the parameters of your set. The other great 
news is there are many many tutorials on how to implement this. 
[Xmodulo](http://xmodulo.com/configure-fail2ban-apache-http-server.html) has a 
great introduction tutorial I followed. The jails I decided to use were Apache 
driven noscript, nohome, badbots, overflows, fakegooglebot, shellshock and 
postflood. I felt this gave a very broad range of protection against various 
attacks. I also set the find time to be 6 hours and most of the max attempts 
of these attacks to be 2. Now if someone reserves a 404 twice with less than 6 
hours in between, they are automatically blacklisted from my site for 48 hours. 
While this is a very extreme approach, I am counting on the fact I will not 
create any 404 links within my own site. So if you are navigating my site as 
intended, there is not a single issue. However, when something is trying to brute 
force my site, they are caught quickly, with little wiggleroom.

While this is just a step towards securing my Raspberry Pi, I feel getting a 
good handle on these two services will go a long way. 
