import requests
import sys
from fake_useragent import UserAgent

def web_check():
    ua = UserAgent(use_cache_server=False)
    header = {'user-agent': ua.random}
    print(header)
    try:
        with open("FILE_LOCATION", "r") as f:
            for url in f:
                page = requests.get(url.strip(), headers=header)
                if page.status_code == requests.codes.ok:
                    print("Website {0} is reachable with code: {1}".format(url.strip(), page.status_code))
                else:
                    print("Website {0} is NOT reachable with code: {1}".format(url.strip(), page.status_code))
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
web_check()
