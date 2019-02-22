# I've separated each part of the Jupyter Notebook into separate scripts to make it easier to read and understand.

import scrape.scraping_scripts.scraping_usgs as usgs
import scrape.scraping_scripts.scraping_facts as facts
import scrape.scraping_scripts.scraping_twitter as twitter
import scrape.scraping_scripts.scraping_jpl as jpl
import scrape.scraping_scripts.scrape_nasa as nasa

def scrape():
    # Dictionary holding data
    mars_data = dict()

    nasas = nasa.doScrape()
    mars_data["nasa_title"] = nasas['title']
    mars_data["nasa_p"] = nasas['text']
    print("Finished processing Nasa data")

    mars_data["featured_image_url"] = jpl.doScrape()
    print("Finished processing JPL data")

    mars_data["mars_weather"] = twitter.doScrape()
    print("Finished processing Twitter data")

    mars_data["facts"] = facts.doScrape()
    print("Finished processing Facts data")

    mars_data["usgs"] = usgs.doScrape()
    print("Finished processing USGS data")

    return mars_data

