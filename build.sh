VERSION="v4.8.1"

docker build -t stevepieper/base:$VERSION base
docker build -t stevepieper/x11:$VERSION x11
docker build -t stevepieper/slicer-dev:$VERSION slicer-dev
docker build -t stevepieper/slicer3:$VERSION slicer3
docker build -t stevepieper/slicer:$VERSION slicer

docker build --no-cache -t stevepieper/slicer-chronicle:$VERSION slicer-chronicle

docker build -t stevepieper/slicer-dev:$VERSION slicer-dev
