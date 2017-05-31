#!/usr/bin/env bash
path_to_caddy=$(which caddy)
if [ -x "$path_to_caddy" ] ; then
	echo "Caddy bin already here: $path_to_caddy"
else
	curl https://getcaddy.com | bash
fi

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

./initDB.sh

mkdir ../stacks-website/data
python graphs.py