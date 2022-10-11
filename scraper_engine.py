'''
The function below takes as an input a DOI and returns an URL of the original article
It does that by interacting with the input box on the dx.doi.org website via a python package called Selenium
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
###importing the needed Selenium packages

def DoiToUrl(DOI):
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
  driver.get("https://dx.doi.org/")

  link = "https://dx.doi.org/"
  driver.get(link)
  box = driver.find_element("xpath", "/html/body/table[2]/tbody/tr[2]/td[1]/form/table/tbody/tr/td/p/input" )
  box.send_keys(DOI)
  box.submit()

  #this waits for the new page to load
  while(link == driver.current_url):
    time.sleep(1)

  redirected_url = driver.current_url

  return(redirected_url)
'''
defining the UrlToEmails function that takes the input 
in the form of an url 
(e.g. "https://pubmed.ncbi.nlm.nih.gov/15447798/")(quotation marks included)
and returns all the email adresses scraped from the provided url
'''
import re
from requests_html import HTMLSession
#importing the re package that enables us to use regular expressions
#importing a HTML parsing (web-scraping) library
#importing the DoiToUrl function I wrote in a separate file that uses a online DOI resolver to access desired articles

EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
#most used regular expression for email addresses(copied from the internet)

def UrlToEmails(url):
    session = HTMLSession()
    r = session.get(url)
    r.html.render()
    elist = []
    for re_match in re.finditer(EMAIL_REGEX, r.html.raw_html.decode()):
        elist.append(re_match.group())
    return elist    
