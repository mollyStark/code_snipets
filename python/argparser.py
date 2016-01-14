# -*- coding: utf-8 -*-
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-x", "--xarg", required=True, help="Function of this argument")
ap.add_argument("-y", "--optional", help="Function of this argument")
args = vars(ap.parse_args())

# get the argument
xarg = args["xarg"]
opt = args["optional"]

print xarg, opt
