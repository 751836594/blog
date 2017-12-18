#!/usr/bin/env bash
docker build \
        --rm=true \
        -f ./docker/online/Dockerfile \
        -t blog/online .