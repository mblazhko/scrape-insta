from instagrapi import Client
from instagrapi.exceptions import LoginRequired
import logging

logger = logging.getLogger()


def login_user(
    session: dict, cl: Client, username: str, password: str
) -> Client:
    """
    Attempts to login to Instagram using either the provided session information
    """
    cl.set_settings(session)
    cl.login(username, password)

    # check if session is valid
    try:
        cl.get_timeline_feed()
    except LoginRequired:
        logger.info(
            "Session is invalid, need to login via username and password"
        )

        old_session = cl.get_settings()

        # use the same device uuids across logins
        cl.set_settings({})
        cl.set_uuids(old_session["uuids"])

        cl.login(username, password)

    return cl
