# Dependencies
from bs4 import BeautifulSoup
import requests

# URL to be scraped
url_nasa = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

def doScrape():

    # Retrieve page with the requests module
    response_nasa = requests.get(url_nasa)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response_nasa.text, 'html.parser')

    # Looking for the div with the articles
    results = soup.find_all('div', class_='slide')

    # Saving the title and description of Nasa's latest news article
    news_title = results[0].find('div', class_='content_title').text
    news_p = results[0].find('div', class_='rollover_description_inner').text

    return {"title": news_title, "text":news_p}
