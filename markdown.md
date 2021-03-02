# markdown
## 环境准备
markdown推荐使用编辑器——typora（方便图片复制粘贴）、vscode。  

使用vscode写markdown。
+ 中文包设置。ctrl_shift_p  display language
+ 安装插件。markdown all in one, markdown preview github styling。

## 语法
md本质上是一种标记。有自身的标记语言，也可以混用部分的html标签。  
+ 段落换行。`/b/b/n` 没有空格的回车不会换行。
+ `**粗体**` `<b>粗体</b>` ctrl+b  
+ `*斜体*` `<em>斜体</em>` ctrl+i
+ ~~删除线~~  <u>下划线</u>
+ 分割线 `***`
+ `+ -` 无序列表
+ `1. 2.` 有序列表
+ 列表嵌套 
1. 第一项：
    - 第一项嵌套的第一个元素
    - 第一项嵌套的第二个元素
'''
2. 第二项：
    - 第二项嵌套的第一个元素
    - 第二项嵌套的第二个元素

+ 区块引用
> 区块引用 最外层
> > 第一层嵌套
> > > 第二层嵌套   

+ 代码片段

`print ()`

```javascript
$(document).ready(function () {
    alert('RUNOOB');
});
```

+ 链接。有多种方式可供选择。   
可以使用html的链接 `<a href=''>`  
<https://www.runoob.com>  
[亚马逊](https://www.amazon.cn/dp/B01IBZWTWW/ref=wl_it_dp_o_pC_nS_ttl?_encoding=UTF8&colid=BDXF90QZX6WX&coliid=I19EB97K0GNLW8)  
将元素切换为链接
```
<a href="https://play.google.com/store/apps/details?id=com.phodal.designiot">
  <img alt="Get it on Google Play"
       src="https://play.google.com/intl/en_us/badges/images/apps/en-play-badge-border.png" width="250" />
</a>
```
+ 使用图片  
可以使用html标签表示
`<img src="xxx" width="50%">`
+ 行内公式和块级公式，类似于latex
## 常用的markdown笔记实例
+ 每个文件只有一个一级标题。
+ 擅长使用列表（有序 or 无序）。
+ 标题不要超过三级。
+ 使用引用作为注释。
