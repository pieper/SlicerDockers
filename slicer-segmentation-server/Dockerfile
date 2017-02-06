# WIP: segmentation server

FROM stevepieper/slicer-chronicle
MAINTAINER pieper@isomics.com

ARG OPERATIONS_DB=segmentation-server
ARG OPERATIONS_DB=$OPERATIONS_DB

ARG S4EXT=/home/researcher/slicerExtensions
ENV S4EXT=$S4EXT
RUN mkdir $S4EXT

# configure slicer as needed -overrides defaults in slicer-chronicle
COPY /home/researcher/.slicerrc.py /home/researcher


#
# set up dependencies for lesion segmenter use case
#

# Chest imaging platform
RUN (cd $S4EXT; \
     wget "http://slicer.kitware.com/midas3/download/index?items=262882" -O ext.tar.gz && \
     tar xvfz ext.tar.gz; rm ext.tar.gz)
ENV CIP="25516-linux-amd64-Chest_Imaging_Platform-gitbbe35a5-2017-01-26"

# Reporting
RUN (cd $S4EXT; \ 
     wget "http://slicer.kitware.com/midas3/download/index?items=262943" -O ext.tar.gz && \
     tar xvfz ext.tar.gz; rm ext.tar.gz)
ENV REPORTING="25516-linux-amd64-Reporting-git9bd1c06-2016-11-24"

# configure slicer as needed
ENV SLICER_ARGUMENTS="--additional-module-paths \
			${S4EXT}/SlicerChronicle/SlicerChronicle \
			${S4EXT}/${CIP}/lib/Slicer-4.6/cli-modules \
			${S4EXT}/${CIP}/lib/Slicer-4.6/qt-loadable-modules \
			${S4EXT}/${CIP}/lib/Slicer-4.6/qt-scripted-modules \
			${S4EXT}/${REPORTING}/lib/Slicer-4.6/cli-modules \
			${S4EXT}/${REPORTING}/lib/Slicer-4.6/qt-loadable-modules \
			${S4EXT}/${REPORTING}/lib/Slicer-4.6/qt-scripted-modules \
			"
