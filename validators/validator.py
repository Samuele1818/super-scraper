from requests_html import HTMLSession


def is_valid_url(session: HTMLSession, url: str):
    if url == "":
        return False

    try:
        session.get(url)
        return True
    except Exception as e:
        # TODO: implement a correct error handling (show useful error message instead of exception message)
        print(e)
        return False
