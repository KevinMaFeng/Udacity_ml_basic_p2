#!/usr/bin/env python
# coding=utf-8

import media
import fresh_tomatoes
import webbrowser
import urllib




def is_invalid_url(url):
    """
    check if a url is valid or not.
    input:url link
    output:True if url is invalid.
           False if url is valid.
    """
    try:
        handler = urllib.urlopen(url)
    except Exception:
        print url + "=urlopen error"
        return True
    
    handler.close()
    return False


def urls_are_good(movies):
    """
    ensure both image and movie links are good.
    input:Movie class list
    output:True if check passed.
           False if check failed.
    """
    for mov in movies:
        if is_invalid_url(mov.get_poster_image_url()):
            return False
        if is_invalid_url(mov.get_trailer_url()):
            return False
    return True

# initialize each instance created.
starwar = media.Movie(r"Star War",
                      r"Star Wars is an American epic space opera media franchise.",
                      r"https://thumbnail0.baidupcs.com/thumbnail/1415c7d6f56c1f80e73a8caaa17ad67c?fid=1380141309-250528-721312214966012&time=1515232800&rt=sh&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-%2BqjmDBtfbxocZPHzOc6SEjN2PWw%3D&expires=8h&chkv=0&chkbd=0&chkpc=&dp-logid=134124572857087541&dp-callid=0&size=c710_u400&quality=100&vuk=-&ft=video",
                      r"http://v.youku.com/v_show/id_XMzA3NTY2OTMwNA==.html?spm=a2h0j.8191423.ykPlayer.5~5~5!6~5~5!4~5~5!2~A")

avadar2 = media.Movie(r"Avadar2",
                      r"It is an upcoming American epic science fiction film directed, produced, and co-written by James Cameron.",
                      r"https://thumbnail0.baidupcs.com/thumbnail/11fc06f405e76025af961e8c93266cb5?fid=1380141309-250528-873401244413457&time=1515236400&rt=sh&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-CzHTXgZmY9hUVRxeyUsAqqfiEgM%3D&expires=8h&chkv=0&chkbd=0&chkpc=&dp-logid=134335179325405842&dp-callid=0&size=c710_u400&quality=100&vuk=-&ft=video",
                      r"http://v.youku.com/v_show/id_XMjk3NTM3NTczNg==.html?spm=a2h0k.8191407.0.0&from=s1.8-1-1.2")

dragon_fighter = media.Movie(r"Dragon Ball FighterZ",
                      r"The Nintendo Entertainment System video game developed by Natsume, see Dragon Fighter (video game).",
                      r"https://thumbnail0.baidupcs.com/thumbnail/8e85b2e88a483b5a3085f9ca11ad24ff?fid=1380141309-250528-70316488466119&time=1515236400&rt=sh&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-zOFnYzCsA1IbIprZeVEuUtuRwwI%3D&expires=8h&chkv=0&chkbd=0&chkpc=&dp-logid=134561521436059403&dp-callid=0&size=c710_u400&quality=100&vuk=-&ft=video",
                      r"http://v.youku.com/v_show/id_XMzA4OTg5NjY2MA==.html?spm=a2h0k.8191407.0.0&from=s1.8-1-1.2")

# construct movies list
movies = [starwar, avadar2, dragon_fighter]

# need check before pass the URLs to the static HTML page.
if not urls_are_good(movies):
    print "Urls check failed."
else:
    try:
        fresh_tomatoes.open_movies_page(movies)
    except webbrowser.Error, e:
        print e
