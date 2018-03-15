import sys
script, encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
            print_line(line, encoding, errors)
            return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    # strip() deletes all whitespaces within the document,
    # including, tabs, spaces, newlines
    next_lang = line_strip()
    # encode() and decode() uses the type of unicode (here its utf-8) to encode/decode the string)
    # type of standard is included as a string 'utf-8'
    raw_bytes = lext.lang.encode(encoding, errors=errors)
    cooked_string =  raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)

#what the hell is 'errors=errors', pourque?
