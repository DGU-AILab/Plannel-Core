# https://github.com/DGU-AILab/Plannel
from container_controller import ContainerController
import configparser
import docker

print('Hello world!')

conf = configparser.ConfigParser()
conf.read('config.ini')

#conf[ini file name][keyword]
VERSION = conf['CONFIG']['version']
BOOTSTRAP_SERVER = conf['CONFIG']['bootstrap.server']
HEARTBEAT_INTERVAL_MS = conf['CONFIG']['heartbeat.interval.ms']

print(VERSION)
print(BOOTSTRAP_SERVER)
print(HEARTBEAT_INTERVAL_MS)

cont_ctrl = ContainerController()
cont_ctrl.get_all_containers()
