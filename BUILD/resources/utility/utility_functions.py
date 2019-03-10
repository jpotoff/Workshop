import os
import re
import fnmatch

def replace_text(filename, text_to_search, replacement_text):
    '''This function will replace <text_to_search> text with
    <replacement_text> string in <filename>'''
    with open(filename, 'r') as file:
        filedata = file.read()
    filedata = filedata.replace(text_to_search, replacement_text)
    with open(filename, 'w') as file:
        file.write(filedata)

def FindParameter(filename, keyword):
    '''This function will find the keyword in the <filename> and
    return the second value'''
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith(keyword):
                line = re.sub(' +', ' ', line).strip()
                return line.split(' ')[1]

def replace_textWithFile(filename, text_to_search, replacement_file):
    '''This function will replace <text_to_search> text with
    <replacement_file> file in <filename>'''
    with open(replacement_file, 'r') as file:
        for line in file:
            replace_text(filename, text_to_search, line.upper() + text_to_search)

    replace_text(filename, text_to_search, '')

# clean all files except the ones with filepattern
def CleanDir(filepattern):
    for file in os.listdir('.'):
        if not fnmatch.fnmatch(file, filepattern):
            os.remove(file)