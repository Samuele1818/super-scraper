def normalize_link(homepage_url: str, link: str):
    """
    Avoid link to external sites, add the base url to provided link
    :param homepage_url: The URL of the home page (e.g https://www.website.com/)
    :param link: Link to normalize
    :return: Normalized link or None if link is not valid
    """
    # Check if link report to an external site
    if homepage_url == link:
        return homepage_url

    if homepage_url.endswith("/"):
        homepage_url = homepage_url[:-1]

    if link.find("http") != -1 and link.find(homepage_url) == -1:
        return None

    return homepage_url + link


def are_links_not_analyzed(discovered_links: dict):
    """
    Check if there are links not analyzed in the dict (value = N)
    :param discovered_links: Dict with links
    :return: True if there are links to analyze, false instead
    """
    return "N" in discovered_links.values()
