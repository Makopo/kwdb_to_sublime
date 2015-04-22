This is the tool which fetches newest version of LSL/OSSL keywords from [kwdb](https://bitbucket.org/Sei_Lisa/kwdb) and convert it for use of [LSL/OSSL Bundle for Sublime Text](https://github.com/Makopo/sublime-text-lsl).

For now, simply run ./generate.sh script.

Actively developing.

Needed:

* curl
* perl
* python

Perl Modules:

* Text::Template
* Regexp::Assemble

Code Walkthrough:

The entry point is [generate.sh] (/Makopo/kwdb_to_sublime/blob/master/generate.sh). I here raw download the lsl2dfg/LSL2dfg.py engine and kwdb.xml from kwdb repository and then kick the engine to generate completion files and some contents in the syntax files. I have the templates in [inputs/] (/Makopo/kwdb_to_sublime/tree/master/inputs) folder and the modules in [lsl2dfg/lsloutputs/] (/Makopo/kwdb_to_sublime/tree/master/lsl2dfg/lsloutputs) folder, both of which will be passed to kwdb engine.

The tricky part is, as for the syntax files (*.tmLanguage), instead of creating the syntax files themselves, I actually create the perl scripts, with kwdb engine. After then, I run the resulting scripts to assemble the regex code with Regexp::Assemble. That's why [the generated codes] (/Makopo/sublime-text-lsl/blob/master/lsl.tmLanguage) are quite unreadable.
