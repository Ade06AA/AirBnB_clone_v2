#!/usr/bin/python3
"""
extra
"""
from os import getenv


StorageType = getenv("HBNB_TYPE_STORAGE", "file")
