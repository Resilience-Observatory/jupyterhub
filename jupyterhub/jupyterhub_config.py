c.JupyterHub.authenticator_class = 'jupyterhub.auth.PAMAuthenticator'
c.PAMAuthenticator.open_sessions = False

import os

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.use_internal_hostname = True
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_CONTAINER']
c.DockerSpawner.remove_containers = True
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
c.JupyterHub.hub_ip = '0.0.0.0'
c.JupyterHub.hub_connect_ip = 'jupyterhub'

c.DockerSpawner.environment = {
    'GRANT_SUDO': 'yes',
}

notebook_dir = '/home/jovyan/work'
c.DockerSpawner.notebook_dir = notebook_dir

host_data_path = os.environ.get('HOST_DATA_PATH')
c.DockerSpawner.volumes = { host_data_path: notebook_dir }

c.Authenticator.admin_users = { os.environ.get('ADMIN_USER') }
