

class FileReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        try:
            f = open(self.path)
            return f.read()
        except IOError as ex:
            return ''


