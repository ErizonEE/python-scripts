import os
import sys

def ping():
    if (len(sys.argv) < 2):
        print("Necesito un host para pinguear")
        return 1

    host = sys.argv[1]
    os.system('ping ' + host + ' | while read pong; do echo "$(date): $pong"; done')

ping()