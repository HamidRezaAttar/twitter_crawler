import time
import pandas as pd
import snscrape.modules.twitter as sntwitter

from datetime import datetime, date, timedelta


class Twitter:
    def __init__(self):
        pass

    def search(
        self,
        query="Bitcoin",
        start="2021-01-01 00:00:00",
        end="2021-05-32 00:00:00",
        n_tweet=10,
    ):
        try:
            start_dt = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
            start_time = time.mktime(start_dt.timetuple())

            end_dt = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
            end_time = time.mktime(end_dt.timetuple())

            tweets_ls = []
            for i, tweet in enumerate(
                sntwitter.TwitterSearchScraper(
                    query
                    + " lang:en since_time:"
                    + str(int(start_time))
                    + " until_time:"
                    + str(int(end_time))
                    + " -filter:links -filter:replies"
                ).get_items()
            ):
                if i > int(n_tweet):
                    break
                tweets_ls.append([tweet.date, tweet.id, tweet.content, tweet.username])
            return pd.DataFrame(
                tweets_ls,
                columns=["Datetime", "Tweet Id", "Text", "Username"],
            )
        except Exception as e:
            print(f"error: {e}")

    def search_account(
        self,
        user_ls=["tim_cook", "BillGates"],
        start="2021-01-01 00:00:00",
        end="2021-05-32 00:00:00",
        n_tweet=10,
    ):
        try:
            start_dt = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
            start_time = time.mktime(start_dt.timetuple())

            end_dt = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
            end_time = time.mktime(end_dt.timetuple())

            tweets_list = []
            for n, k in enumerate(user_ls):
                for i, tweet in enumerate(
                    sntwitter.TwitterSearchScraper(
                        f" from:{user_ls[n]} lang:en since_time:{int(start_time)} until_time:{int(end_time)}"
                    ).get_items()
                ):
                    if i >= int(n_tweet):
                        break
                    tweets_list.append(
                        [tweet.date, tweet.id, tweet.content, tweet.username]
                    )
            return pd.DataFrame(
                tweets_list, columns=["Datetime", "Tweet Id", "Text", "Username"]
            )
        except Exception as e:
            print(f"error: {e}")
