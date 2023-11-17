import os
from instagrapi import Client
from dotenv import load_dotenv

from login_user import login_user
from hashtag import get_hashtag_info_with_provided_amount
from make_session import make_session, get_session

load_dotenv()


USERNAME = os.getenv("USERNAME_INST")
PASSWORD = os.getenv("PASSWORD")


def scrape_hashtag_data(client, username, password, amount) -> list:
    try:
        session = get_session(client, f"session_{username}.json")
        if session:
            print(f"Session for {username} was found")
    except FileNotFoundError:
        print(f"Session for {username} not found, making new session...")
        make_session(cl=client, username=username, password=password)
        session = get_session(client, f"session_{username}.json")
        print(f"Session for {username} created")

    logged_in_user = login_user(
        session=session, cl=client, username=username, password=password
    )
    hashtag_info = get_hashtag_info_with_provided_amount(
        cl=logged_in_user, tag_name=input("Enter hashtag: "), amount=amount
    )

    return hashtag_info


if __name__ == "__main__":
    cl = Client()
    data = scrape_hashtag_data(
        client=cl,
        username=USERNAME,
        password=PASSWORD,
        amount=int(input("Enter amount of posts you want to get data for: "))
    )
    for item in data:
        print(item)
