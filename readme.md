[![Open Courses](http://www.wikinotes.ca/header.png)](http://www.wikinotes.ca)

Wikicode to KVTML Converter
===========================

What's a good snazzy name for this? Anyways, this is (will be) a Python script for converting from wikicode to kvtml (the format used by the open source word quiz / flash card software kwordquiz). Useful for quizzing yourself on stuff etc. Used extensively (or will be) on [Open Courses](http://www.wikinotes.ca). So you can make a dictionary-like list of things and then easily quiz yourself on it afterwards.

Usage
=====

You can either run it through

    ./convert.py inputfile outputfile

where convert.py has been set as executable, through `chmod +x convert.py`, or through

    python convert.py inputfile outputfile

if you don't feel like that doing that for some reason.

### inputfile ###

Has to be a text file (extensionless or with an extension, either is fine) and the contents have to be in wikicode format. The first line of the file should be the title, and should be in this format:

    =The title goes here=

The number of `=`'s is variable. Whitespace outside the `=`'s will be stripped.

If there is no title line (or something that the parser recognises as a title), it will prompt you to enter a title. If you enter nothing, the name of the output file will be used.

The format of the entries must be in one (or more) of several supported formats - see the Supported formats section for more.

### outputfile ###

If this filename does not have a .kvtml extension, it will automatically be given one.

Supported formats
=================

Here are the formats of the entries that are supported. Note that you can have multiple formats in one document (why would you, though?) because it was easier to code that way.

    *'''Term''': definition

    *'''Term''' definition (NOT CURRENTLY WORKING LOL)

    *Term: definition

    ; Term : definition

Note that whitespace and the number of quotation marks doesn't matter (except in the second case). Anywhere between 1 and 3 quotation marks is fine for the first format, and any number of quotation marks is fine for the third and fourth formats. Whitespace is also insignificant - whitespace on the edges will be stripped.

There may be more formats later, depending on how useful they are.

Examples
========

There will be sample wikicode provided as well as the expected output for the sample. Also, links to quizzes on wikinotes that were created using this software.

To do
=====
*   Needs snazzy name lol
*   More formats
*   Examples - convert samples
*   Encode special characters? e.g. < > & etc

About Open Courses
==================

We need some sort of boilerplate text for this ...
