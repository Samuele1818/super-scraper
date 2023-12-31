import asyncio
import json
import re

from mdutils.fileutils import MarkDownFile
from requests_html import HTMLSession

from net.spider import get_links, get_page
from mutils.utils import are_links_not_analyzed


def loop_links(session: HTMLSession, log: MarkDownFile | None, discovered_links: dict):
    """
    Loop over the links and add news when discovered in the analyzed page.
    :param session: HTMLSession to make requests
    :param log: Log file to write information
    :param discovered_links: Dict with the links and their states (N(ot analyzed) or A(nalyzed))
    :return: None
    """
    # TODO: Replace with URL passed by arguments if too slow
    # Loop all discovered pages of the site
    log.append_end("# Pages\n")
    for link in discovered_links.copy():
        # If link already analyzed skip
        if discovered_links[link] == "N":
            # Get the page content
            current_page = get_page(session, link)

            # Analyze the page
            print(f"Analyzing: {link}")
            analyze_page(current_page, log, link, discovered_links)

            # Mark link as analyzed
            discovered_links[link] = "A"

    if are_links_not_analyzed(discovered_links):
        loop_links(session, log, discovered_links)


def analyze_page(page: object, log: MarkDownFile | None, url: str, discovered_links: dict):
    """
    Analyze the content of the webpage and log the results
    :param page: Page to analyze
    :param log: Log file to write report
    :param url: Url of the webpage
    :param discovered_links: Dict containing the links to visit
    :return: None
    """
    # Log the page url
    log.append_end(f"## {url}\n")

    if page is None:
        # TODO: Add more information about the error
        log.append_end("Error while getting page. Page could not exits / temporally not reachable\n")
        return

    metadata(page, log)
    get_links(page, log, discovered_links)
    forms_inputs(page, log)
    cookies(page, log)
    contacts(page, log)


def forms_inputs(page: object, log: MarkDownFile | None):
    """
    Log any form/input retrieved in the page with relative information
    :param page: Page to analyze
    :param log: Log file to write report
    :return: None
    """
    log.append_end("### Forms and Inputs\n")

    forms = page.find("form")
    inputs = page.find("input")

    log.append_end("#### Forms \n")
    # Log all the metadata
    for form in forms:
        log.append_end(f"- `{form}`\n")

    log.append_end("#### Inputs \n")
    # Log all the metadata
    for input in inputs:
        log.append_end(f"- `{input}`\n")


def contacts(page: object, log: MarkDownFile | None):
    """
    Find contacts from the page, such as socials and emails
    :param page: Page to analyze
    :param log: Log file to write report
    :return: None
    """
    # TODO improve the function
    text = page.text

    log.append_end("### Contacts\n")

    log.append_end("#### Emails\n")

    # Check if text in the page represents an email
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    for email in emails:
        log.append_end(f"- {email}\n")

    # Load the file with the list of socials name as a JSON
    with open('./lists/social.json', 'r') as social_file:
        social_networks = json.load(social_file)

        # Create a pattern for matching URLs
        pattern = '|'.join(re.escape(url) for url in social_networks.values())

        # Find all matches in the text
        matches = re.findall(pattern, text)

        # Get the social network names from the matches
        matched_social_networks = [name for name, url in social_networks.items() if url in matches]

        log.append_end("#### Socials\n")

        # Check if text in the page represents a social
        for social in matched_social_networks:
            log.append_end(f"- {social}\n")


def cookies(page: object, log: MarkDownFile | None):
    log.append_end("### Cookies\n")
    asyn = asyncio.get_event_loop()
    page_cookies = asyn.run_until_complete(page.page.cookies())

    for cookie in page_cookies:
        log.append_end(f"- `{cookie}`\n")


def metadata(page: object, log: MarkDownFile | None):
    """
    Get metadata of page and write to log
    :param page: Page to analyze
    :param log: Log file to write report
    :return: None
    """
    log.append_end("### Metadata\n")

    meta = page.find("meta")

    # Log all the metadata
    for m in meta:
        log.append_end(f"- `{m}`\n")