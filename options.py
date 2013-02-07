from optparse import OptionParser


def createOptionParser():
    parser = OptionParser()
    addCommands(parser)
    addCommandsArguments(parser)
    return parser


def addCommands(parser):
    parser.add_option("-a", "--add", dest="add", help="add new item",
                      metavar="ITEM", action="store_true")
    parser.add_option("-d", "--delete", dest="del", help="remove item",
                      metavar="ITEM_INDEX")
    parser.add_option("-q", "--query", action="store_true", dest="query")
    parser.add_option("-r", "--remove", dest="remove", help="remove item",
                      metavar="ID")
    parser.add_option("-u", "--update", dest="update", help="update item",
                      metavar="ID")


def addCommandsArguments(parser):
    parser.add_option("-t", "--text", dest="text", help="item content",
                      default=None)
    parser.add_option("-p", "--priority", dest="priority", help="item priority",
                      default=5, type="int")
    parser.add_option("--min", dest="min",
                      help="minimal priority of item during querying",
                      default=0, type="int")
    parser.add_option("--max", dest="max",
                      help="maximal priority of item during querying",
                      default=10, type="int")
    parser.add_option("-l", "--limit", dest="limit", type="int", default=10,
                      help="limit of items returned from query")


def runDriver(driver, parsed_options):
    options, args = parsed_options
    with driver:
      if options.query:
        driver.selectItems(options.max, options.min, options.limit)
      elif options.add:
        if not options.text:
            print "item content required!"
            return
        driver.addItem(options.priority, options.text)
      elif options.remove:
        driver.removeItem(options.remove)
      elif options.update:
        driver.updateItem(options.update, options.text, options.priority)
