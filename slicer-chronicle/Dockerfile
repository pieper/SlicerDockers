# SlicerChronicle customized docker

FROM stevepieper/slicer
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

# add requests as helper package
RUN (cd $S4EXT/SlicerChronicle/SlicerChronicle; \
	git clone https://github.com/kennethreitz/requests.git reqests-checkout; \
        chown -R researcher:researcher reqests-checkout; \
        mv reqests-checkout/requests requests; \
        rm -rf reqests-checkout; \
        )


COPY /home/researcher/.slicerrc.py /home/researcher
RUN chown -R researcher:researcher /home/researcher/.slicerrc.py

# configure slicer as needed
ENV SLICER_ARGUMENTS="--additional-module-paths ${S4EXT}/SlicerChronicle/SlicerChronicle"
