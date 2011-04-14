#!/usr/bin/env python
import sys
import re
import datetime

# Some helper methods
def make_header(title):
    # Get info needed for the date lol
    now = datetime.date.today()
    time_string = now.isoformat()
    
    # Returns the contents of the header as a string
    return '<?xml version="1.0" encoding="UTF-8"?>\n\
    <!DOCTYPE ktvml PUBLIC "kvtml2.dtd" "http://edu.kde.org/kvtml/kvtml2.dtd">\n\
    <kvtml version="2.0">\n\
    <information>\n\
        <generator>wikicode-to-kvtml-convertor (NEEDS A NAME)</generator>\n\
        <title>' + title + '</title>\n\
        <date>' + time_string + '</date>\n\
    </information>\n\
    <identifiers>\n\
        <identifier id="0">\n\
            <name>Term</name>\n\
            <locale>en</locale>\n\
        </identifier>\n\
        <identifier id=1">\n\
            <name>Definition</name>\n\
            <locale>en</locale>\n\
        </identifier>\n\
    </identifiers>\n\
    <entries>\n'

# Handle the command line arguments
# Give it an input file and an output file
# If the output filename is not *.kvtml, will make it so
if len(sys.argv) < 3:
    print 'Usage: ./convert.py inputfile outputfile'
    print 'Check the readme file for more info and where to get help'
    sys.exit(1)

# Now save the input and output file data
input_filename = sys.argv[1]
output_filename = sys.argv[2]


# First make sure the file exists and can be read
try:
    input_file = open(input_filename, 'r')
except IOError:
    sys.exit("The input file could not be read!")

# If the title is not saved in the file, prompt the user for it
# For the title to be saved, it must be the first thing in the file
# Like this: =Title= with that being the only thing on the line
# ==Title== or ===Title=== is also valid or even ==Title= etc
lines = input_file.readlines()
first_line = lines[0]
if re.match("^=+[^=]+=+$", first_line):
    # Just make it a substring of the first line
    # Also get rid of the trailing newline is there is one
    title = first_line.strip().strip('=')
    need_first_line = False # First line is the title
else:
    print 'The input file had no associated title.'
    print "Please enter a title (enter nothing for 'Untitled')."
    title = raw_input('Desired title: ')
    if len(title) == 0:
        # Default title - Untitled if none entered
        title = 'Untitled'
    need_first_line = True # As the first line is not the title

print make_header(title)
# For keeping track of which line we're on. Only needed for i = 0
i = 0
for line in lines:
    if i == 0 and not need_first_line:
        # ignore the first line
        pass
    else:
        print line
    i = i + 1

# Now try to figure out which format the wikicode is in

# Don't forget to close the file
input_file.close()
