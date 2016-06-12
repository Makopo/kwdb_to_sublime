#!/usr/bin/env python

# sublime.py - This is a LSL2dfg.py output module that outputs all the
# functions, events and constants in the database with their signatures,
# types and values.

import sys

def output(document, defaultdescs, databaseversion, infilename, outfilename, lang, tag):

  def get_signature(element, elemtype):

    # get wiki url prefix
    urlprefix = "http://wiki.secondlife.com/wiki/"
    try:
        if not (element["grid"]).startswith("sl"):
          urlprefix = "http://opensimulator.org/wiki/"
    except KeyError:
        pass

    # function definition line
    if (elemtype == "f"):
      sign = "\"{name}\": \"Function: {type} <a href=\\\"{urlprefix}{name}\\\">{name}</a>("\
        .format(name=element["name"], type=element["type"] if element.has_key("type") else "void", \
                urlprefix=urlprefix)
      first = True
      if "params" in element:
        for param in element["params"]:
          if first:
            first = False
          else:
            sign = sign + ", "
          sign = sign + "{type} {name}".format(name=param["name"], type=param["type"])
      sign = sign + ");"
    elif (elemtype == "c"):
      sign = "\"{name}\": \"Constant: {type} <a href=\\\"{urlprefix}{name}\\\">{name}</a> = {value}"\
        .format(name=element["name"], type=element["type"], urlprefix=urlprefix, value="dummy")
    elif (elemtype == "e"):
      sign = "\"{name}\": \"Event: <a href=\\\"{urlprefix}{name}\\\">{name}</a>("\
        .format(name=element["name"], type=element["type"] if element.has_key("type") else "void", \
                urlprefix=urlprefix)
      first = True
      if "params" in element:
        for param in element["params"]:
          if first:
            first = False
          else:
            sign = sign + ", "
          sign = sign + "{type} {name}".format(name=param["name"], type=param["type"])
      sign = sign + "){ ; }"


    # status line
    try:
      status = element["status"]
      if not (status == "normal"):
        sign = sign + "<p style=\\\"color:#fff;background-color:#820124;\\\">{status}</p>".format(status=status)
    except KeyError:
      pass

    # description line
    try:
      desc = element["desc"]["en"]["text"].replace('\n', '<br>').replace('"', '\\\"')
      sign = sign + "<p>{desc}</p>".format(desc=desc)
    except KeyError:
      pass

    # statistics line
    if (elemtype == "f"):
      sign = sign + "<p>{delay} Forced Delay, {energy} Energy</p>"\
        .format(delay=float(element["delay"]), energy=float(element["energy"]))

    # final
    sign = sign + "\""
    return sign

  # starting main sequence here

  functions = []
  constants = []
  events = []
  for element in document:
    if element["cat"] == "function":
      functions.append(element)
    elif element["cat"] == "constant":
      constants.append(element)
    elif element["cat"] == "event":
      events.append(element)
  functions.sort(lambda x,y: cmp(x["name"],y["name"]))
  constants.sort(lambda x,y: cmp(x["name"],y["name"]))
  events.sort(lambda x,y: cmp(x["name"],y["name"]))

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
      if not line.startswith("<<< LINES >>>"):
        outf.write(line)
      else:
        outf.write("\t")
        outf.write(",\n\t".join([get_signature(element, "f") for element in functions]))
        outf.write(",\n\t")
        outf.write(",\n\t".join([get_signature(element, "c") for element in constants]))
        outf.write(",\n\t")
        outf.write(",\n\t".join([get_signature(element, "e") for element in events]))
        outf.write("\n")

  finally:
    if outfilename is not None:
      outf.close()

pass