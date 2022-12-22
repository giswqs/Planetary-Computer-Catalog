import json
import pandas as pd
from pystac_client import Client

out_dir = "datasets"

endpoint = "https://planetarycomputer.microsoft.com/api/stac/v1"

cat = Client.open(endpoint)

datasets = []

for collection in cat.get_collections():
    data = collection.to_dict()
    print(data["id"])
    dataset = {}
    output = out_dir + "/" + data["id"] + ".json"
    with open(output, "w") as f:
        json.dump(data, f, indent=True)

    dataset["title"] = data["title"]
    dataset["id"] = data["id"]
    dataset["description"] = data["msft:short_description"]
    dataset["license"] = data["license"]

    if "msft:group_id" in data:
        dataset["group_id"] = data["msft:group_id"]
    else:
        dataset["group_id"] = ""
    dataset["container"] = data["msft:container"]
    dataset["storage_account"] = data["msft:storage_account"]

    dataset["keywords"] = data["keywords"]
    dataset["providers"] = [provider["name"] for provider in data["providers"]]
    dataset["link"] = data["links"][0]["href"]

    dataset["bbox"] = data["extent"]["spatial"]["bbox"][0]
    dataset["temporal"] = data["extent"]["temporal"]["interval"][0]

    if "cube:variables" in data:
        dataset["variables"] = list(data["cube:variables"].keys())
    else:
        dataset["variables"] = ""
    if "cube:dimensions" in data:
        dataset["dimensions"] = list(data["cube:dimensions"].keys())
    else:
        dataset["dimensions"] = ""

    if "item_assets" in data:
        dataset["assets"] = list(data["item_assets"].keys())
    else:
        dataset["assets"] = ""

    datasets.append(dataset)

print("Total datasets: ", len(datasets))

df = pd.DataFrame(datasets)
df["title"] = df["title"].apply(lambda x: x.title() if x[0].islower() else x)
df.sort_values(by=["title"], inplace=True)
df.to_csv("pc_catalog.tsv", index=False, sep="\t")
df.to_json("pc_catalog.json", orient="records", indent=4)
