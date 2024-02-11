Requires pyperclip:
pip3 install pyperclip

Open zsh:
nano ~/.zshrc  

Add this: 
jp() {
    /path/to/python/ /Path/to/file/jp.py "$1"
}

Now you can run "jp [number]" and it will return lorem ipsum text but for Japanese in your terminal and copy it to your clipboard.