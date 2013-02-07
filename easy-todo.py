#!/usr/bin/python
# coding: utf-8
#
# Copyright Wojciech Żółtak 2012
#

import sqlite3
import storage
from options import createOptionParser, runDriver
from storage.sqlite3 import SQLite3Storage

DB_FILE = "easy-todo.db3"

def main():
    parser = createOptionParser()
    (options, args) = parser.parse_args()
    driver = SQLite3Storage( dict(db=DB_FILE) )
    runDriver(driver, parser.parse_args())

if __name__ == "__main__":
    main()
