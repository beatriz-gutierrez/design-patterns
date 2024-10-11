from threading import Thread
from singleton_images import Singleton
from httplib2 import Http
from bs4 import BeautifulSoup
from urllib.parse import urljoin

import os
from urllib.request import urlretrieve

class ImageDonwloaderThread(Thread):
    """
    A thread for downloading images in parallel.
    """
    def __init__(self, thread_id: str, name: str, counter: int):
        Thread.__init__(self)
        self.thread_name = name
        self.thread_id = thread_id
        self.counter = counter

    def _download_images(self):
        singleton = Singleton()
        http_to_visit = Http()

        while singleton.to_visit:
            url = singleton.to_visit.pop()

            print(f'Starting download images from {url}')

            try:
                _, response =  http_to_visit.request(url)
            except Exception:
                print('error when reading http page')
                continue

            beaty_soup =  BeautifulSoup(response, 'html.parser')
            images = BeautifulSoup.find_all(beaty_soup, 'img')

            base_path = os.path.dirname(os.path.abspath(__file__))
            for image in images:
                src_image = image.get('src')
                src_image = urljoin(url, src_image)

                basename_image =  os.path.basename(src_image)

                if src_image not in singleton.downloaded:
                    singleton.downloaded.add(src_image)
                    print(f'Downloading {src_image}')
                    urlretrieve(src_image, os.path.join(base_path, 'images', basename_image))

            print(f'{self.thread_name} thread finished downloading images from {url}')

    def run(self):
        print(f'Starting thread {self.name}')
        self._download_images()
        print(f'Finished thread {self.name}')
