"""
JupyterHub Spawner to spawn user notebooks on an OpenStack cluster.

This module exports `OpenStackSpawner` class, which is the actual spawner
implementation that should be used by JupyterHub.
"""
import os
import json
import time
import string
import threading
import sys
from urllib.parse import urlparse, urlunparse
from concurrent.futures import ThreadPoolExecutor
import multiprocessing


from tornado import gen
from tornado.concurrent import run_on_executor
from traitlets.config import SingletonConfigurable
from traitlets import Type, Unicode, List, Integer, Union, Dict, Bool, Any
from jupyterhub.spawner import Spawner
from jupyterhub.traitlets import Command
#from kubernetes.client.models.v1_volume import V1Volume
#from kubernetes.client.models.v1_volume_mount import V1VolumeMount
#from kubernetes.client.rest import ApiException
#from kubernetes import client
import escapism

#from kubespawner.traitlets import Callable
#from kubespawner.utils import request_maker, k8s_url
#from kubespawner.objects import make_pod, make_pvc
#from kubespawner.reflector import PodReflector

class OpenStackSpawner(Spawner):
    """
    Implement a JupyterHub spawner to spawn OpenStack instances.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    @gen.coroutine
    def start(self):
        return (pod.status.pod_ip, self.port)

    @gen.coroutine
    def stop(self, now=False):
        yield gen.sleep(1)

    @gen.coroutine
    def poll(self):
        return (pod.status.pod_ip, self.port)

    def get_state(self):
        """get the current state"""
        state = super().get_state()
        if self.pid:
            state['pid'] = self.pid
        return state

    def load_state(self, state):
        """load state from the database"""
        super().load_state(state)
        if 'pid' in state:
            self.pid = state['pid']

    def clear_state(self):
        """clear any state (called after shutdown)"""
        super().clear_state()
        self.pid = 0