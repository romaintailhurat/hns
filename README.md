# Get your Hacker News upvoted stories

## TODOs

- move the secrets file outside the git repo ; add option `hns <command> --secrets /path/to/secrets.json`
- create specific CLI entry points with options (eg `hns hn`)

## How to run

Create a `secrets.json` file at the root of the project, with this layout:

```json
{ "user": "yourHNuserid", "password": "yourHNpassword" }
```

Install poetry, then:

```
poetry run python3 hns/main.py
```

It will create a `stories.json` file containing your upvoted stories titles and links.

## Dev

Using poetry with VS Code : https://olav.it/2019/11/16/configuring-poetry-in-visual-studio-code/

Parsing the resulting JSON file :

```bash
cat stories.json | jq .
cat stories.json | jq .count
cat stories.json | jq .updated
```
