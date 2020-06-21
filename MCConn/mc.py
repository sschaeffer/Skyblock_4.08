import socket
import mcrcon

block = {
    0: "prismarine_brick_slab",     # 0     ocean
    1: "stone_slab",                # 1     plains
    2: "smooth_red_sandstone_slab", # 2     desert 
    3: "cobblestone_slab",          # 3     mountain
    4: "oak_slab",                  # 4     forest
    5: "spruce_slab",               # 5     taiga
    6: "polished_granite_slab",     # 6     swamp
    7: "mossy_cobblestone_slab",    # 7     river 
        # 10  frozen ocean
        # 11  frozen river
        # 12  snowy tundra
        # 13  snowy mountain
    14: "purpur_slab",              # 14    mushroom_fields
        # 15  mushroom_fields_shore
    16: "smooth_sandstone_slab",    # 16    beach
    18: "andesite_slab",            # 18    wooded_hills
    21: "jungle_slab",              # 21    jungle
    24: "dark_prismarine_slab",     # 24    deep_ocean
    25: "granite_slab",             # 25    stone_shore
    27: "birch_slab",               # 27    birch_forest
    29: "dark_oak_slab",            # 29    dark_forest
    35: "acacia_slab",              # 35    savanna
    45: "prismarine_slab",          # 45    lukewarm_ocean
    48: "dark_prismarine_slab",     # 48    deep_lukewarm_ocean
}
unknownbiome="red_nether_brick_slab"
spawnborder="smooth_quartz_slab"
sleeptime=1.5


def command(sock, command, debug=False):
    response = mcrcon.command(sock, command)
    if debug == True:
        print(command)
        print(response)

    return response

def login(sock, password):
    return mcrcon.login(sock, password)

def tp(sock, player, x, z, y, debug=False):
    command(sock,"tp "+player+" "+str(x)+" "+str(z)+" "+str(y),debug)

def checkbiome(sock, player, debug=False):
    response = command(sock,"scoreboard players get "+player+" playerBiome")
    response_split = response.split(" ")
    return int(response_split[2])

def killall_mobs(sock, debug=False):
    command(sock,"kill @e[name=!stephenschaeffer,name=!aidenschaeffer,name=!ryanschaeffer]",debug)

def fill(sock, x1, z1, y1, x2, z2, y2, block, debug=False):
    command(sock, "fill "+str(x1)+" "+str(z1)+" "+str(y1)+" "+\
            str(x2)+" "+str(z2)+" "+str(y2)+" "+block, debug)

def point(sock, x, z, y, block, debug=False):
    fill(sock, x, z, y, x, z, y, block, debug)

def xline(sock, x, z, y1, y2, block, debug=False):
    fill(sock, x, z, y1, x, z, y2, block, debug)

def xwall(sock, x, z1, z2, y1, y2, block, debug=False):
    fill(sock, x, z1, y1, x, z2, y2, block, debug)

def yline(sock, x1, x2, z, y, block, debug=False):
    fill(sock, x1, z, y, x2, z, y, block, debug)

def ywall(sock, x1, x2, z1, z2, y, block, debug=False):
    fill(sock, x1, z1, y, x2, z2, y, block, debug)

def plane(sock, x1, x2, y1, y2, z, block, debug=False):
    fill(sock, x1, z, y1, x2, z, y2, block, debug)

def floor(sock, x1, x2, y1, y2, block, debug=False):
    fill(sock, x1, 0, y1, x2, 0, y2, block, debug)

def container(sock, x1, z1, y1, x2, z2, y2, extblock, intblock, debug=False):
    fill(sock, x1, z1, y1, x2, z2, y2, extblock, debug)
    fill(sock, x1+1, z1+1, y1+1, x2-1, z2-1, y2-1, intblock, debug)

def opencontainer(sock, x1, z1, y1, x2, z2, y2, extblock, intblock, debug=False):
    fill(sock, x1, z1, y1, x2, z2, y2, extblock, debug)
    fill(sock, x1+1, z1+1, y1+1, x2-1, z2, y2-1, intblock, debug)
