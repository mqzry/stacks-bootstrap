#!/usr/bin/env bash
git submodule init
git submodule update
cd stacks-website
git submodule init
git submodule update
if [ ! -d "tex" ] ; then
	git clone git://github.com/stacks/stacks-project tex
fi

ln -s css/stacks-editor.css js/EpicEditor/epiceditor/themes/editor/stacks-editor.css
ln -s css/stacks-preview.css js/EpicEditor/epiceditor/themes/editor/stacks-preview.css

python ../bootstrap.py $1

cd tex
rm -rf tags/tmp/*
make tags
cd ../..

./initDB.sh

cd stacks-tools
mkdir ../stacks-website/data
python graphs.py