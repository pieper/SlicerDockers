# SlicerDocker platform image
# (based on https://github.com/dit4c/dockerfile-dit4c-container-slicer)

ARG VERSION="latest"

FROM stevepieper/x11:${VERSION}
MAINTAINER pieper@isomics.com

RUN apt-get install -y libglu1-mesa
RUN apt-get install -y libpulse-dev libnss3 libglu1-mesa
RUN apt-get install -y --reinstall libxcb-xinerama0
RUN apt-get install -y libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-render-util0 libxcb-xkb1 libxkbcommon-x11-0

# Slicer 4.5: http://download.slicer.org/bitstream/461634
# Slicer 4.8.1 http://download.slicer.org/bitstream/738960
# Slicer 4.10.1 http://download.slicer.org/bitstream/944596
# Slicer 4.10.2 http://download.slicer.org/bitstream/1023242

# Slicer 4.11.20200930
RUN SLICER_URL="http://download.slicer.org/bitstream/1341035" && \
  curl -v -s -L $SLICER_URL | tar xz -C /tmp && \
  mv /tmp/Slicer* /opt/slicer

# copy /opt after extraction slicer (/opt/slicer is extracted tar)
COPY /etc /etc
COPY /opt /opt
COPY /usr /usr


# See http://na-mic.org/Mantis/view.php?id=4015
RUN su researcher -c "mkdir /home/researcher/Documents"
COPY /home/researcher/Documents /home/researcher/Documents
RUN chown -R researcher:researcher /home/researcher/Documents

COPY /home/researcher/.config /home/researcher/.config
RUN chown -R researcher:researcher /home/researcher/.config

RUN LNUM=$(sed -n '/launcher_item_app/=' /etc/tint2/panel.tint2rc | head -1) && \
  sed -i "${LNUM}ilauncher_item_app = /opt/slicer/slicer.desktop" /etc/tint2/panel.tint2rc

# Note that slicer is started automatically at login from /etc/skel/.xinitrc
# it will run whatever is in the user's home directory .slicerrc.py, so any
# users of this docker image have the option of putting arbitrary startup commands in that file.
#
# Note also you can set the SLICER_ARGUMENTS environment variable using the -e "SLICER_ARGUMENTS=<value>"
# on the docker run command line.
