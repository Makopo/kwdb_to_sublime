rm lsl2dfg/LSL2dfg.py
rm kwdb.xml

curl https://kwdb.googlecode.com/hg/lsl2dfg/LSL2dfg.py -o lsl2dfg/LSL2dfg.py
curl https://kwdb.googlecode.com/hg/database/kwdb.xml -o kwdb.xml

python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_completions -g sl -i inputs/LSL.sublime-completions.in -o outputs/LSL.sublime-completions -y
python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_completions -g os -i inputs/OSSL.sublime-completions.in -o outputs/OSSL.sublime-completions -y

echo "~~~~~~"
python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_events_valid -g sl -i inputs/convertkeywords.pl.in | perl 
echo "~~~~~~"
python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_functions_valid -g sl -i inputs/convertkeywords.pl.in | perl
echo "~~~~~~"
python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_constants_valid -g sl -i inputs/convertkeywords.pl.in | perl 
echo "~~~~~~"
python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_keywords_invalid -g sl -i inputs/convertkeywords.pl.in | perl 


echo "~~~~~~"
python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_keywords_invalid -g os -i inputs/convertkeywords.pl.in | perl
echo "~~~~~~"
python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_events_valid -g os -i inputs/convertkeywords.pl.in | perl
echo "~~~~~~"
python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_constants_valid -g os -i inputs/convertkeywords.pl.in | perl
echo "~~~~~~"
python lsl2dfg/LSL2dfg.py -u -d kwdb.xml -f sublime_functions_valid -g os -i inputs/convertkeywords.pl.in | perl
