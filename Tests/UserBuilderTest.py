import unittest

from DataAccess.APIService import APIService
from Model.Part import Part
from Model.Piece import Piece
from Builders.UserBuilder import UserBuilder


class UserBuilderTest(unittest.TestCase):
    def test_create_pieces_from_user_collection(self):
        # Arrange
        api = APIService("https://d16m5wbro86fg2.cloudfront.net/api")
        ub = UserBuilder(api)
        # Arrange
        input_data = [
            {"pieceId": "123", "variants": [{"color": 2, "count": 4}, {"color": 1, "count": 2}]},
            {"pieceId": "456", "variants": [{"color": 3, "count": 3}]}
        ]
        expected_output = [
            Piece(part=Part(designID="123", material=2), quantity=4),
            Piece(part=Part(designID="123", material=1), quantity=2),
            Piece(part=Part(designID="456", material=3), quantity=3)
        ]

        # Act
        result = ub.create_pieces_from_user_collection(input_data)

        # Assert
        self.assertEqual(len(result), len(expected_output),
                         "The result should have the same number of pieces as expected.")
        for piece in expected_output:
            self.assertIn(piece, result, "The piece should be in the result.")


if __name__ == '__main__':
    unittest.main()
