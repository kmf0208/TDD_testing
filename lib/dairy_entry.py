import math

class DiaryEntry:
    def __init__(self, title, contents):
        if title == '' or contents == '':
            raise Exception("sorry no title to show")
        self.title = title
        self.contents = contents
        self.read_so_far = 0

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
       words = self.format().split()
       return len(words)
    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception('sorry can not calculate time with wpm of zero')
        contents_word = len(self._contents_words())
        return math.ceil(contents_word /wpm)

    def reading_chunk(self, wpm, minutes):
        words_can_read = wpm * minutes
        num_words = self._contents_words()
        if self.read_so_far >= len(num_words):
            self.read_so_far = 0
        chunk_start = self.read_so_far
        chunk_end =  self.read_so_far + words_can_read
        chunk_words = num_words[chunk_start:chunk_end]
        self.read_so_far = chunk_end
        return ' '.join(chunk_words)
    
    def _contents_words(self):
        return self.contents.split()