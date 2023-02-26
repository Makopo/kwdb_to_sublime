#!/usr/bin/env python

import sys

def output(document, defaultdescs, databaseversion, infilename, outfilename, lang, tag):

  constants = []
  events = []
  functions = []
  invalids = []
  for element in document:
    if 'status' not in element or element['status'] == 'normal':
      if element["cat"] == "constant":
        constants.append(element)
      elif element["cat"] == "event":
        events.append(element)
      elif element["cat"] == "function":
        functions.append(element)
    else:
        invalids.append(element)

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
      if line.startswith("<<< CONSTANTS >>>"):
        for entry in constants:
          outf.write("$ra->add( '{0}' );\n".format(entry["name"]))
      elif line.startswith("<<< EVENTS >>>"):
        for entry in events:
          outf.write("$ra->add( '{0}' );\n".format(entry["name"]))
      elif line.startswith("<<< FUNCTIONS >>>"):
        for entry in functions:
          outf.write("$ra->add( '{0}' );\n".format(entry["name"]))
      elif line.startswith("<<< INVALIDS >>>"):
        for entry in invalids:
          outf.write("$ra->add( '{0}' );\n".format(entry["name"]))
      elif line.startswith("<<< VERSION >>>"):
        outf.write("my $version = '{0}';\n".format(databaseversion))
        outf.write("my $infile = 'templates/{0}.sublime-syntax.tmpl';\n".format(tag))
      else:
        outf.write(line)

  finally:
    if outfilename is not None:
      outf.close()

      # output for this function is perl script.
      # usually this function is called without outfilename, hence written in sysout.
      # after then perl will execute the contents in outf.

pass
