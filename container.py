import docker
from containerAttrs import ContainerAttrs

class Container:

    def __init__(self, hash, image, entrypoint, env):
        self.hash = hash
        self.image = image
        self.entrypoint = entrypoint
        self.env = env
        self.attrs = ContainerAttrs(self.hash)

    def __str__(self):
        self.attrs = ContainerAttrs(self.hash)
        return "hash : {}, entrypoint : {}, image : {}, created : {}, since_created : {}, container_uptime : {}, \
running_time : {}, exitcode : {}"\
            .format(self.hash, self.entrypoint, self.image, self.attrs.created, self.attrs.since_created, \
            self.attrs.state['StartedAt'], self.attrs.uptime, self.attrs.state['ExitCode'])
