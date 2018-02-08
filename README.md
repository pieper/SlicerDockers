These are the docker configuration files to make a baseline user
environment for [3D Slicer][slicer].

It includes:
* base: a gui-less debian with file management via webdav
* x11: a basic gui environment with noVNC
* slicer-dev: pre-installed developer environment to build Slicer
* slicer: a binary distribution version of Slicer you can connect to
* slicer-chronicle: an example of a customized slicer

The build.sh script shows how to make the dockers (change the account
from stevepieper to your docker hub name)

Then run the container with a command like this:

`docker run -d -p 8080:8080 --name slicer stevepieper/slicer-chronicle`

then open `localhost:8080` in your browser and click the "X11 Session" button.

Close the container down again with:

 docker rm -f slicer


Also works with [hyper](http://hyper.sh)

```
hyper run -d -p 80:8080 -p 2016:2016 --name slicer stevepieper/slicer-chronicle
hyper fip attach 199.245.58.37 slicer
```

[slicer]: http://slicer.org

