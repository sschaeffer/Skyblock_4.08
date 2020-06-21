#!/usr/bin/env python 

import socket
#import mc
import time
import sys
#from chunk import chunk
from MCConn import MCConn
from Chunk import Chunk

def main(): 
    mcconn = MCConn()
    mcconn.login()
    mcconn.gamerule_stop()

    try:
#        mcconn.clear_pushbroom(60,-65,130,stepback=1,repeat=1,teleportpresleep=120.0,teleportpostsleep=120.0)
#
        mcconn.clear_pushbroom(59,-64,128)
        mcconn.clear_pushbroom(50,64,-128)
        mcconn.clear_pushbroom(40,-64,128)
        mcconn.clear_pushbroom(30,64,-128)
        mcconn.clear_pushbroom(20,-64,128)
        mcconn.clear_pushbroom(10,64,-128)
        mcconn.clear_pushbroom(0,-64,128)
        mcconn.clear_pushbroom(-10,64,-128)
        mcconn.clear_pushbroom(-20,-64,128)
        mcconn.clear_pushbroom(-30,64,-128)
        mcconn.clear_pushbroom(-40,-64,128)
        mcconn.clear_pushbroom(-50,64,-128)
        mcconn.clear_pushbroom(-59,-64,128)
#
##        for x in range(xstart,xend):
##                if(x%2) ==0:
##                    for z in range(zstart,zend):
##                        mcconn.tp(x*16,100,z*16)
##                        t=Chunk(mcconn,x,z)
##                        t.clear_chunk()
##                        t.clear_floor()
##                        time.sleep(sleeptime)
##                        print(x,z)
##                else:
##                    for z in reversed(range(zstart,zend)):
##                        mcconn.tp(x*16,100,z*16)
##                        t=Chunk(mcconn,x,z)
##                        t.clear_chunk()
##                        t.clear_floor()
##                        time.sleep(sleeptime)
##                        print(x,z)
##
##                if((x-1)%2) ==0:
##                    for z in range(zstart,zend):
##                        mcconn.tp((x-1)*16,100,z*16)
##                        t=Chunk(mcconn,(x-1),z)
##                        t.clear_chunk()
##                        t.clear_floor()
##                        time.sleep(sleeptime)
##                        print((x-1),z)
##                else:
##                    for z in reversed(range(zstart,zend)):
##                        mcconn.tp((x-1)*16,100,z*16)
##                        t=Chunk(mcconn,(x-1),z)
##                        t.clear_chunk()
##                        t.clear_floor()
##                        time.sleep(sleeptime)
##                        print((x-1),z)
##
##                if(x%2) ==0:
##                    for z in range(zstart,zend):
##                        mcconn.tp(x*16,100,z*16)
##                        t=Chunk(mcconn,x,z)
##                        t.clear_chunk()
##                        t.clear_floor()
##                        time.sleep(sleeptime)
##                        print(x,z)
##                else:
##                    for z in reversed(range(zstart,zend)):
##                        mcconn.tp(x*16,100,z*16)
##                        t=Chunk(mcconn,x,z)
##                        t.clear_chunk()
##                        t.clear_floor()
##                        time.sleep(sleeptime)
##                        print(x,z)
##
##                if((x-1)%2) ==0:
##                    for z in range(zstart,zend):
##                        mcconn.tp((x-1)*16,100,z*16)
##                        t=Chunk(mcconn,(x-1),z)
##                        t.clear_chunk()
##                        t.clear_floor()
##                        time.sleep(sleeptime)
##                        print((x-1),z)
##                else:
##                    for z in reversed(range(zstart,zend)):
##                        mcconn.tp((x-1)*16,100,z*16)
##                        t=Chunk(mcconn,(x-1),z)
##                        t.clear_chunk()
##                        t.clear_floor()
##                        time.sleep(sleeptime)
##                        print((x-1),z)
##
##                if(x%2) ==0:
##                    for z in range(zstart,zend):
##                        mcconn.tp((x)*16,100,z*16)
##                        t=Chunk(mcconn,(x),z)
##                        t.clear_chunk()
##                        t.clear_floor()
##                        time.sleep(sleeptime)
##                        print(x,z)
##                else:
##                    for z in reversed(range(zstart,zend)):
##                        mcconn.tp((x)*16,100,z*16)
##                        t=Chunk(mcconn,(x),z)
##                        t.clear_chunk()
##                        t.clear_floor()
##                        time.sleep(sleeptime)
##                        print(x,z)
##

    finally:
        mcconn.close()

if __name__ == '__main__':
    main()
