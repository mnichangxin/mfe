由于 TLS/SSL 协议位于应用层和传输层 TCP 协议之间。TLS 粗略的划分又可以分为 2 层：
靠近应用层的握手协议 TLS Handshaking Protocols
靠近 TCP 的记录层协议 TLS Record Protocol

在 TLS 握手过程中，客户端和服务器将共同执行以下操作：
指定将使用的 TLS 版本（TLS 1.0、1.2、1.3 等）
确定将使用哪些加密套件。
通过服务器的公钥和 SSL 证书颁发机构的数字签名来验证服务器的身份
握手完成后，生成会话密钥以使用对称加密

1. WebSocket 与 HTTP 的关系

### 相同点

都是一样基于 TCP 的，都是可靠性传输协议。
都是应用层协议。

### 不同点

WebSocket 是双向通信协议，模拟 Socket 协议，可以双向发送或接受信息。HTTP 是单向的。
WebSocket 是需要握手进行建立连接的。

2. css

translator
transition：渐变
transform: 动画

3. es6
   async
   await

4. 降级访问
   HTTPS 与 HTTP 核心区别

上面讲到 Socket 是什么？，有一点我忘了讲：
HTTPS 与 HTTP 核心区别在于两点：
把 HTTP 下层的传输协议由 TCP/IP 换成了 SSL/TLS
收发报文不再使用 Socket API，而是调用专门的安全接口。
具体区别：
HTTPS 协议需要到 CA 申请证书，一般免费证书很少，需要交费。
HTTP 是超文本传输协议，信息是明文传输，HTTPS 则是具有安全性的 ssl 加密传输协议。
HTTP 和 https 使用的是完全不同的连接方式，用的端口也不一样,前者是 80,后者是 443。
HTTP 的连接很简单,是无状态的。HTTPS 协议是由 SSL+HTTP 协议构建的可进行加密传输、身份认证的网络协议，比 HTTP 协议安全。

1. HTTP 报文结构是怎样的？
   对于 TCP 而言，在传输的时候分为两个部分:TCP 头和数据部分。

而 HTTP 类似，也是 header + body 的结构，具体而言:

起始行 + 头部 + 空行 + 实体

GET /home HTTP/1.1
HTTP/1.1 200 OK

http/1.1 规定了以下请求方法(注意，都是大写):

GET: 通常用来获取资源
HEAD: 获取资源的元信息
POST: 提交数据，即上传数据
PUT: 修改数据
DELETE: 删除资源(几乎用不到)
CONNECT: 建立连接隧道，用于代理服务器
OPTIONS: 列出可对资源实行的请求方法，用来跨域请求
TRACE: 追踪请求-响应的传输路径

## HTTP1.1 如何解决 HTTP 的队头阻塞问题？

什么是 HTTP 队头阻塞？
阻塞后面请求的处理。这就是著名的 HTTP 队头阻塞问题。

1. 并发连接
   对于一个域名允许分配多个长连接，Chrome 中是 6 个。
   但其实，即使是提高了并发连接，还是不能满足人们对性能的需求。
2. 域名分片

xss:
恶意注册 script 嵌入

csrf：
骗取 cookie 信任

### 函数去抖和函数节流

函数去抖（debounce）：
当调用函数 n 秒后，才会执行该动作，若在这 n 秒内又调用该函数则取消前一次并重新计算执行时间（频繁触发的情况下，只有足够的空闲时间，才执行代码一次）

```javascript
function debounce(delay, cb) {
  let timer;
  return function () {
    if (timer) clearTimeout(timer);
    timer = setTimeout(function () {
      cb();
    }, delay);
  };
}
```

函数节流（throttle）：
函数节流的基本思想是函数预先设定一个执行周期，当调用动作的时刻大于等于执行周期则执行该动作，然后进入下一个新周期（一定时间内 js 方法只跑一次。比如人的眨眼睛，就是一定时间内眨一次）

```javascript
function throttle(cb, delay) {
  let startTime = Date.now();
  return function () {
    let currTime = Date.now();
    if (currTime - startTime > delay) {
      cb();
      startTime = currTime;
    }
  };
}
```

## 箭头（Arrow）函数

这是 ES6 中最令人激动的特性之一。=>不只是关键字 function 的简写，它还带来了其它好处。箭头函数与包围它的代码共享同一个 this,能很好的解决 this 的指向问题。

## 宏/微

• 遇到 setTimeout 分发到宏任务 Event Queue 中
• 遇到 process.nextTick， promise 的 then 丢到微任务 Event Queue 中

promise 直接输出
