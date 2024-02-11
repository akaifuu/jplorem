Requires pyperclip:


```
pip3 install pyperclip
```


Open zsh:


```
nano ~/.zshrc
  ```

Add this: 

```
jp() {
    /path/to/python/ /Path/to/file/jp.py "$1"
}
```
Now run ```jp [number]``` to return Japanese lorem ipsum in your terminal & copy to your clipboard.
