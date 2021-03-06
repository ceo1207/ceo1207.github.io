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
