import urllib
geocode_url = "https://geodata.gov.gr/en/dataset/4595f6f1-099d-465a-af07-e963992983e9/resource/4814ddea-79ab-4bd4-b22d-6d0e20771781/download/datk.zip"
url = '/api/action/datastore_search?limit=5&q=title:jones'
fileobj = urllib.urlopen(geocode_url)
#print fileobj.read()