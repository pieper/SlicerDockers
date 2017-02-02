These are the docker configuration files to make a baseline user
environment for [3D Slicer][slicer].

It includes:
* base: a gui-less debian with file management via webdav
* x11: a basic gui environment with noVNC
* slicer: a version of Slicer you can connect to
* slicer-chronicle: an example of a customized slicer

The build.sh script shows how to make the dockers (change the account
from stevepieper to your docker hub name)

Then run the container with a command like this:

`docker run -d -p 8080:8080 --name slicer stevepieper/slicer-chronicle`


[slicer]: http://slicer.org

