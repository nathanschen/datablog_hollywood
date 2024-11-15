import pandas as pd

files = '''full_2019_MA_after.csv
full_2019_OC_after.csv
full_2019_OC_before.csv
full_2019_RK_after.csv
full_2019_RK_before.csv
full_2019_RM_after.csv
full_2019_RM_before.csv
full_2020_BP_after.csv
full_2020_BP_before.csv
full_2020_JP_after.csv
full_2020_JP_before.csv
full_2020_LD_after.csv
full_2020_LD_before.csv
full_2020_RZ_after.csv
full_2020_RZ_before.csv
full_2021_AH_after.csv
full_2021_AH_before.csv
full_2021_DK_after.csv
full_2021_DK_before.csv
full_2021_FMD_after.csv
full_2021_FMD_before.csv
full_2021_YYJ_after.csv
full_2021_YYJ_before.csv
full_2022_ADB_after.csv
full_2022_ADB_before.csv
full_2022_JC_after.csv
full_2022_JC_before.csv
full_2022_TK_after.csv
full_2022_TK_before.csv
full_2022_WS_after.csv
full_2022_WS_before.csv
full_2023_BF_after.csv
full_2023_BF_before.csv
full_2023_JLC_after.csv
full_2023_JLC_before.csv
full_2023_KHQ_after.csv
full_2023_KHQ_before.csv
full_2023_MY_after.csv
full_2023_MY_before.csv'''.split()

sentiments = pd.DataFrame(columns = ["file", "negative", "neutral", "positive"])

# full_2019_MA_before.csv PUT IT BACK IN

for file in files:
    content_df = pd.read_csv(file)
    sentiment_counts = content_df['label'].value_counts()
    sentiment_counts = sentiment_counts.to_dict()

    new_row = [file, sentiment_counts["negative"], sentiment_counts["neutral"], sentiment_counts["positive"]]
    sentiments.loc[len(sentiments)] = new_row


print(sentiments)
sentiments.to_csv("sentiments", index=False)
