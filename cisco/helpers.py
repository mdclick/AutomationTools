import time
import sys

def Print(msg, newLine=False):
        sys.stdout.write(msg)
        sys.stdout.flush()
        if(newLine):
                Print('\n')


def Loading(seconds, msg='', newLine=False):
    x = 0
    sys.stdout.write(msg)
    while x<seconds:
        time.sleep(1)
        Print('.')       
        x+=1
    if(newLine):
        Print('\n')

