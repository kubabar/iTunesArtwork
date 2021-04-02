# -*- coding: utf-8 -*-
from requests import get
from json import loads
from PIL import Image
import numpy as np

def get_ansi_color_code(r, g, b):
    if r == g and g == b:
        if r < 8:
            return 16
        if r > 248:
            return 231
        return round(((r - 8) / 247) * 24) + 232
    return 16 + (36 * round(r / 255 * 5)) + (6 * round(g / 255 * 5)) + round(b / 255 * 5)

def get_color(r, g, b):
    return "\x1b[48;5;{}m \x1b[0m".format(int(get_ansi_color_code(r,g,b)))

def show_image(url, h, text):
    img = Image.open(get(url, stream=True).raw)
    w=h*2
    img = img.resize((w,h), Image.ANTIALIAS)
    img_arr = np.asarray(img)
    h,w,c = img_arr.shape
    med=int(h/2)+1
    for x in range(med):
        for y in range(w):
            pix = img_arr[x][y]
            print(get_color(pix[0], pix[1], pix[2]), sep='', end='')
        if x!=med-1:
            print()
        else:
            print(' '+text)
    for x in range(med, h):
        for y in range(w):
            pix = img_arr[x][y]
            print(get_color(pix[0], pix[1], pix[2]), sep='', end='')
        print()
        
def search_cover(term):
    return loads(get("https://itunes.apple.com/search", params={'term': term, 'country': 'pl', 'limit': '10'}).text)['results']

def select_search(term, size=7):
    list=search_cover(term)
    for i in range(len(list)):
        show_image(list[i]['artworkUrl60'], int(size), '[{}] '.format(str(i+1))+list[i]['trackName'])
        print()
    w=int(input('wybierz numerek: '))
    return list[w-1]

def get_url(res):
    return res['artworkUrl100'][:-13]+'100000x100000-999.jpg'

if __name__ == '__main__':
    while True:
        print(get_url(select_search(input('kogo co? '))))