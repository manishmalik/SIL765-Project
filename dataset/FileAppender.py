class FileAppender:
    def __init__(self, file_name):
        self.file = open(file_name, "a")

    def append(self, string):
        self.file.write(string + "\n")

    def complete(self):
        self.file.close()