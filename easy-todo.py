#!/usr/bin/python
# coding: utf-8
#
# Copyright Wojciech Żółtak 2012
#
import storage
from options import createOptionParser, runDriver
from storage.sqlite3 import SQLite3Storage
from settings import getConfig


def main():
    parser = createOptionParser()
    (options, args) = parser.parse_args()
    config = getConfig()
    driver = SQLite3Storage(config)
    runDriver(driver, parser.parse_args())


if __name__ == "__main__":
    main()
