from requests_html import HTMLSession

from files.files import create_log
from scrapers.scrapers import files, loop_links
from scrapers.spider import get_page
from validators.validator import is_valid_url

if __name__ == '__main__':
    print("SSCraper...", '\n')

    # Testing URL
    url = "https://www.a-boutall.com/"

    # Create the session to make requests
    session = HTMLSession()

    # Request URL till the inserted URL is valid and reachable11
    while not is_valid_url(session, url):
        url = input("Insert the URL of the website (home page URL): ")

    # Dict with all the discovered links
    discovered_links = {url: "N"}

    # Page passed to function to be analyzed, change on link loop
    current_page = get_page(session, url)

    print("Start scanning...", '\n')

    # Create the log file
    log = create_log()

    # Search for useful files in the website
    files(session, log, url)

    # Loop website pages and analyze them, log results
    loop_links(session, log, discovered_links)
