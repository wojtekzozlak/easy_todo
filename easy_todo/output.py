class SimpleTextOutput(object):
    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        pass

    def __init__(self, config):
        pass

    def queryResult(self, items):
        for item in items:
            print "{0}) {1} [{2}]".format(item['id'], item['item'], item['priority'])

    def noContent(self):
        print "Item content required!"

    def itemAdded(self):
        print "Item added"

    def itemRemoved(self):
        print "Item removed"

    def itemUpdated(self):
        print "Item updated"
