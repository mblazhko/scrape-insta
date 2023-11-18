import time

from instagrapi import Client


def count_user_followers(cl: Client, user_id) -> int:
    return cl.user_info(user_id).dict()["follower_count"]


def get_hashtag_info_with_provided_amount(
    cl: Client, tag_name: str, amount: int
) -> list[dict[str, int]]:
    cl.delay_range = [0.15, 0.2]
    hashtags = cl.hashtag_medias_top_v1(name=tag_name, amount=amount)

    followers_list = []
    for hashtag in hashtags:
        item = hashtag.dict()
        post_id = item["code"]
        user_id = item["user"]["pk"]
        followers_count = count_user_followers(cl, user_id)
        output = {
            "post_id": post_id,
            "user_id": user_id,
            "follower_count": followers_count,
        }
        print(output)
        followers_list.append(output)

    return followers_list
