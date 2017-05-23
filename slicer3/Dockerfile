# Slicer3Docker platform image
# (based on https://github.com/dit4c/dockerfile-dit4c-container-slicer)

FROM stevepieper/x11
MAINTAINER pieper@isomics.com

RUN apt-get install -y libglu1-mesa


# Slicer 3.6.3
RUN SLICER_URL="https://www.slicer.org/slicer3-downloads/Release/linux-x86_64/Slicer3-3.6.3-2011-03-04-linux-x86_64.tar.gz" && \
  curl -v -s -L $SLICER_URL | tar xz -C /tmp && \
  mv /tmp/Slicer* /opt/slicer



# copy /opt after extraction slicer (/opt/slicer is extracted tar)
COPY /etc /etc
COPY /opt /opt
COPY /usr /usr


RUN LNUM=$(sed -n '/launcher_item_app/=' /etc/tint2/panel.tint2rc | head -1) && \
  sed -i "${LNUM}ilauncher_item_app = /opt/slicer/slicer.desktop" /etc/tint2/panel.tint2rc
