from instagrapi import Client


def make_session(cl: Client, username: str, password: str) -> None:
    cl.login(username, password)
    cl.dump_settings(f"session_{username}.json")
    print("Creating session is successful")


def get_session(cl: Client, filename: str):
    return cl.load_settings(filename)
