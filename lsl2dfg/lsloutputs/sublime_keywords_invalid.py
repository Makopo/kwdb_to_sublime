#!/usr/bin/env python

import sys

def output(document, defaultdescs, databaseversion, infilename, outfilename, lang, tag):

  constants = []
  function = []
  for element in document:
    if 'status' in element and element['status'] != 'normal':
      if element["cat"] == "constant":
        constants.append(element)
      if element["cat"] == "function":
        function.append(element)

  if infilename is not None:
    inf = open(infilename, "r")
  else:
    inf = sys.stdin

  try:
    inputlines = inf.readlines()

  finally:
    if infilename is not None:
      inf.close()

  if outfilename is not None:
    outf = open(outfilename, "w")
  else:
    outf = sys.stdout

  try:
    for line in inputlines:
      if not line.startswith("<<< %s KEYWORDS >>>" % tag):
        outf.write(line)
      else:
        # Output all in the XML file's order
        for entry in constants:
          outf.write("$ra->add( '" + entry["name"] + "' );\n")
        for entry in function:
          outf.write("$ra->add( '" + entry["name"] + "' );\n")

  finally:
    if outfilename is not None:
      outf.close()


pass
