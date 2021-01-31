# SlicerChronicle customized docker

ARG VERSION="latest"

FROM stevepieper/slicer:${VERSION}
MAINTAINER pieper@isomics.com

ARG COUCHDB_URL=http://quantome.org:5984
ARG CHRONICLE_DB=chronicle
ARG CHRONICLE_USER=""
ARG OPERATIONS_DB=operations

ENV COUCHDB_URL=$COUCHDB_URL
ENV CHRONICLE_DB=$CHRONICLE_DB
ENV CHRONICLE_USER=$CHRONICLE_USER
ENV OPERATIONS_DB=$OPERATIONS_DB

ARG S4EXT=/home/researcher/slicerExtensions
ENV S4EXT=$S4EXT
RUN mkdir $S4EXT

# Get SlicerChronicle module
RUN (cd $S4EXT; \
	git clone https://github.com/pieper/SlicerChronicle.git SlicerChronicle; \
        chown -R researcher:researcher SlicerChronicle \
        )

# add urllib3 as helper package
RUN (cd $S4EXT/SlicerChronicle/SlicerChronicle; \
	git clone https://github.com/shazow/urllib3.git urllib3-checkout; \
        (cd urllib3-checkout; git checkout 1.22); \
        chown -R researcher:researcher urllib3-checkout; \
        mv urllib3-checkout/urllib3 urllib3; \
        rm -rf urllib3-checkout; \
        )

# add idna as helper package
RUN (cd $S4EXT/SlicerChronicle/SlicerChronicle; \
	git clone https://github.com/kjd/idna.git idna-checkout; \
        (cd idna-checkout; git checkout v2.6); \
        chown -R researcher:researcher idna-checkout; \
        mv idna-checkout/idna idna; \
        rm -rf idna-checkout; \
        )

# add certifi as helper package
RUN (cd $S4EXT/SlicerChronicle/SlicerChronicle; \
	git clone https://github.com/certifi/python-certifi.git certifi-checkout; \
        (cd certifi-checkout; git checkout v1.0.1); \
        chown -R researcher:researcher certifi-checkout; \
        mv certifi-checkout/certifi certifi; \
        rm -rf certifi-checkout; \
        )

# add requests as helper package
RUN (cd $S4EXT/SlicerChronicle/SlicerChronicle; \
	git clone https://github.com/kennethreitz/requests.git requests-checkout; \
        (cd requests-checkout; git checkout v2.18.3); \
        chown -R researcher:researcher requests-checkout; \
        mv requests-checkout/requests requests; \
        rm -rf requests-checkout; \
        )

# Get SlicerWeb module
RUN (cd $S4EXT; \
	git clone https://github.com/pieper/SlicerWeb.git SlicerWeb; \
        chown -R researcher:researcher SlicerWeb \
        )
EXPOSE 2016


COPY /home/researcher/.slicerrc.py /home/researcher
RUN chown -R researcher:researcher /home/researcher/.slicerrc.py

# configure slicer as needed
ENV SLICER_ARGUMENTS="--additional-module-paths ${S4EXT}/SlicerChronicle/SlicerChronicle ${S4EXT}/SlicerWeb/WebServer"
