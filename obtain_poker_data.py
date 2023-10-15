import requests
import os
import hashlib

expected_sha256 = "c18333f541b344effb8f446c30f398634d1d045e7b991f3c3399e69af940c4c9"

poker_url = "https://archive.ics.uci.edu/static/public/158/poker+hand.zip"


response = requests.get(poker_url)


if not os.path.exists('data'):
    os.mkdir('data')



with open('data/poker+hand.zip', mode='wb') as f:
    f.write(response.content)


with open('data/poker+hand.zip', mode='rb') as f:
    data = f.read()
    computed_sha256hash = hashlib.sha256(data).hexdigest()



if (computed_sha256hash != expected_sha256):
    print("WARNING: Computed poker hash does not match expected adult hash")
else:
    print("Computed poker matches expected adult hash")

