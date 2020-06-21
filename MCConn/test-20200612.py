#!/usr/bin/env python 

import socket
import mc
import time
import sys
from chunk import chunk

def main(): 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("rio",25577))

    try:
        result = mc.login(sock, "M!necraft")
        if not result:
            print("Incorrect rcon password")
            return

        sleeptime=.1

        for x in range(-64,60):
                if(x%2) ==0:
                    for y in range(-64,64):
                        mc.killall_mobs(sock)
                        mc.tp(sock,"stephenschaeffer",x*16,100,y*16)
                        t = chunk(sock,x,y,"stephenschaeffer")
                        t.clear_chunk()
                        t.clear_floor()
                        time.sleep(sleeptime)
                        print("stephenschaeffer "+str(x)+" "+str(y))
                else:
                    for y in reversed(range(-64,64)):
                        mc.killall_mobs(sock)
                        mc.tp(sock,"stephenschaeffer",x*16,100,y*16)
                        t = chunk(sock,x,y,"stephenschaeffer")
                        t.clear_chunk()
       	                t.clear_floor()
                        time.sleep(sleeptime)
                        print("stephenschaeffer "+str(x)+" "+str(y))

        time.sleep(sleeptime)

    finally:
        sock.close()

if __name__ == '__main__':
    main()
