#!/bin/bash

#VERSION="4.11.20200930"
#VERSION="5.0.3"
VERSION="5.2.2"

docker push stevepieper/base:$VERSION
docker push stevepieper/x11:$VERSION
docker push stevepieper/slicer:$VERSION

exit

docker push stevepieper/slicer3:$VERSION

docker push stevepieper/slicer-morph:$VERSION
docker push stevepieper/slicer-dmri:$VERSION

docker push stevepieper/slicer-chronicle:$VERSION

docker push stevepieper/slicer-dev:$VERSION
