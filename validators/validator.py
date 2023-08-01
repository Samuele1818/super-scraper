import requests


def is_valid_url(url: str):
    if url == "":
        return False

    try:
        requests.get(url)
        return True
    except Exception as e:
        # TODO: implement a correct error handling (show useful error message instead of exception message)
        print(e)
        return False
