#!/usr/bin/env bash
scp -r . lhy@server.lhy.kr:/srv/foodfly
ssh lhy@server.lhy.kr -C '~/.pyenv/versions/proj-7th-team4-foodfly/bin/pip install -r /srv/foodfly/.requirements/local.txt'
