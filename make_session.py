from instagrapi import Client


def make_session(cl: Client, username: str, password: str) -> None:
    cl.login(username, password)
    cl.dump_settings(f"session_{username}.json")
    print("Creating session is successful")


def get_session(cl: Client, filename: str) -> dict:
    return cl.load_settings(filename)


def get_or_create_new_session(
        client: Client, username: str, password: str
) -> dict:
    try:
        session = get_session(client, f"session_{username}.json")
        if session:
            print(f"Session for {username} was found")
    except FileNotFoundError:
        print(f"Session for {username} not found, making new session...")
        make_session(cl=client, username=username, password=password)
        session = get_session(client, f"session_{username}.json")
        print(f"Session for {username} created")

    return session
