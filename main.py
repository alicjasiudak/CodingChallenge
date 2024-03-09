from APIService import APIService


def main():
    api = APIService()
    set = api.fetch_set_by_id("040f11ab-e301-4724-bacd-50841816e06b")
    colors = api.fetch_colors()
    users = api.fetch_users()
    user = api.fetch_user_by_id('353555ef-3135-4d3a-8e39-c680e1eb26d2')
    # print(user)
    print(set.pieces)
    # print(user.collection)
    # print(user.collection[0])




if __name__ == "__main__":
    main()
