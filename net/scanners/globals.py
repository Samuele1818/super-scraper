import socket

import webtech
import nmap3

from mdutils.fileutils import MarkDownFile
from requests_html import HTMLSession


def nmap_scan(url: str, log: MarkDownFile | None):
    """
    Log the whois checkup of the site
    :param log: Log file to write report
    :param url: Url of the webpage
    :return: None
    """
    # Format the URL for gehostbyname
    url = url.replace("https://", "").replace("/", "")

    ip_address = socket.gethostbyname(url)
    log.append_end("# Target Information\n")
    log.append_end(f"IP: {ip_address}" + "\n\n")

    nmap = nmap3.Nmap()
    log.append_end("## Nmap Scan\n")
    log.append_end("### Ports\n")
    log.append_end(str(nmap.scan_top_ports(ip_address)) + "\n\n")
    log.append_end("### OS\n")
    log.append_end(str(nmap.nmap_os_detection(ip_address)) + "\n\n")
    # log.append_end("### Subnet\n")
    # log.append_end(str(nmap.nmap_subnet_scan(ip_address)) + "\n\n")


def technologies(url: str, log: MarkDownFile | None):
    """
    Log the technologies checkup of the site
    :param log: Log file to write report
    :param url: Url of the webpage
    :return: None
    """
    log.append_end("## Technologies\n")
    try:
        wt = webtech.WebTech(options={'json': True})
        report = wt.start_from_url(url)
        log.append_end(str(report) + "\n\n")
    except webtech.utils.ConnectionException:
        log.append_end("Connection error" + "\n\n")


def files(session: HTMLSession, url: str, log: MarkDownFile | None):
    """
    Find all the useful files of the website:
        - sitemap.xml
        - robots.txt
    and print the result
    :param session: HTMLSession to use requests_html
    :param log: Log file to write report
    :param url: Url of the webpage
    :return:
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
