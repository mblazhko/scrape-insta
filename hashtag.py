import time

from instagrapi import Client


def get_hashtag_info_with_provided_amount(
    cl: Client, tag_name: str, amount: int
):
    cl.delay_range = [0.15, 0.2]
    hashtags = cl.hashtag_medias_top_v1(name=tag_name, amount=amount)

    followers_list = []
    for hashtag in hashtags:
        item = hashtag.dict()
        post_id = item["code"]
        user = item["user"]["pk"]
        followers_count = cl.user_info(user).dict()["follower_count"]
        output = {
            "post_id": post_id,
            "username": user,
            "follower_count": followers_count,
        }
        followers_list.append(output)
    return followers_list
