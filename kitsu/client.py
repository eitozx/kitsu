import urllib.parse
import requests
import aiohttp

from .object import Anime, Manga

BASE_URL = "https://kitsu.io/api/edge/"

class Client:
    
    def __init__(self):
        self._headers = {
            "Accept": "application/vnd.api+json",
            "Content-Type": "application/vnd.api+json"
        }

    def _api_path(self, ext : str = None):
        url = f"{BASE_URL}{ext}" if ext else BASE_URL
        return requests.get(url, headers = self._headers).json()

    # def search_all_anime(self, name : str):
    #     return self._api_path(f"anime?filter[text]={urllib.parse.quote(name)}")["data"]
    
    def search_anime(self, name : str):
        data = self._api_path(f"anime?filter[text]={urllib.parse.quote(name)}&page[limit]=1")
        return Anime(**data)

    # def search_all_manga(self, name : str):
    #     return self._api_path(f"manga?filter[text]={urllib.parse.quote(name)}")["data"]

    def search_manga(self, name : str):
        data = self._api_path(f"manga?filter[text]={urllib.parse.quote(name)}&page[limit]=1")
        return Manga(**data)