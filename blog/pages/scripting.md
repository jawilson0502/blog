One thing I find incredibly fascinating is taking a look at my logs and seeing 
who has viewed my site and what region of the world they came from. Yet looking 
at a log manually makes this past-time difficult. There is a lot of information, 
but how much of it do I really want? What key parts are missing from what I want 
to know? To help me better understand my logs, I created a small script that 
filters out what I don't need to read, and adds in the information I am most 
curious about.

## Where to start?

The hardest part in any project for me is deciding where to start. Sometimes 
the end goal seems so far away it is almost unattainable. So to tackle this 
project, I decided to start with the smallest piece and work forward. The 
first thing I decided I needed was to filter out any of the log records that 
didn't mean anything to me. I decided that would be the CSS, JS, font, and 
favicon references in the log. Due to the fact they are only loaded if a main 
page of my blog is loaded, they don't hold any real value. I could always just 
look at the main page to get the same logging information.

## Step 2: .... Filter even more!

Alright, now I've narrowed it down to log records that may mean something. 
However, I started noticing there are a lot of the IP addresses visiting 
"robots.txt". I feel it is safe to assume 99% of log references to "robots.txt" 
is a bot, and not an actual visitor. So the next step I took was to filter all 
of them out while creating a running list of known bots to filter out later. 
The next section of code I wrote takes a leap of faith within myself - I assume 
anyone who gets a "404" error attempted to go to a page that was not there, and 
was never meant to be. This assumes that I did not put any broken links in my 
code. It also assumes that the attempt was malicious. With that in mind, I 
filter out any "404"s and save the IP addresses to another file for future reference.

## Step 3: Review the good data!

Now that I have a reasonable filter on my access logs for my website, I can 
review the data I care about. Currently for me, that means seeing who visited 
my site and from where. The last section of my code involves pulling out all 
the IP addresses I've deemed worth, and finding out where they came from. I 
use [IPInfo](http://ipinfo.io) to curl all my data. I then feed it to a new 
file for reviewing later. Now I have all the information I am interested in.

## What next?

Now that I have this script written, I have the ability to watch the logs on 
my website giving me any information I want. I now have an easy list of known 
bots to view, and decide later if I want them to continue visit, or if I want 
to restrict their access further than I already have. I have a list of bots 
that I assume are malicious. Later I may decide if they hit my site more than 
a certain number of times, I want to deny their IP from coming back. I could 
decide next to take all the data from what I deemed to be good log records 
and create a script to tell me how often a particular page is visited. This 
would give me some kind of metric on how effective writing these blogs actually are.

For now I am going to start reviewing the information I have from these new 
filtered log results and decide exactly how I want to process them, and how 
foolproof they are.

To see a copy of my script, please click
[here](https://github.com/jawilson0502/myScripts/blob/master/websiteLogScript.sh)
and stay tuned for a blog post regarding the other script I have in my GitHub!
