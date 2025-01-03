import docker

c = get_config()

# Use DockerSpawner
c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"

# Networking settings
c.JupyterHub.hub_ip = "0.0.0.0"
c.JupyterHub.hub_port = 808
c.JupyterHub.port = 8000

# Create a custom Docker network instead of using bridge
c.DockerSpawner.network_name = "jupyterhub"
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.post_start_cmd = 'sh -c "cd work && python compile.py && rm leaderboard.py && rm checker.py && rm submission.py && rm compile.py"'
# Container configuration
c.DockerSpawner.image = "jupyterhub-user"
c.DockerSpawner.notebook_dir = "/home/jovyan/work"
c.DockerSpawner.remove = True

# Authentication
c.JupyterHub.authenticator_class = "dummyauthenticator.DummyAuthenticator"
c.DummyAuthenticator.allow_all = True
c.DummyAuthenticator.password = "test"
