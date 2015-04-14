# webparser-crawler
Some website parsers and crawlers in python with the Beautiful Soup and Requests libraries

Requires Selenium, Beautiful Soup, and Requests libraries to be installed on the machine.


Usage:  Run python2.7 crawl.py database.txt in terminal, where database.txt is a list of LinkedIn page numbers to scrape data from.

This program is specific to one project: It scrapes the number of followers from each LinkedIn webpage and deposits the result into a txt file that is (today's-date).txt

If the URL is invalid, then the txt file will have a message on that line that says so.

I also added a feature that allows the user to watch the crawl happen.  When the program is run, a firefox window will open and each LinkedIn webpage will show in the browser as the program goes through it.

I also attempted to add a feature that would make it easier to get past LinkedIn's security system, but I ran out of time and may come back to it at a later date.

##Issues and questions can be directed towards srwilliams444@gmail.com

