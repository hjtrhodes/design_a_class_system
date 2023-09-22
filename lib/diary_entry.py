class DiaryEntry:
    def __init__(self, title, contents): # title, contents are strings
        self.title = title
        self.contents = contents
        self.word_count = len(contents.split(' '))
        self.read_time = 0


    def reading_time(self, wpm):
        self.read_time = round(self.word_count/wpm)
        return self.read_time