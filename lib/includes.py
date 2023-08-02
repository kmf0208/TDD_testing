def includes(text):
    if text == "":
        raise Exception("no tasks")
    return True if "TODO" in text.upper() else False

"""
    
    
    if "TODO" in text.upper():
        return True
    else:
        return False
    
"""