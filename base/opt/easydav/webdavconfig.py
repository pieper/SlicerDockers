# -*- coding: utf-8 -*-

# Root directory for files that are served through WebDAV.
# Users are denied access outside this directory.

root_dir = '/home/researcher'

# Root url of the WebDAV repository.
# Can usually be None, so that the program automatically decides the path
# based on request.
# If specified, should be like 'http://domain.com/webdav.cgi/'.
# Any spaces and other special characters in the url must be encoded with the
# percent notation (like %20 for space).
root_url = None

# Access restrictions
# List entries can be either shell glob patterns (* and ? wildcards)
# or Python functions taking a path and returning a boolean.
#
# Glob patterns are matched against each component of the path, so that
# e.g. '.svn' also denies access to all files under '.svn'.
#
# Python functions get the whole path to the file in file system and
# should return True to deny access.

# Deny all access to these files.
restrict_access = [
    '.ht*',
    '.svn',
    '.easydav_locks'
]
    
# Deny write access to these files.
restrict_write = [
    '*.php',
    '*.cgi',
    '*.fcgi',
    '*.pl',
    
    # Apache is silly and matches multiple file extension
    # individually in some configurations.
    # E.g. test.php.txt gets parsed as php.
    '*.php.*',
    '*.cgi.*',
    '*.fcgi.*',
    '*.pl.*',
]

# Enable or disable the HTML interface, intended for web browsers.
# This does not affect webdav clients.
# Allowed values: '' (no html interface), 'r' (read only) or 'rw' (read write)
html_interface = 'rw'

# File name normalization
# Unicode can express same letters in multiple forms, such as composed and
# decomposed forms. Therefore it is possible to have two filenames that
# look exactly the same but compare inequal.
#
# Problem is further complicated because Mac OS X normalizes filenames to
# the decomposed form, whereas Windows and Linux use the composed form by
# default. This setting uses Python's unicodedata.normalize() to normalize
# filenames passed by clients.
#
# Suggested setting is 'NFC' to normalize to the composed form. You can also
# use None to disable normalization.
unicode_normalize = 'NFC'

# Lock configuration

# Lock database file, set to None to disable lock support.
# Path can be relative to root_dir or absolute.
lock_db = '.easydav_locks'

# Maximum timeout in seconds that clients can set for locks.
# The default setting 3600 lets locks stay for 1 hour before
# they have to be refreshed.
lock_max_time = 3600

# Internal timeout in seconds for accessing the lock database.
# Default setting should be ok unless you start seeing
# 503 Service Unavailable errors.
lock_wait = 5

# Error logging

# Log path, set to None to disable logging.
# Path can be relative to webdav.py location or absolute.
log_file = '/var/log/easydav/access.log'

# Log level, higher means less verbose output.
# Levels are defined in python module 'logging':
# DEBUG = 10
# INFO = 20
# WARN = 30
# ERROR = 40
# FATAL = 50
log_level = 30
