# wordle-warden

## Configuring secrets
A discord bot API key must be created in a file `secrets.py` and contain the string variable `api_key`. Program will exit if value empty.

## Using pre-built docker image (reccomended)
- `docker run -d ccrosby/wordle-warden` (assuming connor set the secrets up, otherwise use `jamesdesmond`)

## Building docker container locally
- `git clone` the repo and `cd` into it
- `docker build -t wordle-warden .`
- `docker run -d wordle-warden` (-d runs in background)


### Automatic Linting
This project automatically lints all new and edited files on each commit. 

[Here is how to run the linter locally](https://github.com/github/super-linter/blob/main/docs/run-linter-locally.md)

## TODO:
- Add function which writes wordle messages to disk.
    - Use these messages as test data for a pytest suite for unit+regression testing (some weird unicode stuff would be good here)
- Generate a leaderboard or parse all score files for lifetime stats
    - e.g. Who has lowest overall avg. score? (and inverse)
    - Convert all the .txt files to .csv format one-time
    - Script then parses all .csv files and generates report
    - Data structure: List of tuples in form: `[(username,[scores])]`
    - Possible consideration to data structure:
        - does not capture the date of score
            - Possibly [scores] should be in form `[{date:score}]`
            - Full schema: `[(username,{date:score})]`
- Auto-mark the day's word as spoilertext in worldle channel?