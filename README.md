# PDF Merge Tool for MacOS

Just a thin wrapper over the GhostScript command I discovered [here](http://hints.macworld.com/article.php?story=2003083122212228).

## Usage

Copy the script somewhere on your machine, then create an alias in your ~/.profile file by inserting the line, eg

alias pdfmerge='python3 ~/Tools/pdfmerge.py'

File names can be input with or without the .pdf extension. When you are finished entering file names, entering a blank space will prompt for the output name.

In its current form the files input must be in the current working directory.

## ToDo

PDF-insertion tool. Break up a document into before/after sections, then use the merging functionality to put it back together.

Starts to become a pdf-utility suite.
