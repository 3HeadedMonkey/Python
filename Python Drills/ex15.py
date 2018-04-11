from sys import argv
# load arguments from the terminal and set them accordingly to the values
script, filename = argv
# set the content of filename as a string named txt
txt = open(filename)

print(f"Here's your file {filename}:")
#read the txt and print it to the terminal
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
