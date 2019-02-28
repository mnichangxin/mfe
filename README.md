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

这里主要挑一些比较常问的点，逐步剖析。

#### HTML/CSS

1. 对 Web 语义化的理解

从 `HTML` 语义化和 `CSS` 语义化两方面回答：

* HTML 语义化：`HTML` 为网页文档内容提供上下文结构和含义。对于 `HTML` 体系而言，`Web` 语义化是指使用语义恰当的标签，使页面有良好的结构，让页面元素有含义，便于被浏览器、搜索引擎解析、利于 `SEO`。通常我们所说的 `HTML` 应该是完全脱离表现信息的，其中的标签应该都是语义化地定义了文档的结构。

* CSS 语义化：`CSS` 语义就是 `class` 和 `id` 命名的语义。`class` 属性作为 `HTML` 与`CSS` 衔接的纽带，其本意是用来描述元素内容的。指用易于理解的名称对 `html` 标签附加的 `class`或 `id` 命名。良好的 `CSS` 命名方式减少沟通调试成本，易于理解。

2. `<!Doctype html>` 的作用，严格模式和混杂模式

`<!Doctype html>` 是 `HTML5` 的文档声明。浏览器解析时到底使用严格模式还是混杂模式，与网页中的 DTD 直接相关。`HTML5` 中没有了 `DTD`，所以两者也没了区别，文档声明也简化成了`<!Doctype html>`。

3. 有哪些常见的 meta 标签

* `http-equiv` 属性：`<meta http-equiv='参数' content='参数变量值'>`：

```html
    1. <meta http-equiv=”Set-Cookie” content=”cookievalue=xxx; expires=Friday,12-Jan-2001 18:18:18 GMT; path=/”> // 如果网页过期，那么存盘的cookie将被删除。必须使用GMT的时间格式
    2. <meta http-equiv='expires' content='时间'> // 用于设定网页的到期时间。一旦网页过期，必须到服务器上重新传输
    3. <meta http-equiv=”Refresh” content=”5;URL”> // 告诉浏览器在【数字】秒后跳转到【一个网址】
    4. <meta http-equiv=”content-Type” content=”text/html; charset=utf-8″> // 设定页面使用的字符集
    <meta charset=”utf-8″> // 在HTML5中设定字符集的简写写法
    5. <meta http-equiv=”Pragma” content=”no-cache”> // 禁止浏览器从本地计算机的缓存中访问页面内容。访问者将无法脱机浏览
    6. <meta http-equiv=”Window-target” content=”_top”> // 用来防止别人在iframe(框架)里调用自己的页面
    7. <meta http-equiv='X-UA-Compatible' content='IE=edge,chrome=1'> // 强制浏览器按照特定的版本标准进行渲染。但不支持IE7及以下版本。如果是ie浏览器就用最新的ie渲染，如果是双核浏览器就用chrome内核
```
* name 属性：`<meta name='参数' content='具体的参数值'>`：

```html
    1. <meta name=”viewport” content=”width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no”> // 在移动设备浏览器上，禁用缩放（zooming）功能，用户只能滚动屏幕
    2. <meta name=”description” content=””> // 告诉搜索引擎，当前页面的主要内容是xxx
    3. <meta name=”keywords” content=””> // 告诉搜索引擎，当前页面的关键字。
    4. <meta name=”author” content=””> // 告诉搜索引擎，标注网站作者
    5. <meta name=”copyright” content=””> // 标注网站的版权信息
```

4. CSS 选择器的优先级、继承、层叠

* 通配选择符的权值：`0, 0, 0, 0`
* 标签的权值：`0, 0, 0, 1`
* 伪对象选择器的权值：`0, 0, 0, 1`
* 属性选择器的权值：`0, 0, 1, 0`
* 伪类选择器的权值：`0, 0, 1, 0`
* class 的权值：`0, 0, 1, 0`
* id 的权值：`0, 1, 0, 0`
* important 的权值：`1, 0, 0, 0`

记住这个公式：`important > 内联 > ID > 类 > 标签 | 伪类 | 属性选择器 > 伪对象 > 通配符 > 继承`

5. CSS 实现 div 水平垂直居中

基本从这几方面回答：

* 已知高度和宽度，绝对定位和负边距
* 未知高度或宽度，设置为内联元素并水平垂直居中
* CSS3 transform 属性
* Flex 布局

6. CSS 中 margin 属性的合并问题

* 父元素的上外边距和第一个子元素的上外边距
* 父元素的下外边距和最后一个子元素的下外边距
* 自己的上外边距会和自己的下外边距合并

7. CSS 清除浮动的方式

* 容器元素闭合标签前添加额外元素并设置 `clear: both`
* 父元素触发块级格式化上下文（BFC）
* 设置容器元素伪元素并设置 `clear: both`

8. CSS 创建 BFC 的方式

* 根元素
* 浮动元素（确切的说除了 `none` 以外的值）
* 绝对定位元素（position 取值 `absolute` 或 `fixed`）
* 非块盒的块容器（`inline-block`, `table-cell`, `table-caption`, `flex`, `inline-flex`）
* overflow 不为 `visible` 的块盒

#### JavaScript/Node.js

1. 基本数据类型和复杂数据类型有哪些

基本数据类型：`number`、`boolean`、`string`、`undifined`、`null`、`symbol`（ES6 新增）
复杂数据类型：`Object`

2. 数据类型的检测方式

最保险的方法 `Object.prototype.toString`，当 `toString` 被调用时：

* 如果 `this` 值是 `undefined`，就返回 `[object Undefined]`
* 如果 `this` 的值是 `null`，就返回 `[object Null]`
* 让 `O` 成为 `ToObject(this)` 的结果
* 让 `class` 成为 `O` 的内部属性 `[[Class]]` 的值
* 最后返回由 `'[object' ` 和 `class` 和 `']'` 三个部分组成的字符串

```js
    var class2type = {}
    // 生成 class2type 映射
    'Boolean Number String Function Array Date RegExp Object Error Null Undefined'.split(' ').map(function(item, index) {
        class2type['[object ' + item + ']'] = item.toLowerCase()
    })
    function getType(O) {
        return typeof O === 'object' || typeof O === 'function'
        ?
        class2type[Object.prototype.toString.call(O)] || 'object'
        :
        typeof O
    }
```

3. ['1', '2', '3'].map(parseInt) 的输出结果

`parseInt` 接收两个参数：`map` 函数的 `item` 和 `index`。即：

```js
    parseInt('1', 0) -> 1 // radix 为 10 进制
    parseInt('2', 1) -> NaN // radix 不在 2~36 之间
    parseInt('3', 2) -> NaN // 2 进制没有 3，只有 0 和 1
```
输出结果为：`1, NaN, NaN`

5. 事件处理对象中 `e.target` 和 `e.currentTarget` 的区别

* `e.target` 指向真正触发事件监听的对象
* `e.currentTarget` 指向添加事件监听的对象

6. `XSS` 和 `CSRF` 的区别，如何防范

[XSS 和 CSRF](https://juejin.im/post/5c6d142151882503b3271f4b)

7. `CommonJS` 和 `ES Module` 区别

* `CommonJS` 运行时确定依赖关系，`ES Module` 编译时确定依赖关系
* `CommonJS` 加载文件全部模块为对象，`ES Module` 只加载所需的模块
* `CommonJS` 输出的是值的拷贝，`ES Module` 输出的是值的引用

8. JavaScript 事件循环原理

在事件循环中，每进行一次循环操作称为 `tick`，每一次 `tick` 的任务处理模型是比较复杂的，但关键步骤如下：

* 在此次 `tick` 中选择最先进入队列的任务(`oldest task`)，如果有则执行(一次)
* 检查是否存在 `Microtasks`，如果存在则不停地执行，直至清空 `Microtasks Queue`
* 更新 `render`
* 主线程重复执行上述步骤

* `(macro)task` 主要包含：`script`(整体代码)、`setTimeout`、`setInterval`、`I/O`、`UI交互事件`、`postMessage`、`MessageChannel`、`setImmediate`(`Node.js` 环境)
* `microtask`主要包含：`Promise.then`、`MutaionObserver`、`process.nextTick`(`Node.js` 环境)

9. Promise all 方法和 race 方法区别

* `Promise.all`: 当所有的子 `Promise` 都完成，该 `Promise` 完成，返回值是全部值的数组；如果有任何一个失败，该 `Promise` 失败，返回值是第一个失败的子 `Promise` 的结果
* `Promise.race`: 当有一个子 `Promise` 都完成，该 `Promise` 完成

#### React

1. `React` 组件间通信方式

* 父传子：通过 `props`
* 子传父：父组件设置回调函数，子组件调用
* 子传子：一子组件向父组件传递，父组件再向另一子组件传递

#### Vue

1. 对 `MVVM` 的理解

在 `MVVM` 架构下，`View` 和 `Model` 之间并没有直接的联系，而是通过 `ViewModel` 进行交互，`Model` 和 `ViewModel` 之间的交互是双向的，因此 `View` 数据的变化会同步到 `Model`中，而 `Model` 数据的变化也会立即反应到 `View` 上

2. `Vue` 响应式原理（双向数据绑定原理）

* 数据劫持：`Vue` 数据双向绑定采用数据劫持结合 `发布者-订阅者模式` 的方式，通过`Object.defineProperty()` 来劫持各个属性的 `setter`，`getter`，在数据变动时发布消息给订阅者，触发相应监听回调。当把一个普通 `Javascript` 对象传给 `Vue` 实例来作为它的 `data` 选项时，`Vue` 将遍历它的属性，用 `Object.definePropert()` 将它们转为 `getter/setter`
* 源码分析：`Vue` 的数据双向绑定将 `MVVM` 作为数据绑定的入口，整合 `Observer`，`Compile` 和 `Watcher` 三者，通过 `Observer` 来监听自己的 `Model` 的数据变化，通过`Compile` 来解析编译模板指令，最终利用 `Watcher` 搭起 `Observer` 和 `Compile` 之间的通信桥梁，达到 `数据变化 —> 视图更新`；`视图交互变化（input） —> 数据 Model变更` 双向绑定效果

#### HTTP/HTTPS

1. HTTPS 密钥交换原理

#### 工具相关

#### 面经

记录了笔者的校招面试和正式工作后的社招面试：

[2018 前端校招面经合集](https://github.com/mnichangxin/mfe/blob/master/experience/2018%E5%89%8D%E7%AB%AF%E6%A0%A1%E6%8B%9B%E9%9D%A2%E7%BB%8F%E5%90%88%E9%9B%86.md)

[2019 字节跳动前端社招面经（一）](https://github.com/mnichangxin/mfe/blob/master/experience/2019%E5%AD%97%E8%8A%82%E8%B7%B3%E5%8A%A8%E5%89%8D%E7%AB%AF%E7%A4%BE%E6%8B%9B%E9%9D%A2%E7%BB%8F%EF%BC%88%E4%B8%80%EF%BC%89.md)

[2019 字节跳动前端社招面经（二）](https://github.com/mnichangxin/mfe/blob/master/experience/2019%E5%AD%97%E8%8A%82%E8%B7%B3%E5%8A%A8%E5%89%8D%E7%AB%AF%E7%A4%BE%E6%8B%9B%E9%9D%A2%E7%BB%8F%EF%BC%88%E4%BA%8C%EF%BC%89.md)

[2019 搜狐前端社招面经](https://github.com/mnichangxin/mfe/blob/master/experience/2019%E6%90%9C%E7%8B%90%E5%89%8D%E7%AB%AF%E7%A4%BE%E6%8B%9B%E9%9D%A2%E7%BB%8F.md)

[2019 小米前端社招面经](https://github.com/mnichangxin/mfe/blob/master/experience/2019%E5%B0%8F%E7%B1%B3%E5%89%8D%E7%AB%AF%E7%A4%BE%E6%8B%9B%E9%9D%A2%E7%BB%8F.md)

[2019 猿辅导前端社招面经](https://github.com/mnichangxin/mfe/blob/master/experience/2019%E7%8C%BF%E8%BE%85%E5%AF%BC%E5%89%8D%E7%AB%AF%E7%A4%BE%E6%8B%9B%E9%9D%A2%E7%BB%8F.md)

[2019 蚂蚁金服前端社招面经](https://github.com/mnichangxin/mfe/blob/master/experience/2019%E8%9A%82%E8%9A%81%E9%87%91%E6%9C%8D%E5%89%8D%E7%AB%AF%E7%A4%BE%E6%8B%9B%E9%9D%A2%E7%BB%8F.md)