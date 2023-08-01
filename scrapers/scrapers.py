import requests


def files(url: str):
    """
    Find all the useful files of the website:
        - sitemap.xml
        - robots.txt
    and print the result
    """
    sitemap_req = requests.get(f"{url}/sitemap.xml")
    robots_req = requests.get(f"{url}/robots.txt")

    # If found print sitemap.xml content
    if sitemap_req.status_code == 200:
        print("sitemap.xml found: ")
        print(sitemap_req.content.decode(), '\n')

    # If found print robots.txt content
    if robots_req.status_code == 200:
        print("robots.txt found: ")
        print(robots_req.content.decode(), '\n')


