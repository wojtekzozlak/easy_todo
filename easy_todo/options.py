from optparse import OptionParser
from easy_todo.storage.sqlite3 import SQLite3Storage
from easy_todo.output import SimpleTextOutput


def createOptionParser():
    parser = OptionParser()
    addCommands(parser)
    addCommandsArguments(parser)
    return parser


def addCommands(parser):
    parser.add_option("-a", "--add", dest="add", help="add new item", metavar="ITEM",
                      action="store_true")
    parser.add_option("-d", "--delete", dest="del", help="remove item", metavar="ITEM_INDEX")
    parser.add_option("-q", "--query", action="store_true", dest="query")
    parser.add_option("-r", "--remove", dest="remove", help="remove item", metavar="ID")
    parser.add_option("-u", "--update", dest="update", help="update item", metavar="ID")


def addCommandsArguments(parser):
    parser.add_option("-t", "--text", dest="text", help="item content", default=None)
    parser.add_option("-p", "--priority", dest="priority", help="item priority", default=5,
                      type="int")
    parser.add_option("--min", dest="min", help="minimal priority of item during querying",
                      default=0, type="int")
    parser.add_option("--max", dest="max", help="maximal priority of item during querying",
                      default=10, type="int")
    parser.add_option("-l", "--limit", dest="limit", help="limit of items returned from query",
                      default=10, type="int")


class Driver(object):
    def __init__(self, config):
        self.storage = SQLite3Storage(config)
        self.output = SimpleTextOutput(config)

    def run(self, parsed_options):
        options, args = parsed_options
        with self.storage as storage:
            with self.output as output:
                if options.query:
                    result = storage.selectItems(options.max, options.min,
                        options.limit)
                    output.queryResult(result)
                elif options.add:
                    if not options.text:
                        output.noContent()
                    else:
                        storage.addItem(options.priority, options.text)
                        output.itemAdded()
                elif options.remove:
                    storage.removeItem(options.remove)
                    output.itemRemoved()
                elif options.update:
                    result = storage.updateItem(options.update, options.text, options.priority)
                    output.itemUpdated()
