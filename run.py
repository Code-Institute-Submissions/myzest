#! usr/bin/env python3.6
# coding: utf-8

from myzest import app
import os


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'))
