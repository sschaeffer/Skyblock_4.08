import time
from MCConn import MCConn

class Chunk:

    def __init__(self,mcconn: MCConn,cx,cy):
        self.mcconn = mcconn
        self.cx = cx
        self.cy = cy
        self.x = self.cx*16
        self.y = self.cy*16
        self.biome = -1

#    def set_biome(self, biome):
#        self.biome = biome
#
#    def biome_autodetect(self):
#        self.mcconn.tp(self.x+7,100,self.y+7)
#        time.sleep(MCConn.BIOMESLEEPTIME)
#        self.biome = self.mcconn.checkbiome()
#
#    def biome_floor(self):
#
#        if(self.biome==-1): 
#            self.biome_autodetect()
#
#        if self.biome in mc.block:
#                biomeblock = mc.block[self.biome]
#            else:
#                biomeblock = mc.unknownbiome
#
#            mc.floor(self.sock,self.x,self.x+15,self.y,self.y+15,biomeblock)
#
#    def biome_detailed_floor(self):
#
#        if(self.player==""): 
#            print("Please set player")
#        else:
#            for x in range(0,16):
#                for y in range(0,16):
#                    mc.tp(self.sock,self.player,self.x+x,100,self.y+y)
#                    time.sleep(mc.sleeptime)
#                    biome = mc.checkbiome(self.sock,self.player)
#                    if biome in mc.block:
#                        biomeblock = mc.block[biome]
#                    else:
#                        biomeblock = mc.unknownbiome
#
#                    print(biomeblock +"("+str(biome)+")\t\t"+str(self.x+x)+","+\
#                            str(self.y+y)+"\t\tc:"+str(self.cx)+","+str(self.cy)+" r:"+\
#                            str(x)+","+str(y))
#                    mc.point(self.sock,self.x+x,0,self.y+y,biomeblock)
#
    def clear_chunk(self):
        self.mcconn.fill(self.x,1,self.y,self.x+15,127,self.y+15,"air")
        self.mcconn.fill(self.x,128,self.y,self.x+15,255,self.y+15,"air")

    def clear_floor(self):
        self.mcconn.floor(self.x,self.x+15,self.y,self.y+15,"air")

#    def mob_spawner(self,height):
#        mc.container(self.sock,self.x,height,self.y,self.x+15,height+3,self.y+15,"cobblestone","air")
#
#    def mob_grass_openspawner(self,height):
#        mc.opencontainer(self.sock,self.x,height,self.y,self.x+15,height+3,self.y+15,"grass_block","air")
#
#    def mob_ice_openspawner(self,height):
#        mc.opencontainer(self.sock,self.x,height,self.y,self.x+15,height+3,self.y+15,"ice","air")
#
#    def mob_icewater_spawner(self,height):
#        mc.container(self.sock,self.x,height,self.y,self.x+15,height+3,self.y+15,"ice","water")
#
#    def mob_icewater_fishspawner(self,height):
#        mc.container(self.sock,self.x,height,self.y,self.x+15,height+30,self.y+15,"ice","water")
#
#
#