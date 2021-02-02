from container import Container
import docker

class ContainerController:

    def __init__(self):
        self.client = docker.from_env()
        pass

    """
        RESULT EXAMPLE:
        hash : e3875c9e38f9, entrypoint : ['/usr/local/bin/docker-entrypoint'], image : docker.elastic.co/logstash/logstash:6.2.2
        hash : efe4b2141f04, entrypoint : None, image : docker.elastic.co/kibana/kibana:6.2.2
        hash : f4029f2141fd, entrypoint : ['/usr/local/bin/docker-entrypoint.sh'], image : docker.elastic.co/elasticsearch/elasticsearch:6.2.2
    """
    def get_all_containers(self):
        containers = self.client.containers.list(all=True)
        results = []
        for container in containers:
            config = container.attrs['Config']
            hostname = config['Hostname']
            image = config['Image']
            entrypoint = config['Entrypoint']
            env = config['Env']
            cont_obj = Container(hostname, image, entrypoint, env)
            results.append(cont_obj)
            print(cont_obj)
        return results
