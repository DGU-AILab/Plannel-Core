#import docker
from datetime import datetime as dt, timedelta

"""
Attributes for each container
"""

class ContainerAttrs():

    def __init__(self, ContainerId):

        state_list = ["Status","Running","Paused","Dead","ExitCode","StartedAt","FinishedAt"]
        self.client = docker.from_env()
        self.container = self.client.containers.get(ContainerId)
        self.attrs = self.container.attrs

        self.created = self.attrs['Created']
        self.state = { k:self.attrs['State'][k] for k in state_list} # dict about state "Status", "Running", etc..

        self.since_created = dt.utcnow() - str_to_datetime(self.created)
        self.uptime = (dt.utcnow() - str_to_datetime(self.state["StartedAt"])) if (self.state['Running']) else 0


def str_to_datetime(isoformattime):
    #for isoformat like 2021-02-07T14:57:06.842819525Z
    #Created or StartedAt states
    #Sould remove below the .(decimal point), cause it's too long below the decimal point
    return dt.strptime(isoformattime.split(".")[0] , "%Y-%m-%dT%H:%M:%S")
