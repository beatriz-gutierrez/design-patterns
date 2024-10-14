import requests
from abc import ABC, abstractmethod

class Client(ABC):
    @abstractmethod
    def fecth_data(self, url: str) -> dict[str, str]:
        pass


# Real subject
class HttpClient(Client):

    def fecth_data(self, url) -> dict[str, str]:
        print(f"> Making HTTP request to {url}...")

        response = requests.get(url, timeout=30)

        if response.status_code != 200:
            return f"> Error: {response.status_code}"
        return response.content


# Proxy pattern controls accest to the real subject,
# adds caching and lazy initialization
class HttpClientProxy(Client):

    def __init__(self):
        self._client = None
        self._cache = {}

    def fecth_data(self, url) -> dict[str, str]:
        # lazy initializatin and singleton
        if  not self._client:
            print(f"> Initializing (lazy init) HttpClient...")
            self._client = HttpClient()

        if not self._cache or not url in self._cache:
            print(f"Caching data for {url}...")
            self._cache[url] = self._client.fecth_data(url)
        print(f"Get cached data for {url}...")

        return self._cache[url]

if __name__ == "__main__":
    proxy = HttpClientProxy()

    url1 = "https://kartones.net"
    url2 = "https://google.com"

    proxy.fecth_data(url1)
    proxy.fecth_data(url1)
    proxy.fecth_data(url2)
    proxy.fecth_data(url2)
    proxy.fecth_data(url1)
    print(" > Keys in cache:")
    [print(k) for k in proxy._cache]