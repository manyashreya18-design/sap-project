import pandas as pd
import requests

# Download phishing datasets
print("Downloading PhishTank...")
open("phishtank.csv","wb").write(requests.get(
    "https://data.phishtank.com/data/online-valid.csv").content)

print("Downloading OpenPhish...")
open("openphish.txt","wb").write(requests.get(
    "https://openphish.com/feed.txt").content)

# Load datasets
p1 = pd.read_csv("phishtank.csv", usecols=["url"])
p1["label"] = 1

p2 = pd.read_csv("openphish.txt", names=["url"])
p2["label"] = 1

# Load legit dataset
leg = pd.read_csv("top-1m.csv", names=["rank","domain"])
leg["url"] = "http://" + leg["domain"]
leg["label"] = 0

# Combine all
all_data = pd.concat([p1, p2, leg[["url","label"]]])
all_data = all_data.drop_duplicates("url")
all_data = all_data.sample(frac=1)

# Save final dataset
all_data.to_csv("all_urls_dataset.csv", index=False)

print("DONE! all_urls_dataset.csv is created")

