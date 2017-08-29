Everyone has their big ideas, but the bigger question is how do we make those 
ideas reality? This website started out as a big idea I wasn't sure I could 
achieve. There were so many things I have never done before when creating this 
site. I had never registered a domain name, I had dabbled in HTML, CSS, and 
JavaScript, but I had never attempted a large scale project. Even PHP was a 
foreign concept to me. Yet, I set a plan for myself. I decided I needed to 
have a working website with at least some content before I attend Detroit's 
Converge/Bsides conference. Last Sunday morning I woke up and thought to 
myself "This is the day I get this done!" Today, I finally have a fully functional 
website. This post will be part 1 of many more regarding what I've done with 
my website. Below details a little more on the struggles and challenges I faced 
while creating it.

## My base set up

The base set up was probably the easiest part to this entire project. My 
website is hosted on a Raspberry Pi 2, running Raspbian Wheezy (a Debian 
based distribution). I've also installed Apache2. I purchased my domain name 
from [Namecheap](http://www.namecheap.com). I also set up Dynamic DNS as they 
outline in Namecheap's support pages. All in all, it was pretty cut and dry.

## To start from scratch or template?

This was a no brainer for me. While I can definitely edit and enhance HTML and 
CSS, I wasn't quite sure if I could start a website from complete scratch just 
yet. I also wanted a professional looking website up and running as quickly as 
possible. For me, the solution was to find a BootStrap template. BootStrap is 
an easy to work with framework for JavaScript, HTML and CSS that translates 
very easily between screen sizes. This seemed like a perfect fit for me, so 
whether you are viewing my blog on a full size desktop, or your mobile phone,it 
will adjust seamlessly. I found
[startbootstrap.com](http://www.startbootstrap.com) 
and loved their Clean Blog template, as you can see from the layout of this blog.

## Tweaking the template

No matter how nice a template looks, personalizing your website is always a must. 
If it is supposed to represent who you are, you should show that in any place you
can. One of my biggest starting concerns was finding pictures I resonated with 
and placing them as my banners on each page. Yet, once I found them, I had to 
make sure the text was readable on them! While that sounds like an incredibly 
easy task, it turned out to be a bit more complicated. In the end, I decided 
to add "text-shadow" characteristics to anything within the banner. It 
enabled me to keep the crisp white font that came with the template, and 
outline that white with black without it contrasting to an extreme. Once I 
figured out how I wanted to modify the font, it was a matter of finding the 
right class selectors within the templates CSS file and adding that property.

## The horror of Contact Me forms

By far the most challenging part of ensuring this website was functional was 
setting up the "Contact Me" form. The template came with a neatly packaged 
PHP script that would take all the input from a predesigned form, and it 
was supposed to send it along to whatever email I set up. Actually adjusting 
the PHP was simple - you put you email where they tell you to. Unfortunately 
that was not all the set up that was needed. The biggest hurdle was setting 
up my raspberry pi to handle relaying the mail to an external email. That 
is not a feature that is set up out of the box for a raspberry pi. After 
many hours of googling and pulling out my hair, I found the 2 magical tutorial 
websites that made it possible. The first was
[SBProjects](http://www.sbprojects.com/projects/raspberrypi/exim4.php)
This site gives you an easy to follow, set by step tutorial on what to do. 
The only requirement you have to handle before starting that is to have a 
gmail account ready to go. I chose the Exim4 path, but you could choose the 
other if you so choose.

Once I completed that tutorial, sending mail from the command line was finally 
possible! (With so many practical applications of it, the project ideas just 
started brewing). I thought, "Now I for sure should have this PHP script 
working!" That was not the case. There was still one more step I had to take 
to have a fully functioning Contact Me feature. Thanks to some google fu, I 
found the next website that was instrumental in accomplishing this. 
[PageFabric](http://www.pagefabric.com/blogs/2012/02/19/how-to-fix-php-not-sending-mail-in-debian-6-and-exim4/) 
provides another tutorial on how to set up the command line mailing system, 
but because I already had that set up, I skipped down to the section "PHP 
configuration of SMTP email". One change in my PHP5 config file, and I was 
ready to rock and roll.

## What's next?

The next question becomes "What is the next project for my website?" Well, I 
already did come up with quite a few other tweaks to implement and issues to 
address. The most pressing issue is what happens when I've written so many 
blog posts they start cluttering up my front page? Soon I hope to have the 
"Older Posts" button fully functional and help me handle this issue. The other 
feature I want to implement quickly is the ability to search by tags in the 
blog posts. I would love the ability to search for relevant posts for what I 
need to remember. Another simple tweak I want to implement is having fully 
functional and relevant social media buttons on the bottom of each page. Lastly, 
I want to create some kind of script to help me monitor traffic to my site.

However, for the short term, I plan on submitting a lot of "Contact Me" 
forms to myself and enjoy seeing the results.
