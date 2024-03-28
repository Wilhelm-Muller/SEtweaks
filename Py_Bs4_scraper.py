import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE = "https://www.cse.ust.hk/~kwtleung/COMP4321/"
homepage = requests.get("https://www.cse.ust.hk/~kwtleung/COMP4321/Movie/115.html").text
response = requests.get("https://www.cse.ust.hk/~kwtleung/COMP4321/Movie/115.html")
soup = BeautifulSoup(homepage, 'lxml')
url = "https://www.cse.ust.hk/~kwtleung/COMP4321/testpage.htm"



title = soup.find('title').text

links_queue = set() # links found in said url
links_crawled = set() # links already explored
links_tags = soup.find_all("a") # Find all elements with the tag <a>

child_link = []
parent_link = []

#This part is dedicated to file size and modification date
if response.status_code == 200: #successful => 200
    file_size = len(response.content)
    last_mod_date = response.headers.get('last-modified')
print('Title: '+ title)
print(f"File Size: {file_size} bytes")
print(f"Last modified: {last_mod_date}")

print(response.url)

links = [link.get('href') for link in links_tags]
full_links = [urljoin(response.url, link) for link in links]
print(full_links)
url_cleaned = response.url.split(".htm")[0].strip()

for link in full_links:
    #print(f"{link}|{url_cleaned}|Link prefix comparable?{link.startswith(url_cleaned)}")
    if link.startswith(url_cleaned):
        child_link.append(link)
    if response.url.startswith(link.split(".htm")[0].strip()):
        parent_link.append(link)



print(child_link)
print(parent_link)