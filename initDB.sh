echo "Initializing database"
cd stacks-tools
rm -f stacks.sqlite
python create.py
cd ..
rm -rf stacks-website/database 
mkdir stacks-website/database
chmod 0777 stacks-website/database
mv stacks-tools/stacks.sqlite stacks-website/database
chmod 0777 stacks-website/database/stacks.sqlite
chmod 0777 stacks-website/php/cache

cd stacks-tools
python update.py
python macros.py