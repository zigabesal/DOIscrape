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
after a successful run the email_list.txt should be populated with emails
 
Note: running the script opens a Chrome browser window on your computer.

Deficiencies: 
 1. The script cannot (yet) scrape emails from sites
 that include the emails in separate javascript scripts. 
 
 2. The tool is pretty slow and ineficcient, as it opens a webbrowser window for each DOI it scrapes the emails for. 
To scrape 8000 articles for emails with this tool would probably take 
around 10h (on an average computer with a stable internet connection)
 
 3. The email_list.txt gets populated not only with the emails of the researchers, but with everything that matches the regular expression for an email(about 10% of what it scrapes is redundant). The generation of the email_list.txt needs further filtering or subsequent data cleaning is needed.
