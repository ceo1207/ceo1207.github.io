# about git
## gitbook
**功能**

编辑、发布电子书

**使用说明**

+ 安装node.js
+ 安装gitbook
    ```
    //使用淘宝镜像
    npm install --registry=https://registry.npm.taobao.org
    // 或者直接使用 cnpm
    npm install -g cnpm --registry=https://registry.npm.taobao.org
    npm install -g gitbook-cli
    npm install -g gitbook-pdf 
    // 输出pdf
    gitbook pdf ./图书目录
    // 输出本地静态网页 localhost访问
    gitbook serve ./图书目录
    ```


## github pages。

**如何使用github pages**  
github创建同名repository。
+ 可以显示gitbook
+ 可以使用Jekyll编辑生成blog
+ 可以显示md, 网址换掉就可以了。简单易用，最后用gitbook可以生成pdf或者静态网站。
https://xxx.github.io/test.md 改为 https://xxx.github.io/test


github pages缺点  
不支持动态内容，博客必须都是静态网页；
每小时更新不超过 10 次；
博客不能被百度索引。

## git
+ 如何解决github访问速度慢的问题

    https://zhuanlan.zhihu.com/p/109466869  
    使用站长工具检测，将ttl小的ip存入hosts，然后更新dns   
    `ipconfig /flushdns`

    有的时候，不能不直接用ip访问，`http://ip`

+ 如何将已有文件，添加到git ignore。
  1. git rm 使用`-r`递归作用到文件夹。

    `git rm --cached filexample.txt`

  2. .gitignore中添加该文件，可以使用图形化界面操作

+ discard local changes

    `git checkout .`

+ 如何为文件夹添加本地git管理
 
    ```
    git init
    git add . 
    ```

