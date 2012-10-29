#!/bin/python
# coding: utf-8
#
# Copyright Wojciech Żółtak 2012
#

from optparse import OptionParser
import sqlite3
import sys

DB_FILE = "easy-todo.db3"

def init(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS todo_items ( \
                        id INTEGER PRIMARY KEY, \
                        priority INTEGER NOT NULL DEFAULT 5, \
                        item TEXT NOT NULL DEFAULT ''  \
                    );")

def select_items(cursor, max_priority, min_priority, limit):
    result = cursor.execute("SELECT id, item, priority FROM todo_items \
                            WHERE priority <= ? AND priority >= ? \
                            ORDER BY priority, id LIMIT ?",
                           (max_priority, min_priority, limit))
    for row in result:
        (id, item, priority) = row
        print "{0}) {1} [{2}]".format(id, item, priority)

def add_item(cursor, priority, item):
    cursor.execute("INSERT INTO todo_items \
               VALUES(NULL, ?, ?)", (priority, item))

def remove_item(cursor, id):
    cursor.execute("DELETE FROM todo_items \
                    WHERE id = ?", id)

def update_item(cursor, id, text=None, priority=None):
    # TODO: Refactorize to use only one query
    if text:
        cursor.execute("UPDATE todo_items \
                        SET item = ? \
                        WHERE id = ?", (text, id))
    if priority:
        print "updating"
        cursor.execute("UPDATE todo_items \
                        SET priority = ? \
                        WHERE id = ?", (priority, id))


def main():
    parser = OptionParser()
    parser.add_option("-a", "--add", dest="add", help="add new item",
                     metavar="ITEM", action="store_true")
    parser.add_option("-t", "--text", dest="text", help="item content",
                      default=None)
    parser.add_option("-p", "--priority", dest="priority", help="item priority",
                      default=None, type="int")
    parser.add_option("-d", "--delete", dest="del", help="remove item",
                     metavar="ITEM_INDEX")
    parser.add_option("-q", "--query", action="store_true", dest="query")
    parser.add_option("--min", dest="min",
                      help="minimal priority of item during querying",
                      default=0, type="int")
    parser.add_option("--max", dest="max",
                      help="maximal priority of item during querying",
                      default=10, type="int")
    parser.add_option("-l", "--limit", dest="limit", type="int", default=10,
                      help="limit of items returned from query")
    parser.add_option("-r", "--remove", dest="remove", help="remove item",
                      metavar="ID")
    parser.add_option("-u", "--update", dest="update", help="update item",
                      metavar="ID")

    (options, args) = parser.parse_args()


    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    try:
        init(c)
        if options.query:
            select_items(c, options.max, options.min, options.limit)
        elif options.add:
            if not options.text:
                print "item content required!"
                # still reaches "finally" block
                return
            options.priority = options.priority if options.priority else 5
            add_item(c, options.priority, options.text)
        elif options.remove:
            remove_item(c, options.remove)
        elif options.update:
            update_item(c, options.update, options.text, options.priority)
        conn.commit()
    finally:
        conn.close()


if __name__ == "__main__":
    main()
