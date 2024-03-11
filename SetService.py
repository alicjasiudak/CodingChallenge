from typing import List

from DataAccess.IAPIService import IAPIService
from Model.Piece import Piece
from Model.Set import Set
from Builders.SetBuilder import SetBuilder
from Builders.UserBuilder import UserBuilder

URL = "https://d16m5wbro86fg2.cloudfront.net/api"


class SetService:
    def __init__(self, api_service: IAPIService):
        self.api = api_service
        self.user_builder = UserBuilder(api_service)
        self.set_builder = SetBuilder(api_service)

    def available_sets_to_build_by_username(self, username: str) -> List[Set]:
        user = self.user_builder.get_full_user_data_by_name(username)
        all_sets = self.set_builder.get_all_sets_data()
        # eliminate the ones that have more total pieces than the user
        buildable_sets = [
            set_info.name
            for set_info in all_sets
            if set_info.totalPieces <= user.brickCount and self._can_build_set(set_info.pieces, user.collection)
        ]
        print(f"{username} is able to build {buildable_sets}")
        return buildable_sets

    def _can_build_set(self, required_pieces: List[Piece], inventory_pieces: List[Piece]) -> bool:
        missing_pieces = self._identify_missing_pieces(required_pieces, inventory_pieces)
        return len(missing_pieces) == 0

    def _identify_missing_pieces(self, required_pieces: List[Piece], inventory_pieces: List[Piece]) -> List[Piece]:
        missing_pieces = []
        for required in required_pieces:
            inventory_quantity = self._get_piece_quantity_from_inventory(required, inventory_pieces)
            if inventory_quantity < required.quantity:
                missing_pieces.append(required)
        return missing_pieces

    @staticmethod
    def _get_piece_quantity_from_inventory(piece: Piece, inventory_pieces: List[Piece]) -> int:
        for inventory_piece in inventory_pieces:
            if piece.part.designID == inventory_piece.part.designID and piece.part.material == inventory_piece.part.material:
                return inventory_piece.quantity
        return 0
