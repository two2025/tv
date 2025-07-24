import os
import re
import time
import datetime
import threading
from queue import Queue
import requests
import eventlet
eventlet.monkey_patch()


with open("itvlist.txt", 'w', encoding='utf-8') as file:
    file.write('央视频道,#genre#\n')
with open("itvlist.m3u", 'w', encoding='utf-8') as file:
    file.write('央视频道,#genre#\n')
