As I endeavor to continue down the road of learning Linux more fully, I figured
the next major step I needed to take was to dual boot my laptop. With doing
this, I no longer will default into Windows *shudders*, and instead default
into a Linux distro of my choice.

## So Mannnnnnyyy Distros, how do I choose?

The biggest decision you can make is which distro to pick. There are so many 
out there! The way I started to decide was out of the two big branches, Debian 
and Redhat, which would I benefit the most from? To me, a Redhat distro would 
give me the most bang for my buck. This now gives me limited obvious choices;
Fedora or CentOS. The best choice for me ended being Fedora. I believe being 
on the bleeding edge of the updates to the Redhat distributions will give me 
an advantage in the long run. I also enjoy how slick the desktop environment 
with Gnome and how well it integrates into the distro. While there are a few 
hiccups with everything being as fresh and new as can be, the trade off was 
worth it.

## How to make Windows play nicely

You always hear horror stories regarding Windows and Linux dual boots and how
Windows just does not like to play nicely. Fortunately I did not have to deal
with this issue. I started first by  shrinking my current volume in Windows by
running "diskmgmt.msc" and keeping the unallocated space as is. The unallocated
space would become my Fedora space Fortunately, Fedora also can use UEFI boot,
so I only had to disable secure boot in the BIOS, as well as the fast boot in
Windows.

## Installing Fedora

The most difficult part of installing Fedora is creating the bootable USB in
the fashion Fedora recommends. This is the only way to enable UEFI boot for
installation. Without doing this step, Fedora can only install with a BIOS
startup, creating some major issues when working with Windows. This was the
major issue I had for quite some time before I realized I was trying to boot in
two separate ways. So before anyone starts installing, please ensure you have
two compatible boot modes. 

Once you have created your bootable USB, installation is really simple. You
press the appropriate function key that allows you to choose a 1-time boot
option for the USB. Next you choose to install Fedora. Fedora will find the
unallocated space you created while you are in Windows. You can go more
complicated and manually partition everything in the install, or simply allow
Fedora to do its thing, and automagically partition as necessary. Overall, it
is quite painless.

## What I've learned

I've been quite nervous to dual boot, which is what has made me put it off for
so long... However, after completing the process, I'm quite glad I've done it.
I've realized I can do just about everything I need to in Fedora. There are
some kinks because I've chosen such a bleeding edge distro, and getting things
set up takes longer than expected, but I've learned a lot about Linux through
it. It is nice to have my Windows safety net as well, in case I really can't do
something in Fedora but I have yet to run into that situation. I would highly
recommend doing this to any one serious about learning Linux. There is no
better way to learn than to immerse yourself into whatever you want to learn. 
