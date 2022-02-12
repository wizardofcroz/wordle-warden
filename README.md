# wordle-warden

## Configuring secrets
A discord bot API key must be created in a file `discord.key`. The file should only contain the key as text. It will be `cat`'d into the docker with the run command.

## Using pre-built docker image (reccomended)
- `docker run --env DISCORD_KEY=$(cat discord.key) -d alizzardwizzard/wordle-warden`

## Building docker container locally
- `git clone` the repo and `cd` into it
- `docker build -t wordle-warden .`
- `docker run --env DISCORD_KEY=$(cat discord.key) -d alizzardwizzard/wordle-warden` (-d runs in background)

### TODO:
- Add function which writes wordle messages to disk.
    - Use these messages as test data for a pytest suite for unit+regression testing (some weird unicode stuff would be good here)
- Auto-mark the day's word as spoilertext in worldle channel?
- Convert all the .txt files to .csv format one-time

### DONE:
- Generate a leaderboard or parse all score files for lifetime stats
    - e.g. Who has lowest overall avg. score? (and inverse)
    
    - Script then parses all .csv files and generates report
    - Data structure: List of tuples in form: `[(username,[scores])]`
    - Possible consideration to data structure:
        - does not capture the date of score
            - Possibly [scores] should be in form `[{date:score}]`
            - Full schema: `{username: [{date:score}]}`
