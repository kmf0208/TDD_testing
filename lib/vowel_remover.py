class VowelRemover():
    def __init__(self, text):
        self.text = text
        self.vowels = "aeiou"

    def remove_vowels(self):
        i = 0
        while i < len(self.text):
            if self.text[i].lower() in self.vowels:
                self.text = self.text[:i] + self.text[1:]
            i += 1
        return self.text
    
    