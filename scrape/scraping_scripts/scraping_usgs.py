#Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import requests


usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"


def doScrape():
    executable_path = {'executable_path': './chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    #Lookin at the USGS webpage
    titles = list()
    img_links = list()

    browser.visit(usgs_url)
    html = browser.html
    soup_usgs = BeautifulSoup(html, 'html.parser')

    results = soup_usgs.find_all('a', class_='itemLink product-item')
    for result in results:
        title = result.find('h3')
        if (title != None):
            titles.append(title.text)

    for title in titles:
        browser.visit(usgs_url)
        browser.click_link_by_partial_text(title)
        browser.find_link_by_text('Sample').click()
        img_links.append(browser.windows[1].url)
        browser.windows[1].close()

    hemisphere_image_urls = []
    for x in range(len(titles)):
        hemisphere_image_urls.append({"title": titles[x], "img_url": img_links[x]})

    #browser.quit()

    print(hemisphere_image_urls)

    return hemisphere_image_urls

doScrape()
