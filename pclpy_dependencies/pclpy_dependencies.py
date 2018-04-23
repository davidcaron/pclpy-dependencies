# -*- coding: utf-8 -*-

"""Main module."""

import os

here = os.path.split(__file__)[0]
bin_dir = os.path.join(here, "bin")

# add to PATH
if bin_dir not in os.environ["PATH"]:
    os.environ["PATH"] = "%s;%s" % (bin_dir, os.environ["PATH"])
