import unittest

from DataAccess.APIService import APIService
from Model.Part import Part
from Model.Piece import Piece
from SetService import SetService


class TestCanBuildSet(unittest.TestCase):
    def setUp(self) -> None:
        self.api = APIService("https://d16m5wbro86fg2.cloudfront.net/api")
        self.set_service = SetService(self.api)

    def test_can_build_set_full_match(self):
        # Arrange
        set_service = SetService
        required_pieces = [
            Piece(part=Part(designID='3710', material='155', partType="rigid"), quantity=9),
            Piece(part=Part(designID='3710', material='152', partType="rigid"), quantity=7)
        ]
        inventory_pieces = [
            Piece(part=Part(designID='3710', material='155', partType=None), quantity=10),
            Piece(part=Part(designID='3710', material='152', partType=None), quantity=7)
        ]

        # Act
        result = set_service._can_build_set(required_pieces, inventory_pieces)

        # Assert
        self.assertTrue(result)

    def test_can_build_set_not_enough_quantity(self):
        # Arrange
        required_pieces = [
            Piece(part=Part(designID='3710', material='155'), quantity=9),
            Piece(part=Part(designID='3710', material='152'), quantity=7)
        ]
        inventory_pieces = [
            Piece(part=Part(designID='3710', material='155'), quantity=8),  # Not enough
            Piece(part=Part(designID='3710', material='152'), quantity=7)
        ]

        # Act
        result = self.set_service._can_build_set(required_pieces, inventory_pieces)

        # Assert
        self.assertFalse(result)

    def test_can_build_set_missing_piece(self):
        # Arrange
        required_pieces = [
            Piece(part=Part(designID='3710', material='155'), quantity=9),
            Piece(part=Part(designID='3710', material='152'), quantity=7)
        ]
        inventory_pieces = [
            # Missing the first required piece entirely
            Piece(part=Part(designID='3710', material='152'), quantity=7)
        ]

        # Act
        result = self.set_service._can_build_set(required_pieces, inventory_pieces)

        # Assert
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
