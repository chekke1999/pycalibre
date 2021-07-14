#!/usr/bin/env python3
import re
from pycalibre import pycalibre
pyc = pycalibre('/home/shoji/Documents/calibre/Calibreライブラリ/')
data = pyc.calibredb(["list", "--for-machine", "-f", "authors,author_sort", "-s", 'author:"サークル："'])

for i in eval(data):
    if "&" in i["authors"]:
        #ここに著者名が複数ある場合の処理を記述
        authors = re.sub("(サークル:.*?&)","",i["authors"])
        author_sort = re.sub("(サークル:.*?&)","",i["author_sort"])
        dj_circle = re.search("(?<=サークル:).*?(?=&)",i["authors"]).group()
        print(i["id"],"複数検出")
    else:
        #ここに著者名がサークルのみの場合の処理を記述
        authors = i["authors"].replace("サークル:","")
        author_sort = i["author_sort"].replace("サークル:","")
        dj_circle = i["authors"].replace("サークル:","")
        print(i["id"],"単独検出")

    setmeta_str = pyc.calibredb(["set_metadata", "-f", f'authors:{authors}', "-f", f'author_sort:{author_sort}',"-f", f'#dj_circle:{dj_circle}',str(i["id"])])
    print(setmeta_str)