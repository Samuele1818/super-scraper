from bs4 import BeautifulSoup
from mdutils.fileutils import MarkDownFile
from requests_html import HTMLSession

from scrapers.spider import get_links, get_page
from utils.utils import is_links_not_analyzed


def loop_links(session, log, discovered_links: dict):
    """
    Loop over the links and add news when discovered in the analyzed page.
    :param session: HTMLSession to make requests
    :param log: Log file to write information
    :param discovered_links: Dict with the links and their states (N(ot analyzed) or A(nalyzed))
    :return: None
    """
    # FIXME: Replace with URL passed by arguments if too slow
    # Loop all discovered pages of the site
    for link in discovered_links.copy():
        # If link already analyzed skip
        if discovered_links[link] == "N":
            # Get the page content
            current_page = get_page(session, link)
            # Analyze the page
            analyze_page(current_page, log, link, discovered_links)

            discovered_links[link] = "A"

    if is_links_not_analyzed(discovered_links):
        loop_links(session, log, discovered_links)


def analyze_page(page: object, log: MarkDownFile | None, url: str, discovered_links: dict):
    # Log the page url
    log.append_end(f"## {url}\n")

    metadata(page, log)
    get_links(page, log, discovered_links)


def forms_inputs(session: HTMLSession, log: MarkDownFile | None):
    return


def metadata(page: object, log: MarkDownFile | None):
    # Get the page (wait for javascript is not required)
    soup = BeautifulSoup(page.text, "html.parser")

    log.append_end("### Metadata\n")

    # Find all the metadata of the page
    meta = soup.find_all("meta")

    # Log all the metadata
    for m in meta:
        log.append_end(f"- `{m}`\n")


def files(session: HTMLSession, log: MarkDownFile | None, url: str):
    """
    Find all the useful files of the website:
        - sitemap.xml
        - robots.txt
    and print the result
    """
    sitemap_req = session.get(f"{url}/sitemap.xml")
    robots_req = session.get(f"{url}/robots.txt")

    log.append_end("# Files\n")

    # If found print sitemap.xml content
    log.append_end("## Sitemap\n")
    if sitemap_req.status_code == 200:
        log.append_end(sitemap_req.content.decode() + "\n")
    else:
        log.append_end("sitemap.xml not found\n")

    # If found print robots.txt content
    log.append_end("## Robots\n")
    if robots_req.status_code == 200:
        log.append_end(robots_req.content.decode() + "\n")
    else:
        log.append_end("robots.txt not found\n")
