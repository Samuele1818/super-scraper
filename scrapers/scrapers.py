import requests
from mdutils.fileutils import MarkDownFile


def files(url: str, log: MarkDownFile | None):
    """
    Find all the useful files of the website:
        - sitemap.xml
        - robots.txt
    and print the result
    """
    sitemap_req = requests.get(f"{url}/sitemap.xml")
    robots_req = requests.get(f"{url}/robots.txt")

    log.append_end("# Files\n")
    # If found print sitemap.xml content
    log.append_end("## Sitemap\n")
    if sitemap_req.status_code == 200:
        log.append_end(sitemap_req.content.decode())
    else:
        log.append_end("sitemap.xml not found\n")

    # If found print robots.txt content
    log.append_end("## Robots\n")
    if robots_req.status_code == 200:
        log.append_end(robots_req.content.decode())
    else:
        log.append_end("robots.txt not found\n")

