from requests_html import HTMLSession

from files.files import create_log
from net.scanners.globals import files, nmap_scan, technologies
from net.scrapers import loop_links
from net.spider import get_page
from mvalidators.validator import is_valid_url

if __name__ == '__main__':
    print("丂丂⼕尺闩尸🝗尺", '\n')

    # Testing URL
    url = ""

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
