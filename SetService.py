from typing import List

from DataAccess.IAPIService import IAPIService
from Model.Piece import Piece
from Model.Set import Set
from Model.User import User
from Builders.SetBuilder import SetBuilder
from Builders.UserBuilder import UserBuilder

URL = "https://d16m5wbro86fg2.cloudfront.net/api"


class SetService:
    def __init__(self, api_service: IAPIService):
        self.api = api_service
        self.user_builder = UserBuilder(api_service)
        self.set_builder = SetBuilder(api_service)

    def available_sets_to_build_by_username(self, username: str) -> List[Set]:
        user = self._get_all_user_data(username)
        buildable_sets = self.find_buildable_by_user(user)
        return buildable_sets

    def find_buildable_by_user(self, user: User):
        all_sets = self._get_all_sets_data()
        # eliminate the ones that have more total pieces than the user
        potential_sets = []
        for single_set in all_sets:
            if single_set.totalPieces > user.brickCount:
                print(f"The user cannot build {single_set.name} set, too little pieces")
            else:
                potential_sets.append(single_set)

        buildable_sets = []
        for potential_set in potential_sets:
            if self._can_build_set(potential_set.pieces, user.collection):
                buildable_sets.append(potential_set.name)
        print(f"User {user.username} can build the following sets: {buildable_sets}")
        return buildable_sets

    def _get_all_user_data(self, username: str) -> User:
        user = self.user_builder.get_from_json_by_name(username)
        return self.user_builder.get_from_json_by_id(user.id)

    def _get_all_sets_data(self) -> List[Set]:
        all_sets = self.set_builder.get_set_list()
        complete_sets_data = []
        for every_set in all_sets:
            complete_set_data = self._get_all_complete_set_data(every_set.id)
            complete_sets_data.append(complete_set_data)
        return complete_sets_data

    def _get_all_complete_set_data(self, set_id) -> Set:
        full_set_data = self.set_builder.get_set_by_id(set_id)
        return full_set_data

    @staticmethod
    def _can_build_set(required_pieces: List[Piece], inventory_pieces: List[Piece]) -> bool:
        for required in required_pieces:
            matched = False
            for inventory in inventory_pieces:
                if (required.part.designID == inventory.part.designID and
                        required.part.material == inventory.part.material and
                        required.quantity <= inventory.quantity):
                    matched = True
                    break
            if not matched:
                return False
        return True
