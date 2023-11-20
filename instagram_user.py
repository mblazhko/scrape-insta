import os

from instagrapi import Client
import logging

from instagrapi.exceptions import PleaseWaitFewMinutes, LoginRequired


class InstagramUser:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        self.cl = Client()
        self.cl._delay_range = [0.15, 0.2]
        self.session_file_name = f"session_{self.username}.json"
        self.session = self.get_or_create_new_session()

    def set_client_delay_range(
            self,
            min_value: int | float,
            max_value: int | float
    ) -> None:
        self.cl._delay_range = [min_value, max_value]

    def login_user(self) -> None:
        """
        Attempts to log in to Instagram using either the provided session
        information
        """
        self.cl.set_settings(self.session)
        self.cl.login(self.username, self.password)

        # check if the session is valid
        try:
            self.cl.get_timeline_feed()
        except (LoginRequired, PleaseWaitFewMinutes):
            print(
                "Session is invalid, need to login via username and password"
            )

            old_session = self.cl.get_settings()

            # use the same device uuids across logins
            self.cl.set_settings({})
            self.cl.set_uuids(old_session["uuids"])

            self.cl.login(self.username, self.password)
            self.delete_expired_session()
            self.make_session()

    def get_or_create_new_session(self) -> dict:
        try:
            session = self.get_session()
            if session:
                print(f"Session for {self.username} was found")
        except FileNotFoundError or PleaseWaitFewMinutes:
            print(
                f"Session for {self.username} not found, making new session..."
            )
            self.make_session()
            session = self.get_session()
            print(f"Session for {self.username} created")

        return session

    def make_session(self) -> None:
        self.cl.login(self.username, self.password)
        self.cl.dump_settings(self.session_file_name)
        print("Session was created")

    def get_session(self) -> dict:
        return self.cl.load_settings(self.session_file_name)

    def delete_expired_session(self) -> None:
        os.remove(self.session_file_name)
        logging.info(f"Expired session  for {self.username} was deleted")
        