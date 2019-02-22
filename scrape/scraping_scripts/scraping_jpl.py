# Dependencies
from splinter import Browser
import time

url_jpl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'


def doScrape():
    executable_path = {'executable_path': './chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    # Using Splinter to visit JPL's webpage
    browser.visit(url_jpl)

    time.sleep(5)

    # JPL Homepage - going through first button
    browser.click_link_by_partial_text('FULL IMAGE')

    time.sleep(5)

    # JPL Homepage - going to image's landing page
    browser.click_link_by_partial_text('more info')

    time.sleep(5)

    # JPL featured image landing page - clicking on image
    featured_image_url = browser.find_by_tag('figure').find_by_tag('a')['href']
    print(featured_image_url)

    browser.quit()

    return featured_image_url

