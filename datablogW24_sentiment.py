import asyncio
from twscrape import API, gather
from twscrape.logger import set_log_level
import requests
import math
import pandas as pd

model = "cardiffnlp/twitter-roberta-base-sentiment-latest"
hf_token = ["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",
            "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",
            "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",
            "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"]

API_URL = "https://api-inference.huggingface.co/models/" + model
# headers = {"Authorization": "Bearer %s" % (hf_token)}



def analysis(data, token_index):
    headers = {"Authorization": "Bearer %s" % (hf_token[token_index])}
    payload = dict(inputs=data, options=dict(wait_for_model=True))
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()





name = "2023_MY_before.csv"
print(name)


content_df = pd.read_csv(name, sep="\t", names = ["tweet.id", "tweet.user.username", "tweet.date", "tweet.lang", "tweet.rawContent"])
content_df = content_df.drop_duplicates()
content_df = content_df.dropna(axis = 0)

if len(content_df) > 1000:
    subset_df = content_df.sample(n=1000, replace=False, random_state=2023)
    content_df = subset_df

# content_df = content_df[596:600]

# print(content_df)

tweet_label = []
tweet_score = []
index = 0
# content_df.iloc[:, 4]

for tweet in content_df["tweet.rawContent"]:
    index = index + 1
    print(index)
    # print(tweet)
    try:    
        result = analysis(tweet, math.floor(index/280))
        # print(result)
        # print(result[0][0]["label"])
        # print(result[0][0]["score"])

        tweet_label.append(result[0][0]["label"])
        tweet_score.append(result[0][0]["score"])
    except ValueError as e:
        print(f"Error encoding JSON: {e}")

print(len(content_df))
print(len(tweet_label))
print(len(tweet_score))

content_df["label"] = tweet_label
content_df["score"] = tweet_score


new_name = "full_" + name
print(new_name)
content_df.to_csv(new_name, index=False)

sentiment_counts = content_df['label'].value_counts()
print(sentiment_counts)





