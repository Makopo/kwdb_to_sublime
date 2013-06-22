rm lsl2dfg/LSL2dfg.py
rm kwdb.xml

curl https://kwdb.googlecode.com/hg/lsl2dfg/LSL2dfg.py -o lsl2dfg/LSL2dfg.py
curl https://kwdb.googlecode.com/hg/database/kwdb.xml -o kwdb.xml

python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_completions -g sl -i inputs/LSL.sublime-completions.in -o outputs/LSL.sublime-completions -y
python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_completions -g os -i inputs/OSSL.sublime-completions.in -o outputs/OSSL.sublime-completions -y
python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_tmLanguage -g sl -i inputs/convertkeywords.pl.in | perl > outputs/LSL.tmLanguage
python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_tmLanguage -g os -i inputs/convertkeywords.pl.in | perl > outputs/OSSL.tmLanguage
