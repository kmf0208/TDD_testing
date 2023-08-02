import math

class GrammarStats:
    def __init__(self):
        self.passed_text = 0
        self.failed_check = 0
  
    def check(self, text):
   
        if not text:
            raise Exception('it is not be empty')
        
        condition = text[0].isupper() and text[-1] in ".!?"
        if condition:
            self.passed_text += 1
            return True
        else:
            self.failed_check += 1
            return False
  
    def percentage_good(self):
        total = int(self.passed_text) + int(self.failed_check)

        if total == 0:
            return 0
        percentage = (self.passed_text / total) * 100
        return math.ceil(percentage)
        

        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.