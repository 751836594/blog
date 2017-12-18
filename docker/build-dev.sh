#!/usr/bin/env bash


docker build \
        --rm=true \
        -f ./docker/dev/Dockerfile \
        -t blog/dev .
