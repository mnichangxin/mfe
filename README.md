# 大前端技术栈与面试指南

**更多内容在整理中，敬请期待**

## 大前端技术栈

### Web 前端部分

### Android 部分

## 面试指南

### 计算机基础

* [数据结构和算法](https://github.com/CyC2018/CS-Notes/blob/master/docs/notes/%E7%AE%97%E6%B3%95.md)

* [操作系统](https://github.com/CyC2018/CS-Notes/blob/master/docs/notes/%E8%AE%A1%E7%AE%97%E6%9C%BA%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F.md)

* [计算机网络](https://github.com/CyC2018/CS-Notes/blob/master/docs/notes/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C.md)

### Web 前端部分

#### HTML/CSS

1. 对 Web 语义化的理解

从 HTML 语义化和 CSS 语义化两方面回答：

* HTML 语义化：`HTML` 为网页文档内容提供上下文结构和含义。对于 `HTML` 体系而言，`Web` 语义化是指使用语义恰当的标签，使页面有良好的结构，让页面元素有含义，便于被浏览器、搜索引擎解析、利于 `SEO`。通常我们所说的 `HTML` 应该是完全脱离表现信息的，其中的标签应该都是语义化地定义了文档的结构。

* CSS 语义化：`CSS` 语义就是 `class` 和 `id` 命名的语义。`class` 属性作为 `HTML` 与`CSS` 衔接的纽带，其本意是用来描述元素内容的。指用易于理解的名称对 `html` 标签附加的 `class`或 `id` 命名。良好的 `CSS` 命名方式减少沟通调试成本，易于理解。

2. CSS 选择器的优先级、继承、层叠

* 通配选择符的权值：`0, 0, 0, 0`
* 标签的权值：`0, 0, 0, 1`
* 伪对象选择器的权值：`0, 0, 0, 1`
* 属性选择器的权值：`0, 0, 1, 0`
* 伪类选择器的权值：`0, 0, 1, 0`
* class 的权值：`0, 0, 1, 0`
* id 的权值：`0, 1, 0, 0`
* important 的权值：`1, 0, 0, 0`

公式：`important > 内联 > ID > 类 > 标签 | 伪类 | 属性选择器 > 伪对象 > 通配符 > 继承`

3. CSS 实现 div 水平垂直居中

* 已知高度和宽度，绝对定位和负边距
* 未知高度或宽度，设置为内联元素并水平垂直居中
* CSS3 transform 属性
* Flex 布局

4. CSS 中 margin 属性的合并问题

* 父元素的上外边距和第一个子元素的上外边距
* 父元素的下外边距和最后一个子元素的下外边距
* 自己的上外边距会和自己的下外边距合并

5. CSS 清除浮动的方式

* 容器元素闭合标签前添加额外元素并设置 `clear: both`
* 父元素触发块级格式化上下文（BFC）
* 设置容器元素伪元素并设置 `clear: both`

6. CSS 创建 BFC 的方式

* 根元素
* 浮动元素（确切的说除了 `none` 以外的值）
* 绝对定位元素（position 取值 `absolute` 或 `fixed`）
* 非块盒的块容器（`inline-block`, `table-cell`, `table-caption`, `flex`, `inline-flex`）
* overflow 不为 `visible` 的块盒

#### JavaScript/Node.js

#### React

#### Vue

#### 工具相关

#### 面经

记录了笔者的校招面试和正式工作后的社招面试：

[2018 前端校招面经合集](https://github.com/mnichangxin/mfe/blob/master/experience/2018%E5%89%8D%E7%AB%AF%E6%A0%A1%E6%8B%9B%E9%9D%A2%E7%BB%8F%E5%90%88%E9%9B%86.md)

[2019 字节跳动前端社招面经（一）](https://github.com/mnichangxin/mfe/blob/master/experience/2019%E5%AD%97%E8%8A%82%E8%B7%B3%E5%8A%A8%E5%89%8D%E7%AB%AF%E7%A4%BE%E6%8B%9B%E9%9D%A2%E7%BB%8F%EF%BC%88%E4%B8%80%EF%BC%89.md)

[2019 字节跳动前端社招面经（二）](https://github.com/mnichangxin/mfe/blob/master/experience/2019%E5%AD%97%E8%8A%82%E8%B7%B3%E5%8A%A8%E5%89%8D%E7%AB%AF%E7%A4%BE%E6%8B%9B%E9%9D%A2%E7%BB%8F%EF%BC%88%E4%BA%8C%EF%BC%89.md)

[2019 搜狐前端社招面经](https://github.com/mnichangxin/mfe/blob/master/experience/2019%E6%90%9C%E7%8B%90%E5%89%8D%E7%AB%AF%E7%A4%BE%E6%8B%9B%E9%9D%A2%E7%BB%8F.md)

[2019 小米前端社招面经](https://github.com/mnichangxin/mfe/blob/master/experience/2019%E5%B0%8F%E7%B1%B3%E5%89%8D%E7%AB%AF%E7%A4%BE%E6%8B%9B%E9%9D%A2%E7%BB%8F.md)

[2019 猿辅导前端社招面经](https://github.com/mnichangxin/mfe/blob/master/experience/2019%E7%8C%BF%E8%BE%85%E5%AF%BC%E5%89%8D%E7%AB%AF%E7%A4%BE%E6%8B%9B%E9%9D%A2%E7%BB%8F.md)