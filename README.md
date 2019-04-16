# VeganFoodNewsAutoFacebookPoster

## Overview:

TODO

## Install:

1. To install the requirements to run the python scripts:

``` pip install -r requirements.txt ```

2. To initialize your sqlite database:

``` python createdb.py ```

3. To scan the the list of RSS feed to save to the database:

``` python ScanRSSFeeds.py ```


## Other functions:

- To change the RSS Feeds, edit the ScanRSSFeeds.py file manually

- To mark the current items in the database as hidden: 

``` python hideactiveitems.py ```
