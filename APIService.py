import json
from typing import List

import requests

from Model.CollectionItem import CollectionItem
from Model.Color import Color
from Model.Part import Part
from Model.Piece import Piece
from Model.User import User
from Model.Set import Set
from Model.Variant import Variant


class APIService:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://d16m5wbro86fg2.cloudfront.net/api"

    def _fetch_json(self, endpoint) -> dict:
        """generic method for any given endpoint"""
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url)
        response.raise_for_status()  # Will raise HTTPError for bad responses
        return response.json()  # Directly parse and return the JSON response

    def fetch_user_by_name(self, username) -> User:
        """fetch a user by username"""
        user_data = self._fetch_json(f"user/by-username/{username}")
        return User(**user_data)

    def fetch_user_by_id(self, user_id) -> User:
        """fetch a user by id"""
        user_data = self._fetch_json(f"user/by-id/{user_id}")
        collection_data = user_data.get('collection', [])

        collection = [CollectionItem(pieceId=item['pieceId'],
                                     variants=[Variant(color=variant['color'], count=variant['count']) for variant in
                                               item['variants']])
                      for item in collection_data]

        return User(id=user_data['id'],
                    username=user_data.get('username'),
                    location=user_data.get('location'),
                    brickCount=user_data.get('brickCount'),
                    collection=collection)

    def fetch_users(self) -> List[User]:
        """fetch a list of users"""
        users_data = self._fetch_json("users")['Users']
        return [User(**user) for user in users_data]

    def fetch_colors(self) -> List[Color]:
        colors = self._fetch_json(f"colours")['colours']
        return [Color(**color) for color in colors]

    # /api/sets returns a list of the sets in the catalogue
    def fetch_sets(self) -> List[Set]:
        sets = self._fetch_json(f"sets")['Sets']
        return [Set(**lego_set) for lego_set in sets]

    # /api/set/by-name/{name} returns a summary of a single set
    def fetch_set_by_name(self, set_name) -> Set:
        lego_set = self._fetch_json(f"set/by-name/{set_name}")
        return Set(**lego_set)

    # /api/set/by-id/{id} returns the full data for a single set
    def fetch_set_by_id(self, set_id: str) -> Set:
        set_data = self._fetch_json(f"set/by-id/{set_id}")
        pieces_data = set_data.get('pieces', [])

        # Create Piece instances for each piece in the set
        pieces = [Piece(part=Part(**piece['part']), quantity=piece['quantity']) for piece in pieces_data]

        return Set(id=set_data['id'], name=set_data['name'], setNumber=set_data['setNumber'], pieces=pieces,
                   totalPieces=set_data['totalPieces'])
