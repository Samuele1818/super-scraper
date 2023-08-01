import json

from requests_html import HTMLSession
from tqdm import tqdm
from bs4 import BeautifulSoup


def loop_sublinks(url: str):



    return


def get_links(url):
    # Start the session
    session = HTMLSession()
    # Get the page
    r = session.get(url)
    # Wait page loading to get Javascript loaded elements
    r.html.render(timeout=10000)

    # Return a list with all the links contained in the webpage
    return list(r.html.links)
