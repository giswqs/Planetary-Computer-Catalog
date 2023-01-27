import json
import pandas as pd
from pystac_client import Client

out_dir = "datasets"

endpoint = "https://planetarycomputer.microsoft.com/api/stac/v1"

cat = Client.open(endpoint)

datasets = []

for collection in cat.get_all_collections():
    link = collection.get_self_href()
    data = collection.to_dict()
    print(data["id"])
    dataset = {}
    output = out_dir + "/" + data["id"] + ".json"
    with open(output, "w") as f:
        json.dump(data, f, indent=4)

    dataset["title"] = data["title"]
    dataset["id"] = data["id"]
    dataset["description"] = data["msft:short_description"]

    dataset["bbox"] = ", ".join(
        [str(coord) for coord in data["extent"]["spatial"]["bbox"][0]]
    )

    state_date = data["extent"]["temporal"]["interval"][0][0]
    if state_date:
        dataset["start_date"] = state_date.split("T")[0]
    else:
        dataset["start_date"] = ""

    end_date = data["extent"]["temporal"]["interval"][0][1]
    if end_date:
        dataset["end_date"] = end_date.split("T")[0]
    else:
        dataset["end_date"] = ""

    if "msft:group_id" in data:
        dataset["group_id"] = data["msft:group_id"]
    else:
        dataset["group_id"] = ""
    dataset["container"] = data["msft:container"]

    if "msft:storage_account" in data:
        dataset["storage_account"] = data["msft:storage_account"]

    dataset["keywords"] = ", ".join(data["keywords"])
    dataset["providers"] = ", ".join(
        [provider["name"] for provider in data["providers"]]
    )

    dataset["license"] = data["license"]

    dataset["link"] = link

    if "cube:variables" in data:
        dataset["variables"] = ", ".join(list(data["cube:variables"].keys()))
    else:
        dataset["variables"] = ""
    if "cube:dimensions" in data:
        dataset["dimensions"] = ", ".join(list(data["cube:dimensions"].keys()))
    else:
        dataset["dimensions"] = ""

    if "item_assets" in data:
        dataset["assets"] = ", ".join(list(data["item_assets"].keys()))
    else:
        dataset["assets"] = ""

    datasets.append(dataset)

print("Total datasets: ", len(datasets))

df = pd.DataFrame(datasets)
df["title"] = df["title"].apply(lambda x: x.title() if x[0].islower() else x)
df.sort_values(by=["title"], inplace=True)
df.to_csv("pc_catalog.tsv", index=False, sep="\t")

with open("pc_catalog.json", "w") as f:
    json.dump(df.to_dict("records"), f, indent=4)
