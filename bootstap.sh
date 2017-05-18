host = $1

git submodule init
git submodule update

python bootstrap.py $host
make tags

cd ..

git clone https://github.com/stacks/stacks-tools
cd stacks-tools

python create.py
cd ..
mkdir stacks-website/database
chmod 0777 stacks-website/database
mv stacks-tools/stacks.sqlite stacks-website/database
chmod 0777 stacks-website/database/stacks.sqlite
chmod 0777 stacks-website/php/cache

cd stacks-website

ln -s css/stacks-editor.css js/EpicEditor/epiceditor/themes/editor/stacks-editor.css
ln -s css/stacks-preview.css js/EpicEditor/epiceditor/themes/editor/stacks-preview.css

cd ../stacks-tools
python update.py
python macros.py
mkdir ../stacks-website/data
python graphs.py