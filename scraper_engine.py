from selenium import webdriver
from bs4 import BeautifulSoup
import re
import requests
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def DoiToUrl(DOI):
  driver = webdriver.Firefox()
  driver.get("https://dx.doi.org/")

  link = "https://dx.doi.org/"
  driver.get(link)
  box = driver.find_element("xpath", "/html/body/table[2]/tbody/tr[2]/td[1]/form/table/tbody/tr/td/p/input" )
  box.send_keys(DOI)
  box.submit()

  #this waits for the new page to load
  while(link == driver.current_url):
    time.sleep(1)

  url = driver.current_url
  driver.quit()
  return(url)

def ScrapeUrl(url):
    

    

    # Using Selenium to get the page source with javascript executed
    driver = webdriver.Firefox()
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Extracting emails using BeautifulSoup
    emails = []
    for link in soup.find_all('a'):
        email = link.get('href')
        if email and 'mailto:' in email:
            email = email.replace('mailto:', '')
            emails.append(email)

    # Collecting all links from the website
    links = []
    for link in soup.find_all('a'):
        link = link.get('href')
        if link and link.startswith(url):
            links.append(link)
        elif link and not link.startswith(url):
            links.append(url+link)

    # Repeat the process for all the links found in the initial page
    for link in links:
        try:
            driver.get(link)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a'):
                email = link.get('href')
                if email and 'mailto:' in email:
                    email = email.replace('mailto:', '')
                    emails.append(email)
        except:
            pass

    # Removing duplicates
    emails = list(set(emails))

    

    driver.quit()
    return(emails)


def Scrape():

    

    email_list = []
    ### this list will store the scraped emails
    DOI_list = []
    ###this list will store the DOI numbers of the articles we want to scrape for emails
    
    with open("sampleDOI.txt") as f:
        unfiltered_DOI_list = f.readlines()
    ###these two lines of code open text files and read each separate line of the file (DOI) into a list (of unfiltered DOIs that contain whitespace)
    for unfiltered_doi in unfiltered_DOI_list:
        doi = unfiltered_doi.strip()
        DOI_list.append(doi)
    ###these three lines of code strip lines that are read from the text file of unwanted white space and store the stripped DOIs into our DOI_list
    with open('email_list.txt') as e:
        set_scraped = set([line.rstrip() for line in e])
        
        for doi in DOI_list:
            if doi not in set_scraped:
                url_1 = DoiToUrl(doi)
                emails_from_doi = ScrapeUrl(url_1)
                email_list.append(emails_from_doi)
                
                email_txt = open("email_list.txt", "a+")

                for list in email_list:
                    for email in list:
                        email_txt.write(doi + "\n")
                        email_txt.write(email + "\n")

                email_txt.close()
                email_list = []
