import asyncio
import os
import time

from instagrapi import Client
from dotenv import load_dotenv

from login_user import login_user
from hashtag import get_hashtag_info_with_provided_amount
from make_session import get_or_create_new_session

load_dotenv()


USERNAME = os.getenv("USERNAME_INST")
PASSWORD = os.getenv("PASSWORD")


def scrape_hashtag_data(client, username, password) -> list:
    session = get_or_create_new_session(client, username, password)

    logged_in_user = login_user(
        session=session, cl=client, username=username, password=password
    )
    hashtag_info = get_hashtag_info_with_provided_amount(
        cl=logged_in_user,
        tag_name=input("Enter hashtag: "),
        amount=int(input("Enter amount of posts you want to get data for: "))
    )

    return hashtag_info


if __name__ == "__main__":
    cl = Client()
    start = time.time()
    data = scrape_hashtag_data(
        client=cl,
        username=USERNAME,
        password=PASSWORD,
    )
    end = time.time() - start
    print(f"End time is {end}")
