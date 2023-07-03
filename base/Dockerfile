# DOCKER-VERSION 1.0

# Base image for other SlicerDocker platform images
# (inspired by https://github.com/dit4c/dockerfile-dit4c-container-base)
FROM ubuntu:22.04
MAINTAINER pieper@isomics.com

# Directories that don't need to be preserved in images
VOLUME ["/var/cache/apt", "/tmp"]

# Allow HTTPS right from the start
RUN apt-get update && apt-get install -y apt-transport-https && apt-get clean

# Install
# - sudo and passwd for creating user/giving sudo
# - supervisord for monitoring
# - nginx for reverse-proxying
# - patching dependencies
RUN apt-get update && apt-get install -y \
    sudo passwd \
    supervisor \
    nginx \
    vim nano curl wget tmux screen bash-completion man tar zip unzip \
    patch && \
  apt-get clean

# Install Git
RUN apt-get update && apt-get install -y git && apt-get clean

# Log directory for supervisord
RUN mkdir -p /var/log/supervisor

# Add supporting files (directory at a time to improve build speed)
COPY etc /etc
COPY opt /opt
COPY var /var

# Check nginx config is OK
RUN useradd -m nginx
RUN nginx -t

EXPOSE 8080
# Run all processes through supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]

RUN useradd -m researcher -s /bin/bash && \
    gpasswd -a researcher sudo && \
    passwd -d researcher && passwd -u researcher && \
    rm ~researcher/.bashrc ~researcher/.bash_logout ~researcher/.profile && \
    sed -i -e '/^PS1/s/^/#/' /etc/bash.bashrc && \
    sed -i -e '/stdout.*uname/s/^/#/' /etc/pam.d/login && \
    echo 'source /etc/profile.d/prompt.sh' >> /etc/bash.bashrc

RUN chown -R researcher /var/log/supervisor

# Logs do not need to be preserved when exporting
VOLUME ["/var/log"]

# Change MOTD
RUN sh -c '. /etc/os-release && echo "You are using $PRETTY_NAME | $HOME_URL" > /etc/motd'
