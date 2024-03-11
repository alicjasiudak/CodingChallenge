from typing import List

from DataAccess.IAPIService import IAPIService
from Model.Part import Part
from Model.Piece import Piece
from Model.Set import Set


class SetBuilder:
    def __init__(self, api_service: IAPIService):
        self.api = api_service

    def get_set_list(self) -> List[Set]:
        sets = self.api.fetch_sets()
        return [Set(**lego_set) for lego_set in sets]

    def get_set_by_name(self, set_name: str) -> Set:
        set_data = self.api.fetch_set_by_name(set_name)
        return Set(**set_data)

    def get_set_by_id(self, set_id: str) -> Set:
        set_data = self.api.fetch_set_by_id(set_id)
        pieces_data = set_data.get('pieces', [])

        # Create Piece instances for each piece in the set
        pieces = [Piece(part=Part(**piece['part']), quantity=piece['quantity']) for piece in pieces_data]

        return Set(id=set_data['id'], name=set_data['name'], setNumber=set_data['setNumber'], pieces=pieces,
                   totalPieces=set_data['totalPieces'])

    def get_full_set_data_by_name(self, set_name: str) -> Set:
        set_data = self.get_set_by_name(set_name)
        full_set_data = self.get_set_by_id(set_data.id)
        return full_set_data

    def _get_all_complete_set_data(self, set_id) -> Set:
        full_set_data = self.get_set_by_id(set_id)
        return full_set_data

    def get_all_sets_data(self) -> List[Set]:
        all_sets = self.get_set_list()
        complete_sets_data = []
        for every_set in all_sets:
            complete_set_data = self.get_set_by_id(every_set.id)
            complete_sets_data.append(complete_set_data)
        return complete_sets_data
