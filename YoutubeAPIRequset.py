import requests
import json

def json_extract(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values

api_key = "APIHERE"
url = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=20&q=SEARCHFORVIDEOHERE&type=video&key=%s" % api_key

# Get Query results
request = requests.get(url)
print(request.text)

# Parse JSON
json_data = json.loads(request.text)
urlsthumb = json_extract(json_data, 'url')
print(urlsthumb[0])
titles = json_extract(json_data, 'title')
print(titles[0])
VidID = json_extract(json_data, 'videoId')
predefined_url = "https://www.youtube.com/watch?v=%s" % VidID[0]
print(predefined_url)
