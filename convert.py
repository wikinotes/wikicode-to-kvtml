#!/usr/bin/env python
import sys
import re
import datetime

# Define a MalformedLine exception
class MalformedLine:
    pass # don't actually need to do anything

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

# Give it a line, will return the term and definition (tuple)
# If it can't, it will raise a MalformedLine exception
def format_line(line):
    """
    SUPPORTED FORMATS: (whitespace is not significant)
    *'''term''': definition (' or '' instead of ''' also possible)
    *'''term''' definition (same as above)
    ; term : definition
    *term: definition
    """
    # Check if it's in this format: *[''']term[''']: definition
    # Note this means the first : is significant
    # But after the first : there can be others, too
    if re.match("^\*[^\*:]+:", line):
        # The term is between * and :
        separator_index = line.find(':')
        term = line[1:separator_index]
        # Strip it of any single quotes (also whitespace, first)
        # Could be problematic think of workarounds for this later
        term = term.strip().strip("'")
        
        # Now get the definition - after separator to end of string
        definition = line[separator_index+1:].strip()
    elif re.match("^;[^;:]+:", line):
        # If it's in the format ; term : definition
        separator_index = line.find(':')
        term = line[1:separator_index]
        # Maybe put this code below so I don't have to repeat it
        # Later.
        term = term.strip().strip("'")
        definition = line[separator_index+1:].strip()
    else:
        # Not in any of the supported formats ... raise an exception
        # Might be a good idea to separate the formats later
        # Make them into a list or something
        # To make it easier to expand etc
        raise MalformedLine

    return term, definition

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

# Now we try to figure out which format it is ...
# Note that the format can differ between things in the file
# It would make sense if it had to be the same
# But honestly it's easier to code it this way

# For keeping track of which line we're on. Only needed for i = 0
i = 0
bad_lines = []

for line in lines:
    # Strip it of whitespace characters
    line = line.strip()
    if i == 0 and not need_first_line:
        # ignore the first line
        pass
    elif len(line) > 0:
        print line
        print len(line)
        try:
            entry = format_line(line) 
            print 'Term: ' + entry[0]
            print 'Definition: ' + entry[1]
        except MalformedLine:
            # Add this line number to the list of bad lines
            # Starts indexing from 0 of course
            bad_lines.append(i)
    else:
        # Blank lines, ignore
        pass
    i = i + 1

print "Conversion complete!"
# If we have any bad lines, display an error message
# But try to convert the rest of the file first
if len(bad_lines) > 0:
    print "However, there were %d lines that were not in a supported format: lines " % len(bad_lines),
    line_num = 1
    for bad_line in bad_lines:
        print bad_line + 1,
        # Do we need a comma?
        if line_num < len(bad_lines):
            print ',',
        line_num = line_num + 1

# Don't forget to close the file
input_file.close()
