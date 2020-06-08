在当前的微任务没有执行完成时，是不会执行下一个宏任务的。

所以就有了那个经常在面试题、各种博客中的代码片段：

setTimeout(\_ => console.log(4))

new Promise(resolve => {
resolve()
console.log(1)
}).then(\_ => {
console.log(3)
})

console.log(2)
setTimeout 就是作为宏任务来存在的，而 Promise.then 则是具有代表性的微任务，上述代码的执行顺序就是按照序号来输出的。

## css, js 阻塞 html

## 箭头函数和普通函数的区别

普通函数：
(1).this 总是代表它的直接调用者
(2).在默认情况下，没找到直接调用者，this 指向 window
(3).在严格模式下，没有直接调用者的函数中的 this 是 undefined
(4).使用 call，apply，bind 绑定，this 指的是绑定的对象

箭头函数：
(1).在使用 => 定义函数的时候，this 的指向是定义时所在的对象，而不是使用时所在的对象，bind()、call()、apply()均无法改变指向
(2).不能用做构造函数，也就是说不能使用 new 命令，否则就会抛出一个错误
(3).不能使用 arguments 对象，但是可以使用…rest 参数
(4).不能使用 yield 命令
(5).没有原型属性

作者：\_前端小弟
链接：https://www.jianshu.com/p/4840a90751e1
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
