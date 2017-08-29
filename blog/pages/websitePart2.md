The next project I started with my website was to make the home page only 
display so many posts, and have it auto-populate. To accomplish this, I decided 
I needed to create first a database then link in that database to my website.

##Choosing a Database

There are many different databases, but generally they fall into 1 of 2 
categories, either SQL or NoSQL. After researching a bit I decided I wanted to 
go with a SQL database. My biggest driving factor in this was the fact a lot of 
employers are looking for SQL experience. There is also quite a bit of 
documentation with SQL databases. After researching a bit further, I chose MySQL 
in particular. It is light enough to not bog down my Raspberry Pi, yet powerful 
enough to do what I want.

So now I have my database, what should I put into it? The first table I created 
I decided to fill with basic blog information; title, subtitle, date and path. 
I also had MySQL require an ID number and have it automatically assigned. I found 
this to be the easiest way to uniquely identify each post, and a quicker way to 
start to build a relational model for the other tables I planned on creating. I 
also created a table full of tag names as well as a table linking each post to 
at least 1 tag name. (More to come from that on a later date). The sites I found 
most helpful to accomplish this were 
[SQL for
Beginners](http://code.tutsplus.com/tutorials/sql-for-beginners--net-8200) 
by Burak Guzel, as well as dofactory's 
[SQL Join](http://www.dofactory.com/sql/join) tutorial.

## Connecting to my website

Now that I have all the back end work done, how to get it to the front end? PHP 
seemed to be the logical solution to me. It is an easy server side language you 
can easily integrate with html. It also relays information to MySQL without an 
issue. The best reference I found was 
[PHP's documentation](http://php.net/manual/en/book.mysql.php) for connecting PHP 
with MySQL. With these tools all available, I wrote a small PHP script to query 
the database table for my blog posts, return the last 5 in descending order, 
and echo the HTML onto the page. Now by doing this, when I add a new blog into 
my database, it automatically updates the top 5 on my home page.

Well updating my front page is all well and good, but what happens to all the 
rest of my posts? Well now my "Older Posts" button on the front page actually 
does something! Clicking that button now takes you to a new page which loads 
every post I've ever made. Again, I wrote a PHP script, but instead of limited 
it to the last 5 entries, I didn't limit it at all. A copy of the first PHP 
script can be found in my 
[Github](http://github.com/jawilson0502) One major caveat to that script - 
the variables $servername, $username, and $password will have to be set 
depending on your situation. I've also not included what they are set to for 
me, because that would just be silly.

## What next?
					
If you recall from my previous post, [Creating this Website: Part 1]({{
url_for('post', blog_id=3) }}) I had a few main goals lined out to accomplish. 
The great news is, I've accomplished most of them! I now have fully functional 
social media buttons at the bottom. (Insert reference to checking them out here) 
I also have a way to manage older posts (Yay this post!). I've also created a 
script to monitor the traffic on my website, 
[Writing my own Website Script]({{ url_for('post', blog_id=4) }})

The next step will be creating the tag system to make my blog easily searchable 
in a manner I control. I've laid the ground work while creating the MySQL 
database, now it will just be deciding how to integrate that in. I also want 
to freshen up the home page to maybe include a quick mini bio, as well as the 
search tags as well. Please feel free to tweet at me, or message me if you 
have any recommendations, I would love to hear them!
