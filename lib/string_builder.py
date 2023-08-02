class StringBuilder():
    def __init__(self):
        self.str = ""
    
    def add(self, new):
        self.str += new
    
    def size(self):
        return len(self.str)
    
    def output(self):
        return self.str