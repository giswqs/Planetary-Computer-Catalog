import json
from pystac_client import Client

out_dir = 'datasets'

endpoint = 'https://planetarycomputer.microsoft.com/api/stac/v1'

cat = Client.open(endpoint)

for collection in cat.get_collections():
    dataset = collection.to_dict()
    print(dataset['id'])
    output = out_dir + '/' + dataset['id'] + '.json'
    with open(output, 'w') as f:
        json.dump(dataset, f, indent=True)