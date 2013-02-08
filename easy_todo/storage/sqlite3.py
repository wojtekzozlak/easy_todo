from __future__ import absolute_import
import sqlite3
import os.path
from copy import copy
from easy_todo.settings import APP_PATH

CONFIG_DATABASE = 'db'

DEFAULT_CONFIG = {
  CONFIG_DATABASE: os.path.join(APP_PATH, 'easy-todo.db3')
}


class SQLite3Storage(object):
    def __init__(self, config):
        # TODO: config check
        self.config = copy(DEFAULT_CONFIG)
        self.config.update(config)


    def __enter__(self):
        database = self.config[CONFIG_DATABASE]
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        self.__maybeInitDatabase()
        return self


    def __exit__(self, type, value, tb):
        if not tb:
            self.connection.commit()
        self.connection.close()


    def __maybeInitDatabase(self):
        self.cursor.execute("\
            CREATE TABLE IF NOT EXISTS todo_items ( \
                id INTEGER PRIMARY KEY, \
                priority INTEGER NOT NULL DEFAULT 5, \
                item TEXT NOT NULL DEFAULT ''    \
            );")


    def selectItems(self, max_priority, min_priority, limit):
        query_result = self.cursor.execute("\
            SELECT id, item, priority FROM todo_items \
            WHERE priority <= ? AND priority >= ? \
            ORDER BY priority, id LIMIT ?",
            (max_priority, min_priority, limit))

        items = []
        for row in query_result:
            (id, item, priority) = row
            items.append(dict(id=id, item=item, priority=priority))
        return items


    def addItem(self, priority, item):
        self.cursor.execute("\
            INSERT INTO todo_items \
            VALUES(NULL, ?, ?)",
            (priority, item))


    def removeItem(self, id):
        self.cursor.execute("\
            DELETE FROM todo_items \
            WHERE id = ?",
            id)


    def updateItem(self, id, text=None, priority=None):
        # TODO: Refactorize to use only one query
        if text:
            self.cursor.execute("\
                UPDATE todo_items \
                SET item = ? \
                WHERE id = ?",
                (text, id))
        if priority:
            self.cursor.execute("\
                UPDATE todo_items \
                SET priority = ? \
                WHERE id = ?",
                (priority, id))
