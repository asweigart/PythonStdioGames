"""Turtle Demo Wrapper
This runs the turtledemo module that comes with Python, which contains
many example programs that use the Python's turtle module.
Tags: tiny, artistic"""
__version__ = 0
import sys, os

print('Running turtledemo module...')
os.system(sys.executable + ' -m turtledemo')