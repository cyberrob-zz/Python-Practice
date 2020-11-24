myfile = open("fruits.txt")
print(myfile.read())

# Open and read a file and show only first 90 characters
with open("fruits.txt") as bear:
    contents = bear.read()
    
#print(contents[0:10])



def count_occurrances(char, filepath):
    with open(filepath) as file:
        contents = file.read()
        
    return contents.count(char)

print(count_occurrances(char='a', filepath='fruits.txt'))