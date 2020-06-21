"""
Generates a image of the top view of a chunk
Needs a textures folder with a block folder inside
"""
import sys
import os
import _path
import anvil
from nbt import nbt
from PIL import Image,ImageDraw,ImageFont

global_biome_totals = [0]*256

BIOMES = {
    0 : "Ocean",  
    1 : "Plains",   
    2 : "Desert",   
    3 : "Mountains",
    4 : "Forest",
    5 : "Taiga",
    6 : "Swamp",
    7 : "River",
    8 : "Nether",
    9 : "Sky",
    10: "Frozen Ocean",
    11: "Frozen River",
    12: "Ice Plains",
    13: "Ice Mountains",
    14: "Mushroom Island",
    15: "Mushroom Shore",
    16: "Beach",
    17: "Desert Hills",
    18: "Forest Hills",
    19: "Taiga Hills",
    20: "Mountains Edge",
    21: "Jungle",
    22: "Jungle Hills",
    23: "Jungle Edge",
    24: "Deep Ocean",
    25: "Stone Beach",
    26: "Cold Beach",
    27: "Birch Forest",
    28: "Birch Forest Hills",
    29: "Roofed Forest",
    30: "Cold Taiga",
    31: "Cold Taiga Hills",
    32: "Mega Taiga",
    33: "Mega Taiga Hills",
    34: "Extreme Hills",
    35: "Savanna",
    36: "Savanna Plateau",
    37: "Mesa",
    38: "Mesa Plateau F",
    39: "Mesa Plateau",
    40: "Small End Islands",
    41: "End Midlands",
    42: "End Highlands",
    43: "End Barrens",
    44: "Warm Ocean",
    45: "Lukewarm Ocean",
    46: "Cold Ocean",
    47: "Deep Warm Ocean",
    48: "Deep Lukewarm Ocean",
    49: "Deep Cold Ocean",
    50: "Deap Frozen Ocean",
    127: "The Void",
    129: "Sunflower Plains",
    130: "Desert M",
    131: "Extreme Hills M",
    132: "Flower Forest",
    133: "Taiga M",
    134: "Swampland M",
    140: "Ice Plains Spikes",
    149: "Jungle M",
    151: "Jungle Edge M",
    155: "Birch Forest M",
    156: "Birch Forest Hills M",
    157: "Roofed Forest M",
    158: "Cold Taiga M",
    160: "Mega Spruce Taiga",
    161: "Redwood Taiga Hills M",
    162: "Extreme Hills+ M",
    163: "Savanna M",
    164: "Savanna Plateau M",
    165: "Mesa(Bryce)",
    166: "Mesa Plateau F M",
    167: "Mesa Plateau M",
    168: "Bamboo Jungle",
    169: "Bamboo Jungle Hills",
    170: "Soul Sand Valley",
    171: "Crimson Forrest",
    172: "Warped Forest",
    173: "Basalt Deltas",
    255: "Not yet calculated",
}

BIOMECOLORS = {
    0 : "#283593", #"Ocean",
    1 : "#66bb6a", #"Plains",
    2 : "#FF9900", #"Desert",
    3 : "#7986CB", #"Mountains",
    4 : "#1b5e20", #"Forest",
    5 : "#CC33CC", #"Taiga",
    6 : "#CC33CC", #"Swamp",
    7 : "#1A237E", #"River",
    8 : "#CC33CC", #"Nether",
    9 : "#CC33CC", #"Sky",
    10: "#CC33CC", #"Frozen Ocean",
    11: "#CC33CC", #"Frozen River",
    12: "#CC33CC", #"Ice Plains",
    13: "#CC33CC", #"Ice Mountains",
    14: "#CC33CC", #"Mushroom Island",
    15: "#CC33CC", #"Mushroom Shore",
    16: "#CC33CC", #"Beach",
    17: "#CC33CC", #"Desert Hills",
    18:  "#1b7720", #"Forest Hills",
    19:  "#CC33CC", #"Taiga Hills",
    20:  "#CC33CC", #"Mountains Edge",
    21:  "#CC33CC", #"Jungle",
    22:  "#CC33CC", #"Jungle Hills",
    23:  "#CC33CC", #"Jungle Edge",
    24:  "#CC33CC", #"Deep Ocean",
    25:  "#CC33CC", #"Stone Beach",
    26:  "#CC33CC", #"Cold Beach",
    27:  "#CC33CC", #"Birch Forest",
    28:  "#CC33CC", #"Birch Forest Hills",
    29:  "#666633", #"Roofed Forest",
    30:  "#CC33CC", #"Cold Taiga",
    31:  "#CC33CC", #"Cold Taiga Hills",
    32:  "#CC33CC", #"Mega Taiga",
    33:  "#CC33CC", #"Mega Taiga Hills",
    34:  "#80cbc4", #"Extreme Hills",
    35:  "#CC33CC", #"Savanna",
    36:  "#CC33CC", #"Savanna Plateau",
    37:  "#FF6600", #"Mesa",
    38:  "#FF3300", #"Mesa Plateau F",
    39:  "#FF0000", #"Mesa Plateau",
    40:  "#CC33CC", #"Small End Islands",
    41:  "#CC33CC", #"End Midlands",
    42:  "#CC33CC", #"End Highlands",
    43:  "#CC33CC", #"End Barrens",
    44:  "#CC33CC", #"Warm Ocean",
    45:  "#CC33CC", #"Lukewarm Ocean",
    46:  "#CC33CC", #"Cold Ocean",
    47:  "#CC33CC", #"Deep Warm Ocean",
    48:  "#CC33CC", #"Deep Lukewarm Ocean",
    49:  "#CC33CC", #"Deep Cold Ocean",
    50:  "#CC33CC", #"Deap Frozen Ocean",
    127: "#CC33CC", # "The Void",
    129: "#CC33CC", # "Sunflower Plains",
    130: "#CC33CC", # "Desert M",
    131: "#CC33CC", # "Extreme Hills M",
    132: "#673AB7", # "Flower Forest",
    133: "#CC33CC", # "Taiga M",
    134: "#CC33CC", # "Swampland M",
    140: "#CC33CC", # "Ice Plains Spikes",
    149: "#CC33CC", # "Jungle M",
    151: "#CC33CC", # "Jungle Edge M",
    155: "#CC33CC", # "Birch Forest M",
    156: "#CC33CC", # "Birch Forest Hills M",
    157: "#CC33CC", # "Roofed Forest M",
    158: "#CC33CC", # "Cold Taiga M",
    160: "#CC33CC", # "Mega Spruce Taiga",
    161: "#CC33CC", # "Redwood Taiga Hills M",
    162: "#CC33CC", # "Extreme Hills+ M",
    163: "#CC33CC", # "Savanna M",
    164: "#CC33CC", # "Savanna Plateau M",
    165: "#CC33CC", # "Mesa(Bryce)",
    166: "#CC33CC", # "Mesa Plateau F M",
    167: "#CC33CC", # "Mesa Plateau M",
    168: "#CC33CC", # "Bamboo Jungle",
    169: "#CC33CC", # "Bamboo Jungle Hills",
    170: "#CC33CC", # "Soul Sand Valley",
    171: "#CC33CC", # "Crimson Forrest",
    172: "#CC33CC", # "Warped Forest",
    173: "#CC33CC", # "Basalt Deltas"
    255: "#212121", # "Not yet calculated",
}


def build_biomes_grid(nb):
    biomes = [[[None for x in range(4)] for y in range(64)] for z in range(4)]
    i=0
    print(nb['DataVersion'])
    for y in range(64):
        for z in range(4):
            for x in range(4):
                biomes[x][y][z] = nb['Level']['Biomes'][i]
                i+=1

    return biomes

def print_biomes(biomes,height):
    for y in range(height):
        for z in range(4):
            for x in range(4):
                print(biomes[x][y][z],end=' ')
            print('')
        if y != height-1:
            print(".......")


def create_biome_image(region,chx1,chx2,chz1,chz2,savfilename):

    xsize=chx2-chx1
    zsize=chz2-chz1
    img = Image.new('RGB', (xsize*4*16,zsize*4*16))
    imgdraw = ImageDraw.Draw(img)

    for z in range(zsize):
        for x in range(xsize):
            nb = region.chunk_data(chx1+x,chz1+z)
            if(nb):
                biomes = build_biomes_grid(nb)
                fill_biome_image(imgdraw,biomes,x*4*16,z*4*16)
            else:
                imgdraw.rectangle((x*4*16,z*4*16,(x*4*16)+64,(z*4*16)+64),BIOMECOLORS[255])
#            print()
#    img.show()
    img.save(savfilename,format="png")


def fill_biome_image(imgdraw,biomes,imgx,imgz):

    local_biome_totals = [0]*256
    for z in range(4):
        for x in range(4):
            biome=biomes[x][0][z]
            local_biome_totals[biome] += 1
            global_biome_totals[biome] += 1
            xpos = imgx+(x*16)
            zpos = imgz+(z*16)
            imgdraw.rectangle((xpos,zpos,xpos+16,zpos+16),fill=BIOMECOLORS[biome])
#            print("xpos:",xpos,"zpos:",zpos,"xpos:",xpos+16,"zpos:",zpos+16,"biome:",biome,BIOMES[biome])
    hl = 255
    hlv = 0
    for l in range(256):
        if local_biome_totals[l] > hlv:
            hl = l
            hlv = local_biome_totals[l]
    imgdraw.text((imgx+16,imgz+16),str(hl),font=ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf"),fill=BIOMECOLORS[255])

def replace_biome(regionfile, chx, chz):

    if isinstance(regionfile, str):
        region = anvil.Region.from_file(regionfile)
    nb = region.chunk_data(chx,chy)

    biomesarray = nb['Level']['Biomes']
    for i in range(len(biomesarray)):
        if biomesarray[i] == 4:
            biomesarray[i]=39
    nb['Level']['Biomes'] = biomesarray

    region.replace_chunk_data(chx,chy,nb)
    region.to_file("/home/integ/.minecraft/saves/1_16pre3_test/region/r.0.-1.test.mca")

def print_biome_for_chunk(region, chx, chz):
    nb = region.chunk_data(chx,chz)
    if nb:
        biomes = build_biomes_grid(nb)
        print_biomes(biomes,1)
    else:
        print("Chunk is not in this regionfile")

def print_chunk_data_tree(region, chx, chz):
    nb = region.chunk_data(chx,chz)
    if nb:
        print(nb.pretty_tree())
    else:
        print("Chunk is not in this regionfile")

def main(region_file):

    try:
        #if isinstance(region_file, str):
#            region = anvil.Region.from_file(region_file)

# inner ring
        region = anvil.Region.from_file(region_file)
        print_chunk_data_tree(region,10,0)
        print_chunk_data_tree(region,11,0)
        create_biome_image(region,0,32,0,32,"/tmp/r.0.0.png")

#        region = anvil.Region.from_file("/home/integ/.minecraft/saves/1_16pre3_test/region/r.0.-1.mca")
#        create_biome_image(region,0,32,-32,0)
#        region = anvil.Region.from_file("/home/integ/.minecraft/saves/1_16pre3_test/region/r.-1.0.mca")
#        create_biome_image(region,-32,0,0,32)
#        region = anvil.Region.from_file("/home/integ/.minecraft/saves/1_16pre3_test/region/r.-1.-1.mca")
#        create_biome_image(region,-32,0,-32,0)

# outer ring
#        print("parsing r.1.-2.mca")
#        region = anvil.Region.from_file("/home/integ/.minecraft/saves/1_16pre3_test/region/r.1.-2.mca")
#        create_biome_image(region,-64,-32,-64,-32)
#        print("parsing r.1.-1.mca")
#        region = anvil.Region.from_file("/home/integ/.minecraft/saves/1_16pre3_test/region/r.1.-1.mca")
#        create_biome_image(region,-64,-32,-32,0)
#        print("parsing r.1.0.mca")
#        region = anvil.Region.from_file("/home/integ/.minecraft/saves/1_16pre3_test/region/r.1.0.mca")
#        create_biome_image(region,-64,-32,0,32)
#        print("parsing r.1.1.mca")
#        region = anvil.Region.from_file("/home/integ/.minecraft/saves/1_16pre3_test/region/r.1.1.mca")
#        create_biome_image(region,-64,-32,32,64)
#
#        print("parsing r.0.-2.mca")
#        region = anvil.Region.from_file("/home/integ/.minecraft/saves/1_16pre3_test/region/r.0.-2.mca")
#        create_biome_image(region,0,32,-64,-32)
#        print("parsing r.0.-1.mca")
#        region = anvil.Region.from_file("/home/integ/.minecraft/saves/1_16pre3_test/region/r.0.-1.mca")
#        create_biome_image(region,0,32,-32,0)
#        print("parsing r.0.0.mca")
#        region = anvil.Region.from_file("/home/integ/.minecraft/saves/1_16pre3_test/region/r.0.0.mca")
#        create_biome_image(region,0,32,0,32)
#        print("parsing r.0.1.mca")
#        region = anvil.Region.from_file("/home/integ/.minecraft/saves/1_16pre3_test/region/r.0.1.mca")
#        create_biome_image(region,0,32,32,64)
#
#        print("parsing r.-1.-2.mca")
#        region = anvil.Region.from_file("/home/integ/.minecraft/saves/1_16pre3_test/region/r.-1.-2.mca")
#        create_biome_image(region,-32,0,-64,-32)
#        print("parsing r.-1.-1.mca")
#        region = anvil.Region.from_file("/home/integ/.minecraft/saves/1_16pre3_test/region/r.-1.-1.mca")
#        create_biome_image(region,-32,0,-32,0)
#        print("parsing r.-1.0.mca")
#        region = anvil.Region.from_file("/home/integ/.minecraft/saves/1_16pre3_test/region/r.-1.0.mca")
#        create_biome_image(region,-32,0,0,32)
#        print("parsing r.-1.1.mca")
#        region = anvil.Region.from_file("/home/integ/.minecraft/saves/1_16pre3_test/region/r.-1.1.mca")
#        create_biome_image(region,-32,0,32,64)
#
#        print("parsing r.-2.-2.mca")
#        region = anvil.Region.from_file("/home/integ/.minecraft/saves/1_16pre3_test/region/r.-2.-2.mca")
#        create_biome_image(region,-64,-32,-64,-32)
#        print("parsing r.-2.-1.mca")
#        region = anvil.Region.from_file("/home/integ/.minecraft/saves/1_16pre3_test/region/r.-2.-1.mca")
#        create_biome_image(region,-64,-32,-32,0)
#        print("parsing r.-2.0.mca")
#        region = anvil.Region.from_file("/home/integ/.minecraft/saves/1_16pre3_test/region/r.-2.0.mca")
#        create_biome_image(region,-64,-32,0,32)
#        print("parsing r.-2.-1.mca")
#        region = anvil.Region.from_file("/home/integ/.minecraft/saves/1_16pre3_test/region/r.-2.1.mca")
#        create_biome_image(region,-64,-32,32,64)


        j=0
        for i in range(256):
            if global_biome_totals[i] > 0:
                j+=1
                print(j,i," ",BIOMES[i],": ",global_biome_totals[i])
                

    except KeyboardInterrupt:
        return 75 # EX_TEMPFAIL
    
    return 0 # NOERR


if __name__ == '__main__':
    if (len(sys.argv) == 1):
        print("No region file specified")
        sys.exit(64) # EX_USAGE
    region_file = sys.argv[1]
    # clean path name, eliminate trailing slashes:
    region_file = os.path.normpath(region_file)
    if (not os.path.exists(region_file)):
        print("No such folder as "+region_file)
        sys.exit(72) # EX_IOERR
    
    sys.exit(main(region_file))