from typing import List

from DataAccess.APIService import APIService
from SetService import SetService

URL = "https://d16m5wbro86fg2.cloudfront.net/api"


def main():
    api_service = APIService(base_url=URL)
    set_service = SetService(api_service)

    users = set_service.user_builder.get_user_list()
    for user in users:
        set_service.available_sets_to_build_by_username(user.username)

    # set_service.available_sets_to_build_by_username('technical-spike')


if __name__ == "__main__":
    main()
