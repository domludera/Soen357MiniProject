import re
import os

simpleicons = []

for root, dirs, files in os.walk("icons", topdown = False):
    for name in files:
        if re.match("\w+-outline\.svg", name):
            simpleicons.append(name)


"""
for i in simpleicons:
    print("<li><img class=\"icons\" src=\"assets/simpleicons/%s\"/></li>" % i)

"""
for i in simpleicons:
    os.system("cp icons/%s simpleicons/" % i)
