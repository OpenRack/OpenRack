import sys


platform = sys.platform
print(platform)

if "linux" in platform:
    print("nice")
if "win" in platform:
    print("ugh")