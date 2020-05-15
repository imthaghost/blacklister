from random import randint
from radix import radix

# blacklist
blacklist = radix.Radix()
# generate ip addresses
for i in range(1000000):
    # ip4 ips shoutout to Ben and Omar for this code :)
    ip = "{}.{}.{}.{}".format(randint(0,255), randint(0,255), randint(0,255), randint(0,255))
    node = blacklist.add(ip)
    node.data["ip"] = ip
    node.data["requests"] = 1


