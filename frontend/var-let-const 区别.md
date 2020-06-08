一、变量提升: var
```javascript
console.log(a);//正常运行，控制台输出 undefined
var a = 1;
```

二、暂时性死区
```javascript
var tmp = 123;

if (true) {
	tmp = 'abc';//报错，Uncaught ReferenceError: tmp is not defined
	let tmp;
}
```


存在全局变量 tmp，但是块级作用域内 let 又声明了一个 tmp变量，导致后者被绑定在这个块级作用域中，所以在 let 声明变量前报错

三、重复声明

let 和 const 命令声明的变量不允许重复声明

五、作用域

第一种场景，内层变量覆盖外层变量。

```javascript
var tmp = new Date();//处于全局作用域

function f() {
  console.log(tmp);// undefined 处于函数作用域
  if (false) {
    var tmp = 'hello world';
  }
}

f(); // undefined 
```

let声明的全局变量不是全局对象的属性。这就意味着，你不可以通过window.变量名的方式访问这些变量。它们只存在于一个不可见的块的作用域中，这个块理论上是Web页面中运行的所有JS代码的外层块
