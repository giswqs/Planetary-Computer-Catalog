# Planetary-Computer-Catalog

[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/giswqs/Planetary-Computer-Catalog/blob/master/pc_catalog.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/giswqs/Planetary-Computer-Catalog/HEAD?labpath=pc_catalog.ipynb)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Introduction

The [Microsoft Planetary Computer](https://planetarycomputer.microsoft.com/) platform hosts a lot of publicly available geospatial datasets. This repo compiles the list of all geospatial datasets on Planetary Computer as a CSV file and as a JSON file, making it easier to find and use them programmatically. The list is updated daily.

A complete list of geospatial datasets on Planetary Computer is available [here](https://planetarycomputer.microsoft.com/catalog).

## Usage

This repo provides the list of geospatial datasets on Planetary Computer in two formats:

- Tab separated values (TSV) file: [pc_catalog.tsv](https://github.com/giswqs/Planetary-Computer-Catalog/blob/master/pc_catalog.tsv)
- JSON file: [pc_catalog.json](https://github.com/giswqs/Planetary-Computer-Catalog/blob/master/pc_catalog.json)

The TSV file can be easily read into a Pandas DataFrame using the following code:

```python
import pandas as pd

url = 'https://github.com/giswqs/Planetary-Computer-Catalog/raw/master/pc_catalog.tsv'
df = pd.read_csv(url, sep='\t')
df.head()
```

## Related Projects

- A list of open datasets on AWS: [aws-open-data](https://github.com/giswqs/aws-open-data)
- A list of open geospatial datasets on AWS: [aws-open-data-geo](https://github.com/giswqs/aws-open-data-geo)
- A list of open geospatial datasets on AWS with a STAC endpoint: [aws-open-data-stac](https://github.com/giswqs/aws-open-data-stac)
- A list of STAC endpoints from stacindex.org: [stac-index-catalogs](https://github.com/giswqs/stac-index-catalogs)
- A list of geospatial datasets on Microsoft Planetary Computer: [Planetary-Computer-Catalog](https://github.com/giswqs/Planetary-Computer-Catalog)
- A list of geospatial datasets on Google Earth Engine: [Earth-Engine-Catalog](https://github.com/giswqs/Earth-Engine-Catalog)
- A list of geospatial data catalogs: [geospatial-data-catalogs](https://github.com/giswqs/geospatial-data-catalogs)
