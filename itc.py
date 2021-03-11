# -*- coding: utf-8 -*-
from requests import get
import re
from json import loads
from os import system
from urllib import parse
from os import system
sc=re.compile('<ul>\n.+?<li><h2><a href="(\/[^/]+\/[^"]+)')
scc=re.compile('<\/header>\n.+?<p>\n.+?<img src="([^"]+)')
def get_album_json(id, cc='us'):
    return loads(get("https://itunes.apple.com/lookup?id={}&country={}}&limit=1".format(id, cc)).text)['results'][0]
def get_cover(title, artist='', sv='it'):
    searchfor=title+' '+artist
    if sv=='it':
        return loads(get("https://itunes.apple.com/search", params={'term': searchfor, 'country': 'us', 'limit': '1'}).text)['results'][0]['artworkUrl100'][:-13]+'100000x100000-999.jpg'
    if sv=='sc':
        res=get('https://soundcloud.com/search/sounds?q='+parse.quote(searchfor.encode('utf8')))
        res.encoding='utf8'
        song=sc.findall(res.text)[0]
        songpage=get('https://soundcloud.com/'+song).text
        url=scc.findall(songpage)[0][:-12]+'original.jpg'
        return url
url=(get_cover(input('title: '), input('artist: '), sv='it'))
print(url)
#system('ffplay -hide_banner "{}"'.format(url))
pathToFile='bubabub/cover.jpg'
system('curl --create-dirs "{}" -o "{}"'.format(cover, pathToFile))