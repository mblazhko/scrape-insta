from instagram_user import InstagramUser


class Hashtag:
    def __init__(self, user: InstagramUser) -> None:
        self.user = user

    def get_hashtag_info_with_provided_amount(
        self, tag_name: str, amount: int
    ) -> list[dict[str, int]]:
        post_list = self.user.cl.hashtag_medias_top_v1(
            name=tag_name, amount=amount
        )

        return self.get_post_data(post_list)

    def get_post_data(self, post_list) -> list[dict[str, int]]:
        post_user_list = []
        for post in post_list:
            item = post.dict()
            post_id = item["code"]
            user_id = item["user"]["pk"]
            output = {
                "post_id": post_id,
                "user_id": user_id,
            }
            post_user_list.append(output)

        return post_user_list

    def count_user_followers(self, user_id: int) -> int:
        return self.user.cl.user_info(user_id).dict()["follower_count"]