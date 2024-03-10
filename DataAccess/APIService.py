from abc import ABC
from typing import List

import requests

from DataAccess.IAPIService import IAPIService
from Model.Color import Color


class APIService(IAPIService, ABC):
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()

    def _fetch_json(self, endpoint) -> dict:
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def fetch_user_by_id(self, user_id) -> dict:
        user_data = self._fetch_json(f"user/by-id/{user_id}")
        return user_data

    def fetch_user_by_name(self, username) -> dict:
        user_data = self._fetch_json(f"user/by-username/{username}")
        return user_data

    def fetch_users(self) -> dict:
        users_data = self._fetch_json("users")['Users']
        return users_data

    def fetch_colors(self) -> List[Color]:
        colors = self._fetch_json(f"colours")['colours']
        return [Color(**color) for color in colors]

    def fetch_sets(self) -> dict:
        sets = self._fetch_json(f"sets")['Sets']
        return sets

    def fetch_set_by_name(self, set_name) -> dict:
        set_data = self._fetch_json(f"set/by-name/{set_name}")
        return set_data

    def fetch_set_by_id(self, set_id: str) -> dict:
        set_data = self._fetch_json(f"set/by-id/{set_id}")
        return set_data
