#!/usr/bin/env bash
git submodule init
git submodule update
cd stacks-website
git submodule init
git submodule update
if [ ! -d "tex" ] ; then
	git clone https://github.com/stacks/stacks-project tex
fi

ln -s css/stacks-editor.css js/EpicEditor/epiceditor/themes/editor/stacks-editor.css > /dev/null 2>&1
ln -s css/stacks-preview.css js/EpicEditor/epiceditor/themes/editor/stacks-preview.css > /dev/null 2>&1


read -p "What hostname should be used?
" host

docker run -d -p 8080:80 -v $PWD:/var/www/html -t sadar/stacks-php > /dev/null 2>&1

python ../bootstrap.py ${host}

echo "Compiling tex"
rm -rf tex/tags/tmp/* > /dev/null 2>&1
docker run -v $PWD/tex:/tex -it sadar/stacks-texlive /bin/bash -c "cd tex && make tags"

cd ..
./initDB.sh

echo "Generating graphs"
cd stacks-tools
mkdir ../stacks-website/data > /dev/null 2>&1
python graphs.py
cd ..