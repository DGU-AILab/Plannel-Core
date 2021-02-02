import docker

class Container:

    def __init__(self, hash, image, entrypoint, env):
        self.hash = hash
        self.image = image
        self.entrypoint = entrypoint
        self.env = env

    def __str__(self):
        return "hash : {}, entrypoint : {}, image : {}"\
            .format(self.hash, self.entrypoint, self.image)
