from instagrapi import Client


def get_hashtag_info_with_provided_amount(
    cl: Client, tag_name: str, amount: int
):
    cl.delay_range = [1, 3]
    hashtag = cl.hashtag_medias_top_v1(name=tag_name, amount=amount)

    followers_list = []

    for item in hashtag:
        post_id = item.dict()["code"]
        user = item.dict()["user"]["username"]
        followers_count = cl.user_info_by_username_v1(user).dict()[
            "follower_count"
        ]

        output = {
            "post_id": post_id,
            "username": user,
            "follower_count": followers_count,
        }

        followers_list.append(output)

    return followers_list
