#!/usr/bin/env python3

import pathlib,subprocess
from subprocess import PIPE

class pycalibre:
    def __init__(self,calibrelib):
        self.clib = pathlib.Path(calibrelib)
    def calibredb(self,op):
        cdb = ["calibredb", "--with-library", str(self.clib)] + op
        print("command:",cdb)
        return subprocess.run(cdb,stdout=PIPE,encoding='utf-8').stdout

