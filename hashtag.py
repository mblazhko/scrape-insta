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
        if not post_list:
            print(f"{amount} posts for {tag_name} wasn't found")
        else:
            print(f"{amount} posts for {tag_name} was found")

        return self.get_all_post_data(post_list)

    def get_all_post_data(self, post_list) -> list[dict[str, int]]:
        post_user_list = []
        for post in post_list:
            output = self.get_one_post_data(post)
            post_user_list.append(output)

        return post_user_list

    def get_one_post_data(self, post) -> dict:
        item = post.dict()
        post_id = item["code"]
        user_id = item["user"]["pk"]
        followers_count = self.count_user_followers(user_id)
        output = {
            "post_id": post_id,
            "user_id": user_id,
            "followers_count": followers_count
        }
        print(f"Info about post '{post.id}' with user {user_id} was gotten")
        return output

    def count_user_followers(self, user_id: int) -> int:
        return self.user.cl.user_info(user_id).dict()["follower_count"]
