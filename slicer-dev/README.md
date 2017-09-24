[Slicer](https://www.slicer.org/) Docker image with dev dependecies for building Slicer (Qt5)

Run with:

docker run -d -p 8080:8080 --name slicer-dev stevepieper/slicer-dev

Then connect to localhost:8080 to interact.

# Simple build with defaults (using Qt4 preinstalled on this docker):

For a quicker limited build:
```
git clone https://github.com/Slicer/Slicer \
&& mkdir Slicer-superbuild \
&& cd Slicer-superbuild \
&& cmake \
  -DSlicer_USE_PYTHONQT_WITH_OPENSSL:BOOL=OFF \
  -DSlicer_BUILD_DataStore:BOOL=OFF \
  -DSlicer_BUILD_CLI_SUPPORT:BOOL=OFF \
  -DSlicer_USE_SimpleITK:BOOL=OFF \
  ../Slicer \
&& make -j8 2>&1 | tee /tmp/log.txt \
&& ./Slicer-build/Slicer
```
or for a complete build:
```
git clone https://github.com/Slicer/Slicer \
&& mkdir Slicer-superbuild \
&& cd Slicer-superbuild \
&& cmake ../Slicer \
&& make -j8 2>&1 | tee /tmp/log.txt \
&& ./Slicer-superbuild/Slicer-build/Slicer
```

# Experimental Qt5 build

## Get pre-built
```
cd /tmp
wget http://download.qt.io/official_releases/online_installers/qt-unified-linux-x64-online.run
chmod +x qt-unified-linux-x64-online.run
./qt-unified-linux-x64-online.run
```

Follow online prompts.  You can skip registration.  Accept default options for install.

## Build from source

RUN wget http://download.qt.io/official_releases/qt/5.9/5.9.1/single/qt-everywhere-opensource-src-5.9.1.tar.xz && \
   tar xf qt-everywhere-opensource-src-5.9.1.tar.xz && \
   rm qt-everywhere-opensource-src-5.9.1.tar.xz && \
   cd qt-everywhere-opensource-src-5.9.1 && \
   ./configure \
     -opensource -confirm-license \
     -no-compile-examples \
     -icu -openssl -qt-xcb -opengl -gui -widgets \
     -release && \
   make -j$(nproc) && \
   make install && \
   cd .. && rm -rf qt-everywhere-opensource*


```
export SLICER_REPO=https://github.com/msmolens/Slicer
export SLICER_TAG=support-qt5-2017-07-18-r26154
cd ~
git clone ${SLICER_REPO} Slicer
(cd Slicer; git checkout ${SLICER_TAG})
mkdir Slicer-superbuild
(cd Slicer-superbuild; \
  cmake \
    -DSlicer_USE_SimpleITK:BOOL=OFF \
    -DSlicer_REQUIRED_QT_VERSION:STRING=5.7.1 \
    -DQt5_DIR:PATH=/home/researcher/Qt/5.9.1/gcc_64/lib/cmake/Qt5 \
  ../Slicer; \
  make -j8) 2>&1 | tee /tmp/log
```
