import asyncio
from twscrape import API, gather
from twscrape.logger import set_log_level

import requests
import pandas as pd

async def main():
    api = API()
    
    #2:00pm to 5:00pm
    #2023:
    #q = "michelle yeoh since:2023-03-12_13:00:00_PST until:2023-03-12_16:00:00_PST lang:en"
    #q = "brendan fraser since:2023-03-12_13:00:00_PST until:2023-03-12_16:00:00_PST lang:en"
    #q = "jamie lee curtis since:2023-03-12_13:00:00_PST until:2023-03-12_16:00:00_PST lang:en"
    #q = "ke huy quan since:2023-03-12_13:00:00_PST until:2023-03-12_16:00:00_PST lang:en"

    #2022:
    #q = "will smith since:2022-03-27_13:00:00_PST until:2022-03-27_16:00:00_PST lang:en"
    #q = "jessica chastain since:2022-03-27_13:00:00_PST until:2022-03-27_16:00:00_PST lang:en"
    #q = "troy kotsur since:2022-03-27_13:00:00_PST until:2022-03-27_16:00:00_PST lang:en"
    #q = "ariana debose since:2022-03-27_13:00:00_PST until:2022-03-27_16:00:00_PST lang:en"

    #2021:
    #q = "anthony hopkins since:2021-04-25_13:00:00_PST until:2021-04-25_16:00:00_PST lang:en"
    #q = "frances mcdormand since:2021-04-25_13:00:00_PST until:2021-04-25_16:00:00_PST lang:en"
    #q = "daniel kaluuya since:2021-04-25_13:00:00_PST until:2021-04-25_16:00:00_PST lang:en"
    #q = "youn yuh-jung since:2021-04-25_13:00:00_PST until:2021-04-25_16:00:00_PST lang:en"

    #2020:
    # a = "joaquin phoenix since:2020-02-09_14:00:00_PST until:2020-02-09_17:00:00_PST lang:en"
    # b = "renee zellweger since:2020-02-09_14:00:00_PST until:2020-02-09_17:00:00_PST lang:en"

    # e = "brad pitt since:2020-02-09_14:00:00_PST until:2020-02-09_17:00:00_PST lang:en"
    # f = "laura dern since:2020-02-09_14:00:00_PST until:2020-02-09_17:00:00_PST lang:en"

    #2019:
    # a = "rami malek since:2019-02-24_14:00:00_PST until:2019-02-24_17:00:00_PST lang:en"
    # b = "olivia colman since:2019-02-24_14:00:00_PST until:2019-02-24_17:00:00_PST lang:en"

    e = "mahershala ali since:2019-02-24_14:00:00_PST until:2019-02-24_17:00:00_PST lang:en"
    # f = "regina king since:2019-02-24_14:00:00_PST until:2019-02-24_17:00:00_PST lang:en"

    #9:00pm to 12:00am
    #2023:
    #q = "michelle yeoh since:2023-03-13_20:00:00_PST until:2023-03-13_23:00:00_PST lang:en"
    #q = "brendan fraser since:2023-03-13_20:00:00_PST until:2023-03-13_23:00:00_PST lang:en"
    #q = "jamie lee curtis since:2023-03-12_20:00:00_PST until:2023-03-12_23:00:00_PST lang:en"
    #q = "ke huy quan since:2023-03-12_20:00:00_PST until:2023-03-12_23:00:00_PST lang:en"

    #2022:
    #q = "will smith since:2022-03-27_20:00:00_PST until:2022-03-27_23:00:00_PST lang:en"
    #q = "jessica chastain since:2022-03-27_20:00:00_PST until:2022-03-27_23:00:00_PST lang:en"
    #q = "troy kotsur since:2022-03-27_20:00:00_PST until:2022-03-27_23:00:00_PST lang:en"
    #q = "ariana debose since:2022-03-27_20:00:00_PST until:2022-03-27_23:00:00_PST lang:en"

    #2021:
    #q = "anthony hopkins since:2021-04-25_20:00:00_PST until:2021-04-25_23:00:00_PST lang:en"
    #q = "frances mcdormand since:2021-04-25_20:00:00_PST until:2021-04-25_23:00:00_PST lang:en"
    #q = "daniel kaluuya since:2021-04-25_20:00:00_PST until:2021-04-25_23:00:00_PST lang:en"
    #q = "youn yuh-jung since:2021-04-25_20:00:00_PST until:2021-04-25_23:00:00_PST lang:en"

    #2020:
    # c = "joaquin phoenix since:2020-02-09_21:00:00_PST until:2020-02-10_00:00:00_PST lang:en"
    # d = "renee zellweger since:2020-02-09_21:00:00_PST until:2020-02-10_00:00:00_PST lang:en"

    # g = "brad pitt since:2020-02-09_21:00:00_PST until:2020-02-10_00:00:00_PST lang:en"
    # h = "laura dern since:2020-02-09_21:00:00_PST until:2020-02-10_00:00:00_PST lang:en"

    #2019:
    # c = "rami malek since:2019-02-24_21:00:00_PST until:2019-02-25_00:00:00_PST lang:en"
    # d = "olivia colman since:2019-02-24_21:00:00_PST until:2019-02-25_00:00:00_PST lang:en"

    # g = "mahershala ali since:2019-02-24_21:00:00_PST until:2019-02-25_00:00:00_PST lang:en"
    # h = "regina king since:2019-02-24_21:00:00_PST until:2019-02-25_00:00:00_PST lang:en"

    # file_a = open("2019_RM_before.csv","w")
    # async for tweet in api.search(a, limit=20000):
    #     print(tweet.id, tweet.user.username, tweet.date, tweet.lang, tweet.rawContent.replace("\n", " "), sep="\t", file = file_a)

    # file_b = open("2019_OC_before.csv","w")
    # async for tweet in api.search(b, limit=20000):
    #     print(tweet.id, tweet.user.username, tweet.date, tweet.lang, tweet.rawContent.replace("\n", " "), sep="\t", file = file_b)


    # file_c = open("2019_RM_after.csv","w")
    # async for tweet in api.search(c, limit=20000):
    #     print(tweet.id, tweet.user.username, tweet.date, tweet.lang, tweet.rawContent.replace("\n", " "), sep="\t", file = file_c)

    # file_d = open("2019_OC_after.csv","w")
    # async for tweet in api.search(d, limit=20000):
    #     print(tweet.id, tweet.user.username, tweet.date, tweet.lang, tweet.rawContent.replace("\n", " "), sep="\t", file = file_d)

    


    file_e = open("2019_MA_before.csv","w")
    async for tweet in api.search(e, limit=1):
        print(tweet.id, tweet.user.username, tweet.date, tweet.lang, tweet.rawContent.replace("\n", " "), sep="\t", file = file_e)

    # file_f = open("2019_RK_before.csv","w")
    # async for tweet in api.search(f, limit=20000):
    #     print(tweet.id, tweet.user.username, tweet.date, tweet.lang, tweet.rawContent.replace("\n", " "), sep="\t", file = file_f)


    # file_g = open("2019_MA_after.csv","w")
    # async for tweet in api.search(g, limit=20000):
    #     print(tweet.id, tweet.user.username, tweet.date, tweet.lang, tweet.rawContent.replace("\n", " "), sep="\t", file = file_g)

    # file_h = open("2019_RK_after.csv","w")
    # async for tweet in api.search(h, limit=20000):
    #     print(tweet.id, tweet.user.username, tweet.date, tweet.lang, tweet.rawContent.replace("\n", " "), sep="\t", file = file_h)


    # file_a.close()
    # file_b.close()
    # file_c.close()
    # file_d.close()
    file_e.close()
    # file_f.close()
    # file_g.close()
    # file_h.close()


if __name__ == "__main__":
    asyncio.run(main())
