echo 'Clearing existing build'
rm -rf ./dist
./env/bin/python -m build

echo 'Build done'