from mdutils.fileutils import MarkDownFile
from requests_html import HTMLSession

from utils.utils import normalize_link


def get_page(session: HTMLSession, url: str):
    """
    Get the webpage content.
    Support javascript rendering
    :param session: HTMLSession to use requests_html
    :param url: Url of the webpage
    :return: The html of the page rendered (Javascript included) / None if errors
    """
    # Get the page
    r = session.get(url)

    # If page not found / errors occurred return None
    if r.status_code != 200:
        return None

    # Wait page loading to get Javascript loaded elements
    r.html.render(timeout=50000, keep_page=True)
    return r.html


def get_links(webpage: object, log: MarkDownFile | None, discovered_links: dict):
    """
    Get all links from the page.
    Add links into the dict to loop all pages discovered
    :param webpage: Page to analyze
    :param log: Log file to write report
    :param discovered_links: Dict containing the links to visit
    :return: List of all links discovered
    """
    homepage_url = list(discovered_links)[0]
    log.append_end("### Links\n")

    links = list(webpage.links)

    for link in links:
        # Insert link in the dictionary if not present and mark it with N(ot visited)
        link = normalize_link(homepage_url, link)
        if link not in discovered_links.keys():
            if link is not None:
                discovered_links[link] = "N"

                # Log all links found in the page
                log.append_end(f"- {link} \n")
    # Return a list with all the links contained in the webpage
    return links
