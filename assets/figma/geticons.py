import re
import os

simpleicons = []

for root, dirs, files in os.walk("wireframes", topdown = False):
    for name in files:
        if re.match("\S+.png", name):
            simpleicons.append(name)


for i in simpleicons:
    print("<img class=\"wireframe\" src=\"assets/figma/wireframes/%s\"/>" % i)

"""
for i in simpleicons:
    os.system("cp icons/%s simpleicons/" % i)
"""
