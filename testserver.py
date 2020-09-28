from pyraklib.server.PyRakLibServer import PyRakLibServer
from pyraklib.server.ServerHandler import ServerHandler
from pyraklib.server.ServerInstance import ServerInstance

class TestServer(ServerInstance):
    raknetServer = None
    handler = None

    def __init__(self):
        self.raknetServer = PyRakLibServer(19132)
        self.handler = ServerHandler(self.raknetServer, self)
        self.handler.sendOption("name", "MCPE;Dedicated Server;390;1.14.60;0;10;13253860892328930865;Bedrock level;Survival;1;19132;19133;")

    def openSession(self, identifier, address, port, clientID):
         print("CONNECTING...")

    def handleEncapsulated(self, identifier, packet, flags):
         print("CONNECTED!")

TestServer()
