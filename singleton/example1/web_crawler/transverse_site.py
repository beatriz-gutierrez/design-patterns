from singleton_images import Singleton
from httplib2 import Http
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def traverse_site(max_links: int = 10):
    link_parser_singleton = Singleton()
    http = Http()

    # pages to parse in the queue
    while link_parser_singleton.queue_to_parse:

        if link_parser_singleton.to_visit and len(link_parser_singleton.to_visit) == max_links:
            return

        url = link_parser_singleton.queue_to_parse.pop()
        parsed_root = urlparse(url)

        try:
            status, response = http.request(url)
        except Exception:
            continue

        # skip if it is not a web page
        if status.get('content-type') != 'text/html':
            continue

        link_parser_singleton.to_visit.add(url)
        print(f'Added {url} to queue')

        beatysoup_scrapper = BeautifulSoup(response, 'html.parser')
        for link in BeautifulSoup.find_all(beatysoup_scrapper, 'a'):
            link_url = link.get('href')
            if not link_url:
                continue

            parsed_url = urlparse(link_url)
            # skip if link follows an external web page
            if parsed_url.netloc and parsed_url.netloc != parsed_root.netloc:
                continue

            # construct a full url from a link that is relative
            link_url = parsed_url.scheme + '://' + parsed_url.netloc + parsed_url.path

            # skip if added previously
            if link_url in link_parser_singleton.to_visit:
                continue

            # add the link to the queue
            link_parser_singleton.queue_to_parse.append(link_url)
