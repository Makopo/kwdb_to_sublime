export OUTPUT_DIR=${CONVERTER_OUTPUT_DIR:-outputs}

rm lsl2dfg/LSL2dfg.py
rm kwdb.xml

# mkdir $OUTPUT_DIR/snippets/functions
# mkdir $OUTPUT_DIR/snippets/constants
# mkdir $OUTPUT_DIR/snippets/events

curl https://kwdb.googlecode.com/hg/lsl2dfg/LSL2dfg.py -o lsl2dfg/LSL2dfg.py
curl https://kwdb.googlecode.com/hg/database/kwdb.xml -o kwdb.xml

python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_completions -g sl -t LSL -i inputs/makesnippets.pl.in | perl
python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_completions -g os -t OSSL -i inputs/makesnippets.pl.in | perl
python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_tmLanguage -g sl -t LSL -i inputs/convertkeywords.pl.in | perl > "$OUTPUT_DIR/lsl.tmLanguage"
python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_tmLanguage -g os -t OSSL -i inputs/convertkeywords.pl.in | perl > "$OUTPUT_DIR/ossl.tmLanguage"

python lsl2dfg/LSL2dfg.py --version --grid=sl,os --database=kwdb.xml
