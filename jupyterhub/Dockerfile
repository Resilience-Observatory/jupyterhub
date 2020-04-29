FROM jupyterhub/jupyterhub:1.2

COPY jupyterhub_config.py .

RUN  curl -O https://raw.githubusercontent.com/jupyterhub/jupyterhub/master/examples/cull-idle/cull_idle_servers.py

RUN pip install \
    dockerspawner==0.11.1
