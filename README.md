# wordle-warden
# Configuring secrets
A discord bot API key must be created in a file `secrets.py` and contain the string variable `api_key`
# Building docker container locally
- `brew install docker`
- Install and run [Docker Desktop](https://docs.docker.com/desktop/mac/install/)
- clone the repo and cd in
- `docker build -t wordle-warden .`
- `docker run -d wordle-warden` (-d runs in background)
# Using pre-built docker image
- `docker run -d ccrosby/wordle-warden` (assuming connor set the secrets up, otherwise use `jamesdesmond`)
