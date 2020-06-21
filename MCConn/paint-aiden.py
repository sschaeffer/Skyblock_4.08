#!/usr/bin/env python 

import socket
import mc
from chunk import chunk

def main():
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("yui-v2",25576))

    try:
        result = mc.login(sock, "M!necraft")
        if not result:
            print("Incorrect rcon password")
            return

        for x in range (-59,-57):
		for y in range (2,8):
			i = chunk(sock,x,y,"aidenschaeffer")
			i.biome_detailed_floor()

       # t = chunk(sock,13,-11,"aidenschaeffer")
       # t.biome_detailed_floor()

# draw the spawn point and spawn boundary
        mc.point(sock,6,0,6,mc.spawnborder)
        mc.xline(sock,-161,0,-161,176,mc.spawnborder)
        mc.xline(sock,176,0,-161,176,mc.spawnborder)
        mc.yline(sock,-161,176,0,-161,mc.spawnborder)
        mc.yline(sock,-161,176,0,176,mc.spawnborder)


    finally:
        sock.close()

if __name__ == '__main__':
    main()
