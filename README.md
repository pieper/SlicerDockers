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

The push.sh script sends the new images to hub.docker.com.

[slicer]: http://slicer.org


# Running a Slicer analysis script in an instance

The script below can be run in an instance and can be used as a template for more sophisticated analysis scripts.

```
"""
Here's a simple proof of concept example to run a slicer based script
in a docker instance.

Note that this runs in a full virtualized desktop envionment, so anything
that works in Slicer on a desktop should also work in the docker instance,
including rendering operations.

First create a directory called /tmp/shared that will serve as the bridge
between the host and the instance.

Then copy this file myScript.py into /tmp/shared

Run this script with a command like the following:

docker run -v /tmp/shared:/tmp/shared -p 8080:8080 --rm -it --env SLICER_ARGUMENTS="--python-script /tmp/shared/myScript.py" stevepieper/slicer

it should print some diagnostic info and then exit.

After it runs you will have a copy of the MRHead.nrrd sample data in the /tmp/shared directory.
"""

# as an example, download data and save it locally
import SampleData
mrHeadVolume = SampleData.downloadSample("MRHead")
slicer.util.saveNode(mrHeadVolume, "/tmp/MRHead-from-docker.nrrd")

import os

# use sudo to copy into the shared folder
os.system("sudo cp /tmp/MRHead-from-docker.nrrd /tmp/shared/MRHead-from-docker.nrrd")

# gracefully shut down the docker instance
os.system('sudo kill -s SIGTERM 1')
```
