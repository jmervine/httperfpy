from sys import path
path.append("..")

import unittest
import httperfpy 

import os
import string

global httperf_path
httperf_path = string.strip(os.popen("which httperf").read())

if httperf_path == '':
    raise Exception("httperf must be install")

