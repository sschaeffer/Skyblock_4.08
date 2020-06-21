import time
from MCConn import MCConn
from Chunk import Chunk

blockdestroysleeptime=0.4
teleportsleeptime=10.0
teleportskiptime=2.0

def main():

    try:
        mcconn = MCConn()
        mcconn.login()

        mcconn.gamerule_stop()

        skiplist = [[False]*14 for i in range(14)]
        for x in range(9):
             for z in range(13):
                  skiplist[x][z]=True

#        skiplist[3][0]=skiplist[3][1]=skiplist[3][2]=skiplist[3][3]=skiplist[3][4]=True
#        skiplist[0][0]=skiplist[0][1]=skiplist[0][2]=skiplist[0][3]=skiplist[0][4]=skiplist[0][5]=skiplist[0][6]=True
        skiplist[9][8]=skiplist[9][10]=skiplist[9][11]=True


        for xi in range(9,12):
            if xi%2==0:
                for zi in range(0,12):
                    x = (xi-6)*10
                    z = (zi-6)*10

                    mcconn.tp((x*16)+8,100,(z*16)+8)
                    if skiplist[xi][zi] == True:
                        time.sleep(teleportskiptime)
                    else:
                        time.sleep(teleportsleeptime)
                    mcconn.tp((x*16)+8,100,(z*16)+8)

                    if skiplist[xi][zi] == True:
                        print("skipping",'\t',xi,zi,x,z,(x*16)+8,(z*16)+8)
                    else:
                        print("first pass",'\t',xi,zi,x,z,(x*16)+8,(z*16)+8)
                        for chx in range(11):
                            for chz in range(11):
                                t = Chunk(mcconn,(x-5)+chx,(z-5)+chz)
                                print("clear chunk",(x-5)+chx,(z-5)+chz)
                                t.clear_chunk()
                                t.clear_floor()
                                time.sleep(blockdestroysleeptime)

                        print("second pass",'\t',xi,zi,x,z,(x*16)+8,(z*16)+8)
                        for chx in range(11):
                            for chz in range(11):
                                t = Chunk(mcconn,(x-5)+chx,(z-5)+chz)
                                print("clear chunk",(x-5)+chx,(z-5)+chz)
                                t.clear_chunk()
                                t.clear_floor()
                                time.sleep(blockdestroysleeptime)

                        print("third pass",'\t',xi,zi,x,z,(x*16)+8,(z*16)+8)
                        for chx in range(11):
                            for chz in range(11):
                                t = Chunk(mcconn,(x-5)+chx,(z-5)+chz)
                                print("clear chunk",(x-5)+chx,(z-5)+chz)
                                t.clear_chunk()
                                t.clear_floor()
                                time.sleep(blockdestroysleeptime)

            else:
                for zi in reversed(range(1,12)):
                    x = (xi-6)*10
                    z = (zi-6)*10

                    mcconn.tp((x*16)+8,100,(z*16)+8)
                    if skiplist[xi][zi] == True:
                        time.sleep(teleportskiptime)
                    else:
                        time.sleep(teleportsleeptime)
                    mcconn.tp((x*16)+8,100,(z*16)+8)


                    if skiplist[xi][zi] == True:
                        print("skipping",'\t',xi,zi,x,z,(x*16)+8,(z*16)+8)
                    else:
                        print("first pass",'\t',xi,zi,x,z,(x*16)+8,(z*16)+8)
                        for chx in range(11):
                            for chz in range(11):
                                t = Chunk(mcconn,(x-5)+chx,(z-5)+chz)
                                print("clear chunk",(x-5)+chx,(z-5)+chz)
                                t.clear_chunk()
                                t.clear_floor()
                                time.sleep(blockdestroysleeptime)

                        print("second pass",'\t',xi,zi,x,z,(x*16)+8,(z*16)+8)
                        for chx in range(11):
                            for chz in range(11):
                                t = Chunk(mcconn,(x-5)+chx,(z-5)+chz)
                                print("clear chunk",(x-5)+chx,(z-5)+chz)
                                t.clear_chunk()
                                t.clear_floor()
                                time.sleep(blockdestroysleeptime)

                        print("third pass",'\t',xi,zi,x,z,(x*16)+8,(z*16)+8)
                        for chx in range(11):
                            for chz in range(11):
                                t = Chunk(mcconn,(x-5)+chx,(z-5)+chz)
                                print("clear chunk",(x-5)+chx,(z-5)+chz)
                                t.clear_chunk()
                                t.clear_floor()
                                time.sleep(blockdestroysleeptime)


    finally:
        mcconn.close()

if __name__ == '__main__':
    main()
