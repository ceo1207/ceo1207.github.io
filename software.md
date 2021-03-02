# 软件使用
## vscode
使用说明参见，[vscode官方文档](https://code.visualstudio.com/docs/editor/debugging)

快捷键及功能使用 切换英文使用快捷键
+ ctrl_shift_p 打开命令面板
+ ctrl_shift_f 搜索
+ ctrl_` 使用console 

如何使用调试功能  
安装相应功能的插件。Debuggers for java/xxx.  

***
## pycharm
+ ctrl 鼠标悬停 看函数参数
+ Ctrl + / 行注释
+ Ctrl + Numpad+ 展开
+ Ctrl + Numpad- 折叠
+ Ctrl + Shift + F 全局查找
+ Ctrl + Shift + R 全局替换
+ Ctrl + O override 父类方法
+ 代码导航
  + ctrl + h 继承结构
  + ctrl + g 行号跳转
  + Ctrl + F12 弹出文件结构
  + f11 设置书签 可以添加描述 , shift+f11 显示全部书签
+ 代码模板。
  Pycharm 提供的这个代码模板，可以说是相当实用的一个功能了。它可以在你新建一个文件时，按照你预设的模板给你生成一段内容，比如解释器路径，编码方法，作者详细信息等。常用变量`${DATE}${TIME}。
+ 可以复制代码后，与选中代码比较，右键-compare with clipboard
+ 查看函数调用者。右键-find usages 或者  ctrl+alt+h 查看caller 很有用

为什么总有快捷键失效？
1. 输入法、其他应用的快捷键有冲突。
2. 在该种语言下，无法使用该功能。
    > python环境下，无法使用块注释 The Code | "Comment with Block Comment" stays grayed out if pycharm does not know the syntax for adding comments for the particular file type.



***
## git
如何将已有文件，添加到git ignore。
1. git rm 使用`-r`递归作用到文件夹。

`git rm --cached filexample.txt`

2. .gitignore中添加该文件，可以使用图形化界面操作

discard local changes

`git checkout .`

