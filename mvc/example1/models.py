import json
import logging
import os

"""
json format of the stored urls as unique pairs,
being the last one the most recent:
{
    long_url: short_url
"""

MAPPINGS_FILE = "mapping_urls.json"
MAPPINGS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), MAPPINGS_FILE)

logging.basicConfig(level=logging.INFO)


class Url:
    def __init__(self, long_url: str):
        self._long_url = long_url
        self._short_url = Url.shorten(long_url)

    @property
    def short_url(self):
        return self._short_url

    @property
    def long_url(self):
        return self._long_url

    @short_url.setter
    def short_url(self, value):
        if not isinstance(value, str):
            raise ValueError("The short url value must be a string")
        self._short_url = value

    @long_url.setter
    def long_url(self, value):
        if not isinstance(value, str):
            raise ValueError("The long url value must be a string")
        self._long_url = value

    @staticmethod
    def _get_mapping_urls() -> dict:
        try:
            with open(MAPPINGS_PATH, "r") as file:
                return json.load(file)
        except:
            logging.info("The mappings file does not exist.")
            return {}

    @staticmethod
    def _save_mapping_urls(mappings_url: json):
        with open(MAPPINGS_PATH, "w") as file:
            json.dump(mappings_url, file)

    @staticmethod
    def _create_short_url() -> str:
        url_mappings = Url._get_mapping_urls()
        
        if not url_mappings:
            return Url._increment_short_url_format()
        
        last_short_url = next(reversed(url_mappings.values()))
        return Url._increment_short_url_format(last_short_url)

    @staticmethod
    def _get_by_long_url(long_url: str) -> str:
        mapping_urls = Url._get_mapping_urls()

        if not mapping_urls or not long_url in set(mapping_urls):
            return None

        return mapping_urls[long_url]

    @staticmethod
    def shorten(long_url: str) -> str:

        short_url = Url._get_by_long_url(long_url)

        if not short_url:
            short_url = Url._create_short_url()
            mapping_urls = Url._get_mapping_urls()
            mapping_urls[long_url] = short_url
            Url._save_mapping_urls(mapping_urls)

        return short_url

    @staticmethod
    def get_by_short_url(short_url: str) -> str:
        mapping_urls = Url._get_mapping_urls()

        if not short_url in set(mapping_urls.values()):
            logging.info("Short url not found in mappings.")

        return next(key for key, value in mapping_urls.items() if value == short_url)

    @staticmethod
    def _increment_short_url_format(url: str):
        """
        Increments string, that is:
            a -> b
            z -> aa
            az -> ba
            empty string -> a
        """
        if not url or url == "":
            return "a"

        last_char = url[-1]

        if last_char != "z":
            return url[:-1] + chr(ord(last_char) + 1)
        else:
            return url[:-1] + "a"
