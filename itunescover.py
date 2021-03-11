from requests import get
import re
from json import loads
r=re.compile("https?:\/\/music.apple.com/[^/]+\/[^/]+\/[^/]+\/([0-9]+)")
def get_album_json(id, cc=us):
    return loads(get("https://itunes.apple.com/lookup?id={}&country={}}&limit=25".format(id, cc)).text)['results'][0]
id=input('id or link: ')
if not isinstance(id, int):
    id=r.findall(id)[0]
cv=get_album_json(id)
cover=cv['artworkUrl100'][:-13]+'100000x100000-999.jpg'
print(cover)