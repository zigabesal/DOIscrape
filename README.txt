What these two scripts do is take a text file with DOI's (sampleDOI.txt, contains DOI's) as input and populate an empty text file (email_list.txt, empty) with emails connected to the authors of the corresponding articles

The scripts use a python package called Selenium, which allows direct input and manipulation of the browser engine.
The script uses this in combination with the dx.doi.org 
website to resolve the DOI's, access the journal sites, and
scrape the emails from the journal sites.



Before using you should make sure: 

Python 3.0.0 or above is installed on your system
Google Chrome is installed on your system
These Python packages are installed (versions used in the creation of the scripts):
requests_html==0.10.0
selenium==4.5.0
webdriver_manager==3.8.3
The script was made and tested in the Ubuntu 22.04 environment
I suspect running it on windows would require some extra troubleshooting

!!! scraper_engine.py, scraper_main.py, sampleDOI.txt and email_list.txt
 are in the SAME directory
 
 To use :
run scraper_main.py 
after a successful run the email_list.txt should be populated with DOI'S and coresponding emails in pairs 
 
Note: running the script opens a Chrome browser window on your computer.

Update: the script now parses the javascript, so it can scrape the emails that are hidden in pop-up windows or possible links.
 
The tool is pretty slow and ineficcient, as it opens a webbrowser window for each DOI it scrapes the emails for. 
It also clicks on every possible clickable thing on the site to scrape the possible emails from
Scraping emails from 100 DOI's takes about two hours
The tool is inefficient, but robust
 
