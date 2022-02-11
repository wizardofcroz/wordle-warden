# wordle-warden
# Configuring secrets
A discord bot API key must be created in a file `secrets.py` and contain the string variable `api_key`
# Building docker container
- clone the repo and cd in
- `docker build -t wordle-warden .`
# Running docker container
- `docker run -d world-warden` (-d runs in background)
