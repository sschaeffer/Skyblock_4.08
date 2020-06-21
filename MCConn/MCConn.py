import collections
import struct
import socket
import time

Packet = collections.namedtuple("Packet", ("ident", "kind", "payload"))

class IncompletePacket(Exception):
    def __init__(self, minimum):
        self.minimum = minimum

class MCConn:

    DEADLINETIME = 5.0
    BUFSIZE = 4096

    def __init__(self,server="rio",port=25577,player="stephenschaeffer"):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server
        self.port = port
        self.password = "M!necraft"
        self.player = player
        self.playerx = 0
        self.playery = 0 
        self.playerz = 0
        self.reset_connection = False

    def sleep(self,sleeptime):
        if sleeptime < 1.0:
            time.sleep(sleeptime)
        else:
            for i in range(int(sleeptime)):
                time.sleep(1.0)
                print(".",end="")

    def decode_packet(self, data):
        """
        Decodes a packet from the beginning of the given byte string. Returns a
        2-tuple, where the first element is a ``Packet`` instance and the second
        element is a byte string containing any remaining data after the packet.
        """

        if len(data) < 14:
            raise IncompletePacket(14)

        length = struct.unpack("<i", data[:4])[0] + 4
        if len(data) < length:
            raise IncompletePacket(length)
         
        ident, kind = struct.unpack("<ii", data[4:12])
        payload, padding = data[12:length-2], data[length-2:length]
        assert padding == b"\x00\x00"
        return Packet(ident, kind, payload), data[length:]

    def encode_packet(self,packet):
        """
        Encodes a packet from the given ``Packet` instance. Returns a byte string.
        """

        data = struct.pack("<ii", packet.ident, packet.kind) + packet.payload + b"\x00\x00"
        return struct.pack("<i", len(data)) + data

    def receive_packet(self):
        """
        Receive a packet from the given socket. Returns a ``Packet`` instance.
        """

        data = b""
        while True:
            try:
                return self.decode_packet(data)[0]
            except IncompletePacket as exc:
                deadline = time.time() + self.DEADLINETIME
                while len(data) < exc.minimum:
                    if time.time() >= deadline:
                        self.reset_connection=True
                        return Packet(-1,0,"")
                    try:
                        data += self.sock.recv(exc.minimum - len(data))
                    except ConnectionResetError as exc:
                        self.reset_connection=True
                        return Packet(-1,0,"")


    def send_packet(self, packet):
        """
        Send a packet to the given socket.
        """
        self.sock.sendall(self.encode_packet(packet))


    def login(self):
        """
        Send a "login" packet to the server. Returns a boolean indicating whether
        the login was successful.
        """
        self.sock.connect((self.server, self.port))
        self.send_packet(Packet(0, 3, self.password.encode("utf8")))
        packet = self.receive_packet()
        return packet.ident == 0

    def close(self):
        self.sock.close()

    def command(self, text):
        """
        Sends a "command" packet to the server. Returns the response as a string.
        """
        self.send_packet(Packet(0, 2, text.encode("utf8")))
        self.send_packet(Packet(1, 0, b""))
        response = b""
        while True:
            packet = self.receive_packet()
            if packet.ident != 0:
                break
            response += packet.payload

        if(self.reset_connection==True):
            self.sock.close()
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.login()

        return response.decode("utf8")

    def tp(self, x, y, z, player=""):
        if player == "":
            player = self.player
            self.playerx = x
            self.playery = y 
            self.playerz = z
        self.command("tp "+player+" "+str(x)+" "+str(y)+" "+str(z))

    def teleport(self, x, y, z, teleportpresleep=0, teleportpostsleep=0):
        self.sleep(teleportpresleep)
        if self.playery == 0:
            self.tp(x,y,z)
        else:
            if(self.playerx == x and self.playery == y and self.playerz == z):
                return(0)
            else:
                if self.playerx - x > 0: nx=self.playerx-1
                elif self.playerx - x < 0: nx=self.playerx+1
                else: nx=x
                if self.playery - y > 0: ny=self.playery-1
                elif self.playery - y < 0: ny=self.playery+1
                else: ny=y
                if self.playerz - z > 0: nz=self.playerz-1
                elif self.playerz - z < 0: nz=self.playerz+1
                else: nz=z
                self.tp(nx,ny,nz)
                return(self.teleport(x,y,z))
        self.sleep(teleportpostsleep)
  

    def checkbiome(self):
        response = self.command(self.sock,"scoreboard players get "+self.player+" playerBiome")
        response_split = response.split(" ")
        return int(response_split[2])

    def killall_mobs(self):
        self.command("kill @e[name=!stephenschaeffer,name=!aidenschaeffer,name=!ryanschaeffer]")

    def gamerule_stop(self):
        self.command("gamerule doWeatherCycle false")
        self.command("weather clear")
        self.command("gamerule doDaylightCycle false")
        self.command("time set day")
        self.command("gamerule doMobSpawning false")
        self.command("kill @e[name=!stephenschaeffer,name=!aidenschaeffer,name=!ryanschaeffer]")

    def gamerule_start(self):
        self.command("gamerule doWeatherCycle true")
        self.command("gamerule doDaylightCycle true")
        self.command("gamerule doMobSpawning true")

    def fill(self, x1, z1, y1, x2, z2, y2, block):
        self.command("fill "+str(int(x1))+" "+str(int(z1))+" "+str(int(y1))+" "+\
                        str(int(x2))+" "+str(int(z2))+" "+str(int(y2))+" "+block)

    def point(self, x, z, y, block):
        self.fill(x, z, y, x, z, y, block)

    def xline(self, x, z, y1, y2, block):
        self.fill(x, z, y1, x, z, y2, block)

    def xwall(self, x, z1, z2, y1, y2, block):
        self.fill(x, z1, y1, x, z2, y2, block)

    def yline(self, x1, x2, z, y, block):
        self.fill(x1, z, y, x2, z, y, block)

    def ywall(self, x1, x2, z1, z2, y, block):
        self.fill(x1, z1, y, x2, z2, y, block)

    def plane(self, x1, x2, y1, y2, z, block):
        self.fill(x1, z, y1, x2, z, y2, block)

    def floor(self, x1, x2, y1, y2, block):
        self.fill(x1, 0, y1, x2, 0, y2, block)

    def container(self, x1, z1, y1, x2, z2, y2, extblock, intblock, debug=False):
        fill(x1, z1, y1, x2, z2, y2, extblock, debug)
        fill(x1+1, z1+1, y1+1, x2-1, z2-1, y2-1, intblock, debug)

    def opencontainer(self, x1, z1, y1, x2, z2, y2, extblock, intblock, debug=False):
        fill(x1, z1, y1, x2, z2, y2, extblock, debug)
        fill(x1+1, z1+1, y1+1, x2-1, z2, y2-1, intblock, debug)

        self.x = self.cx*16
        self.y = self.cy*16

    def clear_chunk(self,x,z):
        print("Clearing",x,z,x*16,z*16)
        self.fill((x*16),128,(z*16),(x*16)+15,255,(z*16)+15,"air")
        self.fill((x*16),0,(z*16),(x*16)+15,127,(z*16)+15,"air")

    def clear_chunkline(self,x,z,linesize=11,directionx=True,teleport=True,teleportpresleep=0.0,teleportpostsleep=0.0):
        if(teleport):
            self.teleport((x*16)+8,130,(z*16)+8,teleportpresleep,teleportpostsleep)
        if(directionx):
            for xd in range(linesize):
                self.clear_chunk(x+(xd-int(linesize/2)),z)
        else:
            for zd in range(linesize):
                self.clear_chunk(x,z+(zd-int(linesize/2)))

    def clear_pushbroom(self,x,z,length,stepback=0,repeat=0,linesize=11,directionx=True,teleport=True,\
                        teleportpresleep=0.0,teleportpostsleep=0.0):
        if(length>0):
            for i in range(length):
                for j in range(repeat+1):
                    if j == 0: self.clear_chunkline(x,z+i,linesize,directionx,teleport,teleportpresleep,teleportpostsleep)
                    else: self.clear_chunkline(x,z+i,linesize,directionx,teleport=False)
                    for k in range(stepback):
                        self.clear_chunkline(x,z+i-(k+1),linesize,directionx,teleport=False)
        else:
            for i in range(abs(length)):
                for j in range(repeat+1):
                    if j == 0: self.clear_chunkline(x,z-i,linesize,directionx,teleport,teleportpresleep,teleportpostsleep)
                    else: self.clear_chunkline(x,z-i,linesize,directionx,teleport=False)
                    for k in range(stepback):
                        self.clear_chunkline(x,z-i+(k+1),linesize,directionx,teleport=False)