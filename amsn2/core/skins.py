import os.path

class Skin(object):
    def __init__(self, core, path):
        self.path = path
        pass

    def getKey(self, key, default):
        pass

    def setKey(self, key, value):
        pass

    def getFilename(self, name):
        return os.path.join(path, name + ".png")


class SkinManager(object):
    def __init__( core):
        self.skin = Skin(core, "skins")

    def setSkin(self, name):
        self.skin = Skin(core, os.path.join("skins", name))

    def listSkins(self, path):
        pass
