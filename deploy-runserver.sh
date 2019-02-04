#!/usr/bin/env bash
echo '============= Quit screen ======================'
ssh lhy@server.lhy.kr -C 'screen -X -S foodfly quit'

echo '============= Delete exist project files ======='
ssh root@server.lhy.kr -C 'rm -rf /srv/foodfly'

echo '============= scp project files ================'
scp -q -r . lhy@server.lhy.kr:/srv/foodfly

echo '============= pipenv install ==================='
ssh lhy@server.lhy.kr -C 'cd /srv/foodfly && /home/lhy/.local/bin/pipenv install --'

echo '============= Create session ==================='
ssh lhy@server.lhy.kr -C 'cd /srv/foodfly && screen -S foodfly -d -m'

echo '============= runserver ========================'
ssh lhy@server.lhy.kr -C "screen -r foodfly -X stuff $'DJANGO_SETTINGS_MODULE=config.settings.dev /home/lhy/.local/bin/pipenv run /srv/foodfly/app/manage.py runserver 0:8001\n'"
