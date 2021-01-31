# Slicer+extensions customized docker

ARG VERSION="latest"

FROM stevepieper/slicer:${VERSION}
MAINTAINER pieper@isomics.com

ARG SLICER_EXTS

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y xvfb

COPY install-slicer-extension.py /tmp

# add requests as helper package
RUN \
for ext in ${SLICER_EXTS} ; \
do echo "Installing ${ext}" ; \
  EXTENSION_TO_INSTALL=${ext} \
    su researcher -c "xvfb-run --auto-servernum \
      /opt/slicer/Slicer --python-script /tmp/install-slicer-extension.py" ; \
done


