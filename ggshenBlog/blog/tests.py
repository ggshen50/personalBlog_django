import re

path = 'video/BothDance.mp4'
name = re.findall('.*/(\w+.mp4)', path)[0]
title = re.findall('.*/(\w+).mp4', path)[0]
path = re.findall('(video/.*)', path)[0]
print(name, title, path)