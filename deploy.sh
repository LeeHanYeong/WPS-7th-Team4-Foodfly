#!/usr/bin/env bash
scp -r .requirements lhy@server.lhy.kr:/srv/foodfly/.requirements
scp -r .secrets lhy@server.lhy.kr:/srv/foodfly/.secrets
scp -r app lhy@server.lhy.kr:/srv/foodfly/app
ssh lhy@server.lhy.kr -C '~/.pyenv/versions/proj-7th-team4-foodfly/bin/pip install -r /srv/foodfly/.requirements/local.txt'
