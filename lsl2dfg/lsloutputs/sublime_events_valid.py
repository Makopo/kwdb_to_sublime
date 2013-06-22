#!/usr/bin/env python

import sys

def output(document, defaultdescs, databaseversion, infilename, outfilename, lang, tag):

  events = []
  for element in document:
    if 'status' not in element or element['status'] == 'normal':
      if element["cat"] == "event":
        events.append(element)

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
        for entry in events:
          outf.write("$ra->add( '" + entry["name"] + "' );\n")

  finally:
    if outfilename is not None:
      outf.close()


pass
