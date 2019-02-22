import pandas as pd

facts_url = "http://space-facts.com/mars/"


def doScrape():

    # Getting the table of Mars Data using Pandas
    tables = pd.read_html(facts_url)
    df = tables[0]
    df.columns = ["Parameter", "Value"]
    df.set_index("Parameter", inplace=True)
    #df

    html_table = df.to_html()
    html_table = html_table.replace('\n', '')
    return html_table
