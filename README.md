Sublime-clipboardRound
======================
![image](https://badge.waffle.io/tgfjt/Sublime-clipboardRound.png?label=ready)

クリップボード履歴の再利用を行います for Sublime Text.

[README for English](https://github.com/tgfjt/Sublime-clipboardRound/blob/master/README.en.md)


This Plugin inspire from...
このプラグインは、下記vimプラグインの真似です。

* [vim-scripts/YankRing.vim](https://github.com/vim-scripts/YankRing.vim)
* [LeafCage/Yankround.vim](https://github.com/LeafCage/yankround.vim)

##用途

ペースト時に、クリップボード履歴を遡ってペーストし直すことが出来ます。

![image](https://raw.github.com/tgfjt/Sublime-clipboardRound/master/clipboardRound.gif)

##使い方

&lt;C-r&gt;&lt;C-p&gt;で貼り付けたテキストを前の履歴に、
&lt;C-r&gt;&lt;C-n&gt;で・次の履歴に置き換えます。カーソルを動かすと置き換えは確定されます。 

###初期コマンド

*  `Ctrl+R, Ctrl+P` 前の履歴に置換して貼り付け
*  `Ctrl+R, Ctrl+N` 次の履歴に置換して貼り付け
*  `Ctrl+R, Ctrl+L` 履歴の一覧表示（選択するとクリップボード内容を置換）
*  `Ctrl+R, Ctrl+D` 履歴のクリア
 

##Vintage Mode

`Preferences.sublime-settings`に下記設定を追加するとヤンクでも使えます。

```
"vintage_use_clipboard": true,
```
