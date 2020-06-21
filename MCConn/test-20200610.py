import sys
import socket
import mc
import time
from chunk import chunk

def main():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("iori",25577))

    try:
        result = mc.login(sock, "M!necraft")
        if not result:
            print("Incorrect rcon password")
            return

        teleportsleeptime = 10.0
        blockkillsleeptime = 0.1
        x=55
        z=55
        mc.tp(sock,"stephenschaeffer",(x*16)+8,100,(z*16)+8)
        mc.killall_mobs(sock)
        for chx in range(11):
            for chz in range(11):
                t = chunk(sock,(x-5)+chx,(z-5)+chz)
                t.clear_chunk()
                t.clear_floor()
                time.sleep(blockkillsleeptime)
        mc.killall_mobs(sock)
        for chx in range(11):
            for chz in range(11):
                t = chunk(sock,(x-5)+chx,(z-5)+chz)
                t.clear_chunk()
                t.clear_floor()
                time.sleep(blockkillsleeptime)
        mc.killall_mobs(sock)

    finally:
        sock.close()

if __name__ == '__main__':
    main()
