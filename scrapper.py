from bs4 import BeautifulSoup
import requests

jobPost = "https://www.linkedin.com/jobs/collections/recommended/?currentJobId=3971216047&discover=recommended&discoveryOrigin=JOBS_HOME_JYMBII&eBP=CwEAAAGQp6ObhZisL7VF-vHTaavpIKmgCrKRZzUvKD91tjS3HN_z0uFMtH1Y5iBXoSb8V5FWj0EhpQEcsEBxU7Gn1KK26Hsulcbx0v3BQf5vHzxRJ2E7a8ujDgriFUrQ6VSvAHAGmDLiGrpGVfAkT1fMXliS5qHF8kDYZbP3qvAaBLtPMjDQNfWg4c-Iuo6jt3B5e7GiAasAvwIUJx6ut6JN-IKK-OI59X7E9-VLYkSUT7CVbjYpUflTLjMyACA7uKgpF1S9ihCMRfWKEshMyKRa2j3X6R2jGZuDqTa09zXfiPNvl__b36uFkiqnGLF8qdkDs3AfRTWYEoIz1NDFuQe04uaiphQHT7YV1dOht3bcdj1CjZKbnVcqu5aheDMury8K8DbmQZkDav-YYB5mHFH5JmZZkt1NNmcNXnomM595F1ekE5ALKZ3Yu52KQL4ijLowY_szAw&refId=FbGe%2BO%2BlOe01celYXG%2BDmw%3D%3D&trackingId=YDRaD0aEiVZPGguwr737qQ%3D%3D"

try:
    source = requests.get(jobPost)
    soup = BeautifulSoup(source.text, 'html.parser')

    # Print the HTML containing the job position
    position_tag = soup.find('h1', class_="t-24 t-bold inline")
    if position_tag:
        print("Position HTML: ", position_tag.prettify())
        position = position_tag.get_text(strip=True)
        print("Position: ", position)
    else:
        print("Job position not found")

    # Print the HTML containing the company name
    company_tag = soup.find('div', class_="job-details-job-unified-top-card__company-name")
    if company_tag:
        print("Company Name HTML: ", company_tag.prettify())
        companyName = company_tag.get_text(strip=True)
        print("Company Name: ", companyName)
    else:
        print("Company name not found")

except Exception as e:
    print(e)
