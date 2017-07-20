"""
JupyterHub Spawner to spawn user notebooks on an OpenStack cluster.

After installation, you can enable it by adding:

```
c.JupyterHub.spawner_class = 'openstackspawner.OpenStackSpawne'
```

in your `jupyterhub_config.py` file.

We export KubeSpawner specifically here. This simplifies import for users.
Users can simply import openstackspawner.OpenStackSpawner in their applications
instead of the more verbose import openstackspawner.spawner.OpenStackSpawner.
"""
from openstackspawner.spawner import OpenStackSpawner

__all__ = [OpenStackSpawner]
