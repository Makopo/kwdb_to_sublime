export OUTPUT_DIR=${CONVERTER_OUTPUT_DIR:-outputs}

rm lsl2dfg/LSL2dfg.py
rm kwdb.xml

mkdir -p $OUTPUT_DIR/snippets/events

curl https://kwdb.googlecode.com/hg/lsl2dfg/LSL2dfg.py -o lsl2dfg/LSL2dfg.py
curl https://kwdb.googlecode.com/hg/database/kwdb.xml -o kwdb.xml

python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_completions_constants -g sl -i inputs/LSLConstants.sublime-completions.in -o $OUTPUT_DIR/LSLConstants.sublime-completions
python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_completions_constants -g os -i inputs/OSSLConstants.sublime-completions.in -o $OUTPUT_DIR/OSSLConstants.sublime-completions
python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_completions_functions -g sl -i inputs/LSLFunctions.sublime-completions.in -o $OUTPUT_DIR/LSLFunctions.sublime-completions
python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_completions_functions -g os -i inputs/OSSLFunctions.sublime-completions.in -o $OUTPUT_DIR/OSSLFunctions.sublime-completions
python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_completions_events -g sl,os -i inputs/makesnippets.pl.in | perl
python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_tmLanguage -g sl -t LSL -i inputs/convertkeywords.pl.in | perl > "$OUTPUT_DIR/lsl.tmLanguage"
python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_tmLanguage -g os -t OSSL -i inputs/convertkeywords.pl.in | perl > "$OUTPUT_DIR/ossl.tmLanguage"

python lsl2dfg/LSL2dfg.py --version --grid=sl,os --database=kwdb.xml
