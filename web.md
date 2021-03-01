可以自己内网搭建GitLab服务

自动化构建工具， 用来自动完成压缩代码和运行测试等重复性任务


使用工具
 推荐从 Visual Studio Code 开始，免费且提供实时预览和代码提示。

需要测试服务器
 如果你只是从本地文件运行示例，一些浏览器（包括 Chrome）将不会运行异步请求

 它们具有服务端代码。 服务器端语言（如 PHP 或 Python）需要一个特殊的服务器来解释代码并提供结果。

使用python 架设本地的简易服务器
```
＃如果上面返回的Python版本是3.X 
python -m http.server 
＃如果上面返回的Python版本是2.X 
python -m SimpleHTTPServer
```

您可以通过转到localhost:8000Web浏览器中的URL来访问此服务器

需要访问特定资源时，使用url访问，`http://localhost:8000/index2.html`

Python的SimpleHTTPServer模块是有用的，但它不知道如何运行用PHP或Python等语言编写的代码。

安装vscode的live server插件也可以实现网页的实时预览，跟自动保存的时间有关

Python Flask示例python3 python-example.py，然后在您的浏览器中打开 localhost:5000 查看

要运行Node.js（JavaScript）服务器端代码，您可以直接使用Node或选择构建于其上的框架。Express是一个不错的选择 - 请参阅Express Web Framework（Node.js / JavaScript）。

要运行PHP服务器端代码，您需要一个可以解释PHP的服务器设置。本地PHP测试的好选择是MAMP（Mac和Windows），  AMPPS（Mac，Windows，Linux）和LAMP（Linux，Apache，MySQL和PHP / Python / Perl）。这些是完整的包，创建本地设置，允许您运行Apache服务器，PHP和MySQL数据库。


颜色选择工具 https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_Colors/Color_picker_tool  

字体选择平台 http://www.google.com/fonts

使用vs code的标签补全
设置vscode中取消勾选

vscode自动预览html页面