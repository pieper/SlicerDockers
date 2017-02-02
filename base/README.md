stevepieper/base is build from the example below:

dit4c/dit4c-container-base
===============================

[![](https://images.microbadger.com/badges/image/dit4c/dit4c-container-base:debian.svg)](https://microbadger.com/images/dit4c/dit4c-container-base:debian)

The base image for DIT4C containers, which includes a [GoTTY][gotty] shell and file uploader.

The essential rules/guidelines that it follows are:

1. Services are started & managed by supervisord.
2. Any web services provided by the container must be accessed via port 8080.
  * Nginx is used to reverse-proxy services on other ports. HTTP, WSGI & FastCGI proxying work fine.
  * As a result of this requirement, web services really need to exist on paths, not on "/".
3. `/home/researcher` should contain as few extraneous files as possible.

[gotty]: https://github.com/yudai/gotty
