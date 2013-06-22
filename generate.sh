OUTPUT_DIR=${CONVERTER_OUTPUT_DIR:-outputs}

rm lsl2dfg/LSL2dfg.py
rm kwdb.xml

curl https://kwdb.googlecode.com/hg/lsl2dfg/LSL2dfg.py -o lsl2dfg/LSL2dfg.py
curl https://kwdb.googlecode.com/hg/database/kwdb.xml -o kwdb.xml

python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_completions -g sl -t LSL -i inputs/LSL.sublime-completions.in -o "$OUTPUT_DIR/LSL.sublime-completions" -y
python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_completions -g os -t OSSL -i inputs/OSSL.sublime-completions.in -o "$OUTPUT_DIR/OSSL.sublime-completions" -y
python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_tmLanguage -g sl -t LSL -i inputs/convertkeywords.pl.in | perl > "$OUTPUT_DIR/LSL.tmLanguage"
python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_tmLanguage -g os -t OSSL -i inputs/convertkeywords.pl.in | perl > "$OUTPUT_DIR/OSSL.tmLanguage"
