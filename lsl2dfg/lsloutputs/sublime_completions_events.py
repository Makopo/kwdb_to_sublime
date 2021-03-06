#!/usr/bin/env python

import sys
import codecs

def output(document, defaultdescs, databaseversion, infilename, outfilename, lang, tag):

  def get_signature(element):
    sign = element["name"] + "("
    first = True
    if "params" in element:
      cnt = 1;
      for param in element["params"]:
        if first:
          first = False
        else:
          sign = sign + ", "
        sign = sign + "{type} ${{{idx}:{name}}}".format(idx=cnt, name=param["name"], type=param["type"])
        cnt += 1;
    sign = sign + ")"
    return sign

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
    outf = codecs.open(outfilename, "w", "utf-8")
  else:
    outf = sys.stdout

  try:
    for line in inputlines:
      if line.startswith("<<< LINES >>>"):
        outf.write("my $version = '{0}';\n".format(databaseversion))
        for element in document:
          if 'status' not in element or element['status'] == 'normal':
            grid = element["grid"] if "grid" in element else "sl os"
            if element["cat"] == "event":
                outf.write("&print_snippet($template_events, 'events', $version, '{0}', '{1}', '{2}');\n"
                 .format(grid, element["name"], get_signature(element)))
      else:
        outf.write(line)

  finally:
    if outfilename is not None:
      outf.close()

      # output for this function is perl script.
      # usually this function is called without outfilename, hence written in sysout.
      # after then perl will execute the contents in outf.

pass
