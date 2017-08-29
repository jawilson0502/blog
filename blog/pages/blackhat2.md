Something that greatly interests me is the idea of honeypots. Simply put, I 
would love to set one up and see what of traffic comes through. Just as I 
have started creating and analyzing my own log files for my legitimate services, 
I would love to do the same for a honeypot. One of the talks I was fortunate 
enough to attend at Black Hat was the 
[Bring Back the Honeypots](https://www.youtube.com/watch?v=W7U2u-qLAB8)" talk 
by Haroon Meer and Marco Slaviero. In this talk, they overviewed how to use 
[Open Canary](https://github.com/thinkst/opencanary), an open source platform 
that is able to be quickly deployed. It is essentially a honeypot sensor for 
your network written in python.

## What is a Honeypot?

As defined by many, a honeypot is a security mechanism to detect or deflect 
attempts for unauthorized access. Generally they will look like an easy 
attractive target for an attacker to pursue, all while rigged with alerts 
for system administrators, warning them of a possible breach. This could lead 
to rules in the system configuration to lock the offending IP. Another option 
with a honeypot is to use it for security research. It allows a researcher to 
dive into what is really out in the wild trying to get in. It is a great way 
to analyze aspects of an attack.

## What was in the talk?

In this talk they began by giving solid background information on how honeypots 
have been perceived in the past, as well as a reason as to why they are not 
more widely implemented. One of the biggest downfalls for honeypots is that 
they do not give instant gratification. After one is set up, it must be given 
time to be discovered. Until then, it is just another vulnerable box sitting 
on your network. This can lead lead to another problem, many peopel are nervous 
about setting up another node they have to watch and protect, creating more work 
for those monitoring the network. However, the presenters brought up a fantastic 
point - it is almost guaranteed someone is trying to get in, and may already be 
in. A node that is customized to alert you on any suspicious activity, that 
allows you to watch all the exploitation as it is happening gives you a chance 
to now protect against it. It also a completely controlled arena, unlike your 
typical end user node, giving you even more precise control on what happens in this box.

After giving a great background on the theory of honeypots, the speakers 
proceeded to deploy multiple instances of Open Canary, each set up with 
a specific purposes with different alerts for each. Within an hour, they 
had accomplished all of these things.

## What next?

After seeing how simply they set up this configuration, my goal is to set up 
my own honeypot by the end of next winter. I want to be able to analyze the 
traffic and see what typically comes through the wire. While this will require 
finding the appropriate spot to plant the honeypot, I feel this will allow me 
to better understand security needs as a whole.
