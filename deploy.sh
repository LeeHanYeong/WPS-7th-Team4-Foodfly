#!/usr/bin/env bash
# Pipfile이 변경되면 base이미지를 새로 빌드하고 업로드
base_image=$(docker images | grep foodfly:base)
diff=$(git diff Pipfile)
if [[ ! -z "$diff" || -z "$base_image" ]]; then
    pipenv lock --requirements > requirements.txt
    docker build -t foodfly:base -f .dockerfiles/Dockerfile.base .
    rm requirements.txt
    docker tag foodfly:base azelf/foodfly:base
    docker push azelf/foodfly:base
fi
