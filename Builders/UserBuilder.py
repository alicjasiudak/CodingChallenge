from typing import List

from DataAccess.IAPIService import IAPIService
from Model.Part import Part
from Model.Piece import Piece
from Model.User import User


class UserBuilder:
    def __init__(self, api_service: IAPIService):
        self.api = api_service

    def get_user_list(self) -> List[User]:
        users = self.api.fetch_users()
        return [User(**user) for user in users]

    def get_from_json_by_name(self, username: str) -> User:
        user_data = self.api.fetch_user_by_name(username)
        return User(**user_data)

    def get_from_json_by_id(self, user_id: str) -> User:
        user_data = self.api.fetch_user_by_id(user_id)
        collection_data = user_data.get('collection', [])
        collection = self.create_pieces_from_user_collection(collection_data)
        return User(id=user_data['id'],
                    username=user_data.get('username'),
                    location=user_data.get('location'),
                    brickCount=user_data.get('brickCount'),
                    collection=collection)

    @staticmethod
    def create_pieces_from_user_collection(data: List[dict]) -> List[Piece]:
        pieces = []
        for item in data:
            piece_id = item['pieceId']
            for variant in item['variants']:
                # Convert color string to integer
                color_as_int = int(variant['color'])
                part = Part(designID=piece_id, material=color_as_int)
                piece = Piece(part=part, quantity=variant['count'])
                pieces.append(piece)
        return pieces


    # @staticmethod
    # def can_build_set(required_pieces: List[Piece], inventory_pieces: List[Piece]) -> bool:
    #     for required in required_pieces:
    #         matched = False
    #         for inventory in inventory_pieces:
    #             if (required.part.designID == inventory.part.designID and
    #                     required.part.material == inventory.part.material and
    #                     required.quantity <= inventory.quantity):
    #                 matched = True
    #                 break
    #         if not matched:
    #             return False
    #     return True


