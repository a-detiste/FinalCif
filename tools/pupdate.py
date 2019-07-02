# /usr/bin/env python
# -*- encoding: utf-8 -*-
# möp
# This script updates the platon.exe in the c:\pwt directory.

import datetime
import subprocess
import tempfile
import urllib
import zipfile
from html.parser import HTMLParser
from pathlib import Path
from urllib import request

changes_url = 'http://www.platonsoft.nl/spek/xraysoft/update_history_platon.html'
platon_url = 'http://www.platonsoft.nl/spek/xraysoft/mswindows/platon/platon.zip'


def get_changes():
    # fetch the changes of platon and store it in one string (text)
    with request.urlopen(changes_url) as f:
        text = [x.decode('utf-8') for x in f.readlines()]
    text = "".join(text[:25])

    # strips down the html to plain text
    class MLStripper(HTMLParser):
        def __init__(self):
            super().__init__()
            self.reset()
            self.fed = []

        def handle_data(self, d):
            self.fed.append(d.rstrip('\n'))

        def get_data(self):
            return ''.join(self.fed)

    def strip_tags(htmlp):
        s = MLStripper()
        s.feed(htmlp)
        return s.get_data()

    today = datetime.date.today()
    return "\nToday is: {}".format(str(today.strftime('%b %d, %Y\n')), strip_tags(text))


def get_platon() -> tempfile.TemporaryFile:
    # now preceed with platon update
    req = request.Request(platon_url)
    with urllib.request.urlopen(req) as response:
        data = response.read()
    # create a temporary file and download platon.zip to it.
    localFile = tempfile.TemporaryFile(mode='w+b')
    localFile.write(data)
    # open the zip file
    zf = zipfile.ZipFile(localFile, 'r')
    # if not already present - create the platon directory:
    tmphandle, platon_exe = tempfile.mkstemp(prefix='platon', suffix='.exe')
    # extract the files to the platon directory
    with open(tmphandle, 'w+b') as f:
        f.write(zf.read('platon.exe'))
    localFile.close()
    return platon_exe


if __name__ == "__main__":
    pexe = get_platon()
    print(pexe)
    plat = subprocess.Popen([pexe])
    Path(pexe).unlink()