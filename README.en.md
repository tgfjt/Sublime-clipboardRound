Sublime-clipboardRound
======================

Reuse Clipboard History for Sublime Text.

This Plugin inspire from...

* [vim-scripts/YankRing.vim](https://github.com/vim-scripts/YankRing.vim)
* [LeafCage/Yankround.vim](https://github.com/LeafCage/yankround.vim)

##Use for what

You can paste again from previous or following clipboard history.

![image](https://raw.github.com/tgfjt/Sublime-clipboardRound/master/clipboardRound.gif)

##How to Use

* re-paste Pre clipboard with &lt;C-r&gt;&lt;C-p&gt;
* re-paste Next clipboard with &lt;C-r&gt;&lt;C-n&gt;

###Default Commands

*  `Ctrl+R, Ctrl+P` Paste and Replace by previous Clipboard
*  `Ctrl+R, Ctrl+N` Paste and Replace by next Clipboard
*  `Ctrl+R, Ctrl+L` Show Clipboard History at Quick Panel (and Choice)
*  `Ctrl+R, Ctrl+D` Clear Clipboard History
 

##Vintage Mode

Use with "Y"ank(or "D"elete) on `Preferences.sublime-settings`

```
"vintage_use_clipboard": true,
```
