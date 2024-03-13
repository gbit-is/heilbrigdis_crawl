

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd ..
cd ./tmp/starfsleyfi


grep "viewColumn2:_internalViewText" * | awk -F 'xspTextViewColumn' '{print $2}' | awk -F '>' '{print $2}' | awk -F '<' '{print $1}' | grep -v "nbsp" | sort | uniq  > ../kennitolur.txt
