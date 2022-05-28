# Read text from a file, and count the occurrence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

print("**To get right results the file should be in the same folder as this python program, so you just need to specify the name of the file as argument of the function")
print("**The test was carry out with the file (story.txt), but it can be done with any file, just put it as argument of each function")


def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, "r") as openfile:
        read_file = openfile.read()
    return read_file


# *** example read-function in this case****:  read_file_content("story.txt")


def count_words(filename):
    text = read_file_content(filename)
    # [assignment] Add your code here
    
    # Identifying punctuations
    punctuations = """!()-{}[].,;:'"\<>/?@#$%^&_~*"""
    cleaned_text = ""
    
    # cleaning the text entered, 
    for char in text:
        if char not in punctuations:
            cleaned_text = cleaned_text + char
    
    # splitting it with split function
    split_text = cleaned_text.split()
    count = {}
    
    for i in split_text:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
            
    return count


# *** example count-function in this case****: count_words("story.txt")
