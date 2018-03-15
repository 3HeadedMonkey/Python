print("Let's practice everything")
print('You\'d need to know \'bout excapes with \\that do:')
print('\n newlines and\ttabs.')

poem = """
Razu pewniego, jak wieść dawna niesie
niedżwiedż stary napotkał lisa w lesie
wiedząc co mu grozi lis szczwany
świetnie był na wszystko przygotowany
rzecze do niedżwiedzia 'Mój przyjacielu!
takich jak ja jest tu w lesie niewielu,
jeśli mnie pożresz dziadki moje zginą,
\ti żona i wnuki
\ti czyją to winą?
niedżwiedziowi nużącza była lisia mowa
westchnął do niebia \n\t\tzjadł lisa bez słowa
"""

print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans /1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
#remember that the function returns values to variables accordingly to their position
beans, jars, crates = secret_formula(start_point)
#remember about this way of formatign a string
print("With a starting point of:{}".format(start_point))
#it is an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point /=10

print("We can also do that this way:")
formula = secret_formula(start_point)
#this is an easy wat to apply a list to a format string
print("We'd have {} beans,{} jars, and {} crates.".format(*formula))
