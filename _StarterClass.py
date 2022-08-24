import sys

eggs = []
for egg in eggs:
    sys.path.append(egg)
sys.path.insert(0, "some/dir/of/libs")

import os
import json
import time
import pprint
import requests

from datetime import datetime

class STARTER_CLASS_NAME_HERE:

    def __init__(self):
        self.cert = "path\\to\\cert"
        self.api_a = "http://httpbin.org"

    def example(self):
        u = self.api_a + "/ip"
        r = requests.get(u)
        print(r.status_code)
        print(r.text)

def usage():
    print()
    print("\tusage: %s <mode>\r\n" % os.path.basename(sys.argv[0]))
    print("\t<mode>: 1 - something")
    print("\t        2 - something")
    print()

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        usage()
        quit()

    p = STARTER_CLASS_NAME_HERE()
    m = int(sys.argv[1])
    if (m == 1):
        p.example()
    elif (m == 2):
        p.example()
    else:
        print("[!] Unsupported mode")
        usage()
