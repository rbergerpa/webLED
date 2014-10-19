#!/bin/bash

cd `dirname $0`

/usr/local/bin/gunicorn -w 4 -b 0.0.0.0:80 led:app
