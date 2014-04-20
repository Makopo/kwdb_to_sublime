#!/usr/bin/env python

import sys

def output(document, defaultdescs, databaseversion, infilename, outfilename, lang, tag):

  def get_signature(parameter_format, element):
    sign = element["name"] + "("
    first = True
    if "params" in element:
      cnt = 1;
      for param in element["params"]:
        if first:
          first = False
        else:
          sign = sign + ", "
        sign = sign + parameter_format.format(idx=cnt, name=param["name"], type=param["type"])
        cnt += 1;
    sign = sign + ")"
    return sign

  constants = []
  events = []
  functions = []
  for element in document:
    if 'status' not in element or element['status'] == 'normal':
      if element["cat"] == "constant":
        constants.append(element)
      elif element["cat"] == "event":
        events.append(element)
      elif element["cat"] == "function":
        functions.append(element)

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
        outf.write("my $cat = 'constants';\n")
        for entry in constants:
          # print entry
          outf.write("&print_snippet($template, $cat, $version, '{0}', '{1}', '', '{2}');\n"
           .format(entry["grid"] if entry.has_key("grid") else "sl os", entry["name"], entry["type"]))
      elif line.startswith("<<< EVENTS >>>"):
        outf.write("my $cat = 'events';\n")
        for entry in events:
          # print entry
          outf.write("&print_snippet($template, $cat, $version, '{0}', '{1}', '{2}');\n"
           .format(entry["grid"] if entry.has_key("grid") else "sl os", entry["name"], get_signature("{type} ${{{idx}:{name}}}", entry)))
      elif line.startswith("<<< FUNCTIONS >>>"):
        outf.write("my $cat = 'functions';\n")
        for entry in functions:
          # print entry
          outf.write("&print_snippet($template, $cat, $version, '{0}', '{1}', '{2}', '{3}');\n"
           .format(entry["grid"] if entry.has_key("grid") else "sl os", entry["name"], get_signature("${{{idx}:{type} {name}}}", entry), 
            entry["type"] if entry.has_key("type") else "void"))
      elif line.startswith("<<< COMMON >>>"):
          outf.write("my $version = '{0}';\n".format(databaseversion))
      else:
        outf.write(line)

  finally:
    if outfilename is not None:
      outf.close()

      # output for this function is perl script.
      # usually this function is called without outfilename, hence written in sysout.
      # after then perl will execute the contents in outf.

pass
