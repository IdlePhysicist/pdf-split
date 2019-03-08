#!/bin/bash
echo 'Install PDF Split'
echo 'Checking if GhostScript is installed...'
if command -v gs > /dev/null; then
    echo 'GhostScript installed continuing'
else
    echo 'GhostScript not installed...'
    echo 'Checking if HomeBrew is installed'
    if ! command -v brew > /dev/null; then
        echo 'Installing HomeBrew'
        /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    fi
    echo 'Installing GhostScript'
    brew install gs
fi

if [[ -d "PDFSplit.app" ]]; then
    echo "Copying PDFSplit.app to /Applications/"
    cp -r PDFSplit.app /Applications/.
fi

echo 'Symlinking pdfsplit.py to /usr/local/bin/'
path=$PWD
chmod +x pdfsplit.py
cd /usr/local/bin/
ln -s $path/pdfsplit.py pdfsplit

echo 'Finished installing'# & linking'
echo 'Enjoy 😊'
