# SlicerChronicle customized docker

FROM stevepieper/slicer
MAINTAINER pieper@isomics.com

COPY /home/researcher/.slicerrc.py /home/researcher

# Get modified Chronicle module
RUN git clone https://github.com/pieper/SlicerChronicle.git /home/researcher/SlicerChronicle



ENV SLICER_ARGUMENTS="--additional-module-paths /home/researcher/SlicerChronicle/SlicerChronicle"
