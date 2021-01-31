#!/bin/bash

VERSION="4.11.20200930"

docker build --build-arg VERSION=${VERSION} -t stevepieper/base:$VERSION base
docker build --build-arg VERSION=${VERSION} -t stevepieper/x11:$VERSION x11
docker build --build-arg VERSION=${VERSION} -t stevepieper/slicer:$VERSION slicer

docker build --build-arg VERSION=${VERSION} -t stevepieper/slicer-dev:$VERSION slicer-dev


docker build -t stevepieper/slicer3:$VERSION slicer3
docker build --build-arg VERSION=${VERSION} --no-cache -t stevepieper/slicer-chronicle:$VERSION slicer-chronicle

