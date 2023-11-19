import os
import time

from dotenv import load_dotenv

from instagram_user import InstagramUser
from hashtag import Hashtag

load_dotenv()


USERNAME = os.getenv("USERNAME_INST")
PASSWORD = os.getenv("PASSWORD")


def main(username, password) -> list:
    user = InstagramUser(username, password)
    user.login_user()

    hashtag_info = Hashtag(user=user)

    result = hashtag_info.get_hashtag_info_with_provided_amount(
        tag_name=input("Enter hashtag: "),
        amount=int(input("Enter amount of posts you want to get data for: "))
    )

    return result


if __name__ == "__main__":
    start = time.time()
    data = main(USERNAME, PASSWORD)
    print(data)
    end = time.time() - start
    print(f"End time is {end}")
