class Gratitudes():
    def __init__(self):
        self.gratitudes = []
    
    def add(self, arr):
        self.gratitudes.append(arr)

    def format(self):
        formatted = "Be grateful for: "
        formatted += ", ".join(self.gratitudes)
        return formatted