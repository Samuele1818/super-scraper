from mdutils.fileutils import MarkDownFile

from files.files import create_log
from scrapers.scrapers import files
from scrapers.spider import loop_sublinks, get_links
from validators.validator import is_valid_url

if __name__ == '__main__':
    print("SSCraper...", '\n')
    url = "https://www.a-boutall.com/"

    # Request URL till the inserted URL is valid and reachable11
    while not is_valid_url(url):
        url = input("Insert the URL of the website (home page URL): ")

    # Create the log file
    log = create_log()

    print("Start scanning...", '\n')

    # Search for useful files in the website
    files(url, log)

    loop_sublinks(url)





