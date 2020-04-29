# JupyterHub deployment for the resilience COVID-19 observatory

This is a [JupyterHub](https://jupyter.org/hub) deployment based on
Docker.

Based on [defeo/jupyterhub-docker](https://github.com/defeo/jupyterhub-docker).

## Features

- Containerized single user Jupyter servers, using
  [DockerSpawner](https://github.com/jupyterhub/dockerspawner).
- Authentication against the Unix users on the host.
- User data persistence.

### Adapt to your needs

This deployment is ready to clone and roll on your own server. Read
the [blog
post](https://opendreamkit.org/2018/10/17/jupyterhub-docker/) first,
to be sure you understand the configuration.

Then, if you like, clone this repository and apply (at least) the
following changes:

- In [`.env`](.env), set the variable `HOST` to the name of the server you
  intend to host your deployment on.
- In
  [`jupyterhub/jupyterhub_config.py`](jupyterhub/jupyterhub_config.py),
  edit the *Authenticator* section and the *DockerSpawner* section.

Other changes you may like to make:

- Edit [`datascience-notebook/Dockerfile`](jupyterlab/Dockerfile) to include the
  software you like.

### Run!

Once you are ready, build and launch the application with

```
docker-compose build
docker-compose up -d
```

Read the [Docker Compose manual](https://docs.docker.com/compose/) to
learn how to manage your application.
