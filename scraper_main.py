from scraper_engine import *

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

for doi in DOI_list:
    url_1 = DoiToUrl(doi)
    emails_from_doi = UrlToEmails(url_1)
    email_list.append(list(set(emails_from_doi)))
###first line calls the DoiToUrl function from the engine(see scraper_engine for docu)
###second line calls the UrlToEmails function from the engine(see scraper_engine for docu)
###third line appends emails connected with a specific doi to the email list, the set function is there to get rid of duplicates

email_txt = open("email_list.txt", "w")

for list in email_list:
    for email in list:
        email_txt.write(email + "\n")

email_txt.close()        




       