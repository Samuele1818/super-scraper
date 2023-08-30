from requests_html import HTMLSession

from files.files import create_log
from scrapers.scrapers import files, loop_links, nmap_scan, technologies
from scrapers.spider import get_page
from validators.validator import is_valid_url
2
if __name__ == '__main__':
    print("SSCraper...", '\n')

    # Testing URL
    url = "https://www.samuelesciatore.com/"

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

    # Search for useful files and make a whois
    files(session, url, log)
    nmap_scan(url, log)
    technologies(url, log)
    # Loop website pages and analyze them, log results
    loop_links(session, log, discovered_links)
