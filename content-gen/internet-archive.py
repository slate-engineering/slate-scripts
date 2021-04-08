import internetarchive as ia

from internetarchive import search_items

# example url https://archive.org/details/ucberkeley-webcast-PL3E89002AA9B9879E
# id would be ucberkeley-webcast-PL3E89002AA9B9879E
collection_id = "ucberkeley-webcast-PL3E89002AA9B9879E"

file_id_arr = search_items(f"collection:{collection_id}")

for file_id in file_id_arr:
    # dry run only gets url of items in a collection, set to false to actually download
    ia.download(file_id["identifier"], verbose=True, dry_run=True, glob_pattern="*mp4")
