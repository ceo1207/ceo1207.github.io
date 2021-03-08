# 软件使用
## vscode
使用说明参见，[vscode官方文档](https://code.visualstudio.com/docs/editor/debugging)

快捷键及功能使用 切换英文使用快捷键
+ ctrl_shift_p 打开命令面板
+ ctrl_shift_f 搜索
+ ctrl_` 使用console 

### 如何使用调试功能  
安装相应功能的插件。Debuggers for xxx.  

+ python  
安装python插件即可调试

+ cpp  
  1. 安装 c/c++ 插件（必须）、C++ Intellisense（非必须）、Include Autocomplete（非必须
  2. mingw安装，配置环境变量 path
  3. 配置三个json文件到.vscode中

c_cpp_properties.json
```
   {
    "configurations": [
        {
            "name": "Win32",
            "includePath": [
                "${workspaceRoot}",
                "C:/mingw64/lib/gcc/x86_64-w64-mingw32/8.1.0/include/c++",
                "C:/mingw64/lib/gcc/x86_64-w64-mingw32/8.1.0/include/c++/x86_64-w64-mingw32",
                "C:/mingw64/lib/gcc/x86_64-w64-mingw32/8.1.0/include/c++/backward",
                "C:/mingw64/lib/gcc/x86_64-w64-mingw32/8.1.0/include",
                "C:/mingw64/lib/gcc/x86_64-w64-mingw32/8.1.0/include/c++/tr1",
                "C:/mingw64/x86_64-w64-mingw32/include"
            ],
            "defines": [
                "_DEBUG",
                "UNICODE",
                "__GNUC__=6",
                "__cdecl=__attribute__((__cdecl__))"
            ],
            "intelliSenseMode": "gcc-x64", // mingw64使用gcc的编译器
            "browse": {
                "path": [
                    "${workspaceRoot}",
                    "C:/mingw64/lib/gcc/x86_64-w64-mingw32/8.1.0/include/c++",
                    "C:/mingw64/lib/gcc/x86_64-w64-mingw32/8.1.0/include/c++/x86_64-w64-mingw32",
                    "C:/mingw64/lib/gcc/x86_64-w64-mingw32/8.1.0/include/c++/backward",
                    "C:/mingw64/lib/gcc/x86_64-w64-mingw32/8.1.0/include",
                    "C:/mingw64/lib/gcc/x86_64-w64-mingw32/8.1.0/include/c++/tr1",
                    "C:/mingw64/x86_64-w64-mingw32/include"
                ]
            },
            "compilerPath": "C:\\mingw64\\bin\\gcc.exe",
            "cStandard": "gnu17",
            "cppStandard": "gnu++14"
        }
    ],
    "version": 4
}
```

launch.json
```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "C++ Launch (GDB)", // 配置名称，将会在启动配置的下拉菜单中显示
            "type": "cppdbg", // 配置类型，这里只能为cppdbg
            "request": "launch", // 请求配置类型，可以为launch（启动）或attach（附加）
            "targetArchitecture": "x86", // 生成目标架构，一般为x86或x64，可以为x86, arm, arm64, mips, x64, amd64, x86_64
            "program": "${file}.exe", // 将要进行调试的程序的路径
            "miDebuggerPath": "C:\\mingw64\\bin\\gdb.exe", // miDebugger的路径，注意这里要与MinGw的路径对应
            "args": [], // 程序调试时传递给程序的命令行参数，一般设为空即可
            "stopAtEntry": false, // 设为true时程序将暂停在程序入口处，一般设置为false
            "cwd": "${workspaceRoot}", // 调试程序时的工作目录，一般为${workspaceRoot}即代码所在目录
            "externalConsole": true, // 调试时是否显示控制台窗口，一般设置为true显示控制台
            "preLaunchTask": "g++" // 调试会话开始前执行的任务，一般为编译程序，c++为g++, c为gcc
        }
    ]
}
```

tasks.json
```
{
    "version": "2.0.0",
    "command": "g++",
    "args": [
        "-g",
        "${file}",
        "-o",
        "${file}.exe"
    ], // 编译命令参数
    "problemMatcher": {
        "owner": "cpp",
        "fileLocation": [
            "relative",
            "${workspaceRoot}"
        ],
        "pattern": {
            "regexp": "^(.*)\\\\(.*):(\\d+):(\\d+):\\s+(warning|error):\\s+(.*)$",
            "file": 2,
            "line": 3,
            "column": 4,
            "severity": 5,
            "message": 6
        }
    }
}
```

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
