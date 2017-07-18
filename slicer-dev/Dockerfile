# SlicerDocker development image
# (based on https://github.com/dit4c/dockerfile-dit4c-container-slicer)

FROM stevepieper/x11
MAINTAINER pieper@isomics.com

RUN apt-get update

# useful utilities
RUN apt-get install -y \
  vim-gnome exuberant-ctags

# core Slicer dependencies
RUN apt-get install -y \
  libssl-dev libcurl4-openssl-dev \
  subversion git-core git-svn build-essential \
  libx11-dev libxt-dev \
  libfontconfig-dev libxrender-dev libncurses5-dev \
  libglu1-mesa libgl1-mesa-dev libosmesa6-dev libglu1-mesa-dev \
  qt-sdk

# includes our version of cmake
COPY usr /usr

