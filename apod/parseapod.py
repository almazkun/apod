from urllib.request import urlopen
from html.parser import HTMLParser

LINK = "https://apod.nasa.gov/apod/astropix.html"

class RaiseError(Exception):
    pass


def open_url(url):
    try:
        return urlopen(url)
    except:
        raise RaiseError("Connection error")


def url_object_to_string(urlopen_object):
    result = urlopen_object.read()
    with open("page.html","w") as file:
        file.write(result.decode("utf-8"))
    return result.decode("utf-8")


class ContentFinder(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = set()
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    self.links.add(value)


"""
def __init__(self, title, author, image_tub, image_full, date, explanation):
        title = self.title
        author = self.author
        image_tub = self.image_tub
        image_full = self.image_full
        date = self.date
        explanation = self.explanation
"""



page = url_object_to_string(open_url(LINK))
parser = ContentFinder()

parser.feed(page)

print(parser.links)
