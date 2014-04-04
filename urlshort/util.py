import base64
from urllib.parse import urlparse
import os

def random_string(strlen):
    """
    generate a random string given length
    """
    data = os.urandom(strlen)
    return base64.b64encode(data, b'~-').decode('ascii').replace('=','')

def url_is_valid(url):
    """
    return True if a url is able to be shortened otherwise False
    """
    try:
        u = urlparse(url)
    except:
        return False
    else:
        return u.scheme in ['http', 'ftp', 'https']
