### React 中 keys 的作用是什么？

Keys 是 React 用于追踪哪些列表中元素被修改、被添加或者被移除的辅助标识。

在开发过程中，我们需要保证某个元素的 key 在其同级元素中具有唯一性。在 React Diff 算法中 React 会借助元素的 Key 值来判断该元素是新近创建的还是被移动而来的元素，从而减少不必要的元素重渲染。此外，React 还需要借助 Key 值来判断元素与本地状态的关联关系，因此我们绝不可忽视转换函数中 Key 的重要性。

### 调用 setState 之后发生了什么？

在代码中调用 setState 函数之后，React 会将传入的参数对象与组件当前的状态合并，然后触发所谓的调和过程（Reconciliation）。经过调和过程，React 会以相对高效的方式根据新的状态构建 React 元素树并且着手重新渲染整个 UI 界面。在 React 得到元素树之后，React 会自动计算出新的树与老树的节点差异，然后根据差异对界面进行最小化重渲染。在差异计算算法中，React 能够相对精确地知道哪些位置发生了改变以及应该如何改变，这就保证了按需更新，而不是全部重新渲染。

setstate (funciton/ object, callback)

特性： 1.异步:react 通常会集齐一批需要更新的组件，然后一次性更新来保证渲染的性能

2.浅合并
object.assign 类似的 overwrite

更新机制：
pending queue 和 update queue

```
ReactComponent.prototype.setState = function (partialState, callback) {
    // 将 setState 事务放进队列中
    // this.updater 就是 ReactUpdateQueue, this 是组件的实例
    this.updater.enqueueSetState(this, partialState);
    if (callback) {
        this.updater.enqueueCallback(this, callback, 'setState');
    }
};
```

先 enqueue， 将新的 state 放入 queue
当前如果正处于创建/更新组件的过程，就不会立刻去更新组件，而是先把当前的组件放在 dirtyComponent 里，所以不是每一次的 setState 都会更新组件
用 isBatchingUpdates 标记当前是否出于批量更新

```
// 如果当前事务正在更新过程在中，则调用 callback，既 enqueueUpdate
if (alreadyBatchingUpdates) {
    return callback(a, b, c, d, e);
} else {
// 否则执行更新事务
    return transaction.perform(callback, null, a, b, c, d, e);
}
```

“异步”？
setState 只在合成事件和钩子函数中是“异步”的，在原生事件和 setTimeout 中都是同步的。
只是合成事件和钩子函数的调用顺序在更新之前，导致在合成事件和钩子函数中没法立马拿到更新后的值。

setState 并不是真正意义上的异步操作，它只是模拟了异步的行为。React 中会去维护一个标识（isBatchingUpdates），判断是直接更新还是先暂存 state 进队列。setTimeout 以及原生事件都会直接去更新 state，因此可以立即得到最新 state。而合成事件和 React 生命周期函数中，是受 React 控制的，其会将 isBatchingUpdates 设置为 true，从而走的是类似异步的那一套。

原声事件： addEventListener

react 更新事务 transaction 有 pre 和 post (类似 npm)
React 的事件系统和生命周期事务前后的钩子对 isBatchingUpdates 做了修改，其实就是在事务的前置 pre 内调用了 batchedUpdates 方法修改了变量为 true，然后在后置钩子又置为 false，然后发起真正的更新检测，而事务中异步方法运行时候，由于 JavaScript 的异步机制，异步方法（setTimeout 等）其中的 setState 运行时候，同步的代码已经走完，后置钩子已经把 isBatchingUpdates 设为 false，所以此时的 setState 会直接进入非批量更新模式，表现在我们看来成为了同步 SetState。

this.setState 首先会把 state 推入 pendingState 队列中。
然后将组建标记为 dirtyComponent。
React 中有事务的概念，最常见的就是更新事务，如果不在事务中，则会开启一次新的更新事务，更新事务执行的操作就是把组件标记为 dirty。
判断是否处于 batch update。
是的话，保存组建于 dirtyComponent 中，在事务的时候才会通过 ReactUpdates.flushBatchedUpdates 方法将所有的临时 state merge 并计算出最新的 props 及 state，然后将其批量执行，最后再关闭结束事务。
不是的话，直接开启一次新的更新事务，在标记为 dirty 之后，直接开始更新组件。因此当 setState 执行完毕后，组件就更新完毕了，所以会造成定时器同步更新的情况。

### react 生命周期函数

初始化阶段：

getDefaultProps:获取实例的默认属性
getInitialState:获取每个实例的初始化状态
componentWillMount：组件即将被装载、渲染到页面上
render:组件在这里生成虚拟的 DOM 节点
componentDidMount:组件真正在被装载之后

运行中状态：

componentWillReceiveProps:组件将要接收到属性的时候调用
shouldComponentUpdate:组件接受到新属性或者新状态的时候（可以返回 false，接收数据后不更新，阻止 render 调用，后面的函数不会被继续执行了）
componentWillUpdate:组件即将更新不能修改属性和状态
render:组件重新描绘
componentDidUpdate:组件已经更新
销毁阶段：

componentWillUnmount:组件即将销毁
shouldComponentUpdate 是做什么的，（react 性能优化是哪个周期函数？）
shouldComponentUpdate 这个方法用来判断是否需要调用 render 方法重新描绘 dom。因为 dom 的描绘非常消耗性能，如果我们能在 shouldComponentUpdate 方法中能够写出更优化的 dom diff 算法，可以极大的提高性能。

### fiber

asynchronous and atomic
high priority tasks like animation, user input can come before the low ones like data fetching from backend.

Suspense: pause at any time, or render a placeholder before the data is fetched, without hoisting the logic

### 为什么虚拟 dom 会提高性能?(必考)

虚拟 dom 相当于在 js 和真实 dom 中间加了一个缓存，利用 dom diff 算法避免了没有必要的 dom 操作，从而提高性能。

用 JavaScript 对象结构表示 DOM 树的结构；然后用这个树构建一个真正的 DOM 树，插到文档当中当状态变更的时候，重新构造一棵新的对象树。然后用新的树和旧的树进行比较，记录两棵树差异把 2 所记录的差异应用到步骤 1 所构建的真正的 DOM 树上，视图就更新了。

这就是所谓的 Virtual DOM 算法。包括几个步骤：用 JavaScript 对象结构表示 DOM 树的结构；然后用这个树构建一个真正的 DOM 树，插到文档当中当状态变更的时候，重新构造一棵新的对象树。然后用新的树和旧的树进行比较，记录两棵树差异把 2 所记录的差异应用到步骤 1 所构建的真正的 DOM 树上，视图就更新了

Virtual DOM 算法主要是实现上面步骤的三个函数：element，diff，patch。然后就可以实际的进行使用：// 1. 构建虚拟 DOM
var tree = el('div', {'id': 'container'}, [
el('h1', {style: 'color: blue'}, ['simple virtal dom']),
el('p', ['Hello, virtual-dom']),
el('ul', [el('li')])
])

// 2. 通过虚拟 DOM 构建真正的 DOM
var root = tree.render()
document.body.appendChild(root)

// 3. 生成新的虚拟 DOM
var newTree = el('div', {'id': 'container'}, [
el('h1', {style: 'color: red'}, ['simple virtal dom']),
el('p', ['Hello, virtual-dom']),
el('ul', [el('li'), el('li')])
])

// 4. 比较两棵虚拟 DOM 树的不同
var patches = diff(tree, newTree)
dfs 算法 比较 tag prop
生成 text, props, replace, reorder 的变化

// 5. 在真正的 DOM 元素上应用变更
patch(root, patches)

参考 如何理解虚拟 DOM?-zhihu

react diff 原理（常考，大厂必考）
把树形结构按照层级分解，只比较同级元素。
给列表结构的每个单元添加唯一的 key 属性，方便比较。
React 只会匹配相同 class 的 component（这里面的 class 指的是组件的名字）
合并操作，调用 component 的 setState 方法的时候, React 将其标记为 dirty.到每一个事件循环结束, React 检查所有标记 dirty 的 component 重新绘制.
选择性子树渲染。开发人员可以重写 shouldComponentUpdate 提高 diff 的性能。
参考：React 的 diff 算法

React 中 refs 的作用是什么？
Refs 是 React 提供给我们的安全访问 DOM 元素或者某个组件实例的句柄。我们可以为元素添加 ref 属性然后在回调函数中接受该元素在 DOM 树中的句柄，该值会作为回调函数的第一个参数返回：

class CustomForm extends Component {
handleSubmit = () => {
console.log("Input Value: ", this.input.value)
}
render () {
return (

<form onSubmit={this.handleSubmit}>
<input
type='text'
ref={(input) => this.input = input} />
<button type='submit'>Submit</button>
</form>
)
}
}
上述代码中的 input 域包含了一个 ref 属性，该属性声明的回调函数会接收 input 对应的 DOM 元素，我们将其绑定到 this 指针以便在其他的类函数中使用。另外值得一提的是，refs 并不是类组件的专属，函数式组件同样能够利用闭包暂存其值：

function CustomForm ({handleSubmit}) {
let inputElement
return (

<form onSubmit={() => handleSubmit(inputElement.value)}>
<input
type='text'
ref={(input) => inputElement = input} />
<button type='submit'>Submit</button>
</form>
)
}
如果你创建了类似于下面的 Twitter 元素，那么它相关的类定义是啥样子的？
<Twitter username='tylermcginnis33'>
{(user) => user === null
? <Loading />
: <Badge info={user} />}
</Twitter>
import React, { Component, PropTypes } from 'react'
import fetchUser from 'twitter'
// fetchUser take in a username returns a promise
// which will resolve with that username's data.
class Twitter extends Component {
// finish this
}
如果你还不熟悉回调渲染模式（Render Callback Pattern），这个代码可能看起来有点怪。这种模式中，组件会接收某个函数作为其子组件，然后在渲染函数中以 props.children 进行调用：

import React, { Component, PropTypes } from 'react'
import fetchUser from 'twitter'
class Twitter extends Component {
state = {
user: null,
}
static propTypes = {
username: PropTypes.string.isRequired,
}
componentDidMount () {
fetchUser(this.props.username)
.then((user) => this.setState({user}))
}
render () {
return this.props.children(this.state.user)
}
}
这种模式的优势在于将父组件与子组件解耦和，父组件可以直接访问子组件的内部状态而不需要再通过 Props 传递，这样父组件能够更为方便地控制子组件展示的 UI 界面。譬如产品经理让我们将原本展示的 Badge 替换为 Profile，我们可以轻易地修改下回调函数即可：

<Twitter username='tylermcginnis33'>
  {(user) => user === null
    ? <Loading />
    : <Profile info={user} />}
</Twitter>
展示组件(Presentational component)和容器组件(Container component)之间有何不同
展示组件关心组件看起来是什么。展示专门通过 props 接受数据和回调，并且几乎不会有自身的状态，但当展示组件拥有自身的状态时，通常也只关心 UI 状态而不是数据的状态。
容器组件则更关心组件是如何运作的。容器组件会为展示组件或者其它容器组件提供数据和行为(behavior)，它们会调用 Flux actions，并将其作为回调提供给展示组件。容器组件经常是有状态的，因为它们是(其它组件的)数据源。
类组件(Class component)和函数式组件(Functional component)之间有何不同
类组件不仅允许你使用更多额外的功能，如组件自身的状态和生命周期钩子，也能使组件直接访问 store 并维持状态
当组件仅是接收 props，并将组件自身渲染到页面时，该组件就是一个 '无状态组件(stateless component)'，可以使用一个纯函数来创建这样的组件。这种组件也被称为哑组件(dumb components)或展示组件
(组件的)状态(state)和属性(props)之间有何不同
State 是一种数据结构，用于组件挂载时所需数据的默认值。State 可能会随着时间的推移而发生突变，但多数时候是作为用户事件行为的结果。
Props(properties 的简写)则是组件的配置。props 由父组件传递给子组件，并且就子组件而言，props 是不可变的(immutable)。组件不能改变自身的 props，但是可以把其子组件的 props 放在一起(统一管理)。Props 也不仅仅是数据--回调函数也可以通过 props 传递。
何为受控组件(controlled component)
在 HTML 中，类似 <input>, <textarea> 和 <select> 这样的表单元素会维护自身的状态，并基于用户的输入来更新。当用户提交表单时，前面提到的元素的值将随表单一起被发送。但在 React 中会有些不同，包含表单元素的组件将会在 state 中追踪输入的值，并且每次调用回调函数时，如 onChange 会更新 state，重新渲染组件。一个输入表单元素，它的值通过 React 的这种方式来控制，这样的元素就被称为"受控元素"。

### 何为高阶组件(higher order component)

高阶组件是一个以组件为参数并返回一个新组件的函数。HOC 运行你重用代码、逻辑和引导抽象。最常见的可能是 Redux 的 connect 函数。除了简单分享工具库和简单的组合，HOC 最好的方式是共享 React 组件之间的行为。如果你发现你在不同的地方写了大量代码来做同一件事时，就应该考虑将代码重构为可重用的 HOC。

### 为什么建议传递给 setState 的参数是一个 callback 而不是一个对象

因为 this.props 和 this.state 的更新可能是异步的，不能依赖它们的值去计算下一个 state。

### 除了在构造函数中绑定 this，还有其它方式吗

你可以使用属性初始值设定项(property initializers)来正确绑定回调，create-react-app 也是默认支持的。在回调中你可以使用箭头函数，但问题是每次组件渲染时都会创建一个新的回调。

### (在构造函数中)调用 super(props) 的目的是什么

在 super() 被调用之前，子类是不能使用 this 的，在 ES2015 中，子类必须在 constructor 中调用 super()。传递 props 给 super() 的原因则是便于(在子类中)能在 constructor 访问 this.props。

### 应该在 React 组件的何处发起 Ajax 请求

在 React 组件中，应该在 componentDidMount 中发起网络请求。这个方法会在组件第一次“挂载”(被添加到 DOM)时执行，在组件的生命周期中仅会执行一次。更重要的是，你不能保证在组件挂载之前 Ajax 请求已经完成，如果是这样，也就意味着你将尝试在一个未挂载的组件上调用 setState，这将不起作用。在 componentDidMount 中发起网络请求将保证这有一个组件可以更新了。

### webpack

是由 nodejs 编写的前端资源加载/打包工具，由 nodejs 提供了强大的文件处理，IO 能力。

loader: 是一个 nodejs 函数模块， 传入 resource file 或者 sourceMap json 结果，读取文件，将文件处理为 String 或者 Buffer 格式，然后传给 compiler 或者下一个 loader.
plugin: 是能够参与到 compilation process 的自定义函数，通过 hook 到每一个编译（compiler）中，触发关键事件或处理。

## 我们应当将 AJAX 请求放到 componentDidMount 函数中执行，主要原因有下：

React 下一代调和算法 Fiber 会通过开始或停止渲染的方式优化应用性能，其会影响到 componentWillMount 的触发次数。对于 componentWillMount 这个生命周期函数的调用次数会变得不确定，React 可能会多次频繁调用 componentWillMount。如果我们将 AJAX 请求放到 componentWillMount 函数中，那么显而易见其会被触发多次，自然也就不是好的选择。

如果我们将 AJAX 请求放置在生命周期的其他函数中，我们并不能保证请求仅在组件挂载完毕后才会要求响应。如果我们的数据请求在组件挂载之前就完成，并且调用了 setState 函数将数据添加到组件状态中，对于未挂载的组件则会报错。而在 componentDidMount 函数中进行 AJAX 请求则能有效避免这个问题。

## 描述事件在 React 中的处理方式。

为了解决跨浏览器兼容性问题，您的 React 中的事件处理程序将传递 SyntheticEvent 的实例，它是 React 的浏览器本机事件的跨浏览器包装器。

这些 SyntheticEvent 与您习惯的原生事件具有相同的接口，除了它们在所有浏览器中都兼容。有趣的是，React 实际上并没有将事件附加到子节点本身。

React 将使用单个事件监听器监听顶层的所有事件。这对于性能是有好处的，这也意味着在更新 DOM 时，React 不需要担心跟踪事件监听器。

## createElement 和 cloneElement 有什么区别？

React.createElement():JSX 语法就是用 React.createElement()来构建 React 元素的。它接受三个参数，第一个参数可以是一个标签名。如 div、span，或者 React 组件。第二个参数为传入的属性。第三个以及之后的参数，皆作为组件的子组件。

React.createElement(
type,
[props],
[...children]
)
React.cloneElement()与 React.createElement()相似，不同的是它传入的第一个参数是一个 React 元素，而不是标签名或组件。新添加的属性会并入原有的属性，传入到返回的新元素中，而就的子元素奖杯替换。

React.cloneElement(
element,
[props],
[...children]
)

## React 中有三种构建组件的方式

React.createClass()、ES6 class 和无状态函数。

## new 操作符干了什么

创建了一个空对象。
把所创建的空对象的* proto *指向构造函数的 prototype
执行构造函数中的代码，构造函数中的 this 指向对象
返回该对象（除非构造函数中返回一个对象或者函数）

## 概述下 React 中的事件处理逻辑

为了解决跨浏览器兼容性问题，React 会将浏览器原生事件（Browser Native Event）封装为合成事件（SyntheticEvent）传入设置的事件处理器中。这里的合成事件提供了与原生事件相同的接口，不过它们屏蔽了底层浏览器的细节差异，保证了行为的一致性。另外有意思的是，React 并没有直接将事件附着到子元素上，而是以单一事件监听器的方式将所有的事件发送到顶层进行处理。这样 React 在更新 DOM 的时候就不需要考虑如何去处理附着在 DOM 上的事件监听器，最终达到优化性能的目的。

## 如何告诉 React 它应该编译生产环境版本？

通常情况下我们会使用 Webpack 的 DefinePlugin 方法来将 NODE_ENV 变量值设置为 production。编译版本中 React 会忽略 propType 验证以及其他的告警信息，同时还会降低代码库的大小，React 使用了 Uglify 插件来移除生产环境下不必要的注释等信息。

## react 组件的划分业务组件技术组件？

根据组件的职责通常把组件分为 UI 组件和容器组件。
UI 组件负责 UI 的呈现，容器组件负责管理数据和逻辑。
两者通过 React-Redux 提供 connect 方法联系起来。
简述 flux 思想
Flux 的最大特点，就是数据的"单向流动"。

## 同源策略

它是浏览器的一种约定，脚本只允许访问同一站点的资源，协议相同，域名相同，端口号相同，就是同一站点

在浏览器中，<script> 、<img> <link>等标签都可以跨域加载资源，cookie 和 ajax 都不能跨域加载资源

## redux

用户访问 View
View 发出用户的 Action
Dispatcher 收到 Action，要求 Store 进行相应的更新
Store 更新后，发出一个"change"事件
View 收到"change"事件后，更新页面

了解 redux 么，说一下 redux 把
redux 是一个应用数据流框架，主要是解决了组件间状态共享的问题，原理是集中式管理，主要有三个核心方法，action，store，reducer，工作流程是 view 调用 store 的 dispatch 接收 action 传入 store，reducer 进行 state 操作，view 通过 store 提供的 getState 获取最新的数据，

flux 也是用来进行数据操作的，有四个组成部分 action，dispatch，view，store，工作流程是 view 发出一个 action，派发器接收 action，让 store 进行数据更新，更新完成以后 store 发出 change，view 接受 change 更新视图。Redux 和 Flux 很像。主要区别在于 Flux 有多个可以改变应用状态的 store，在 Flux 中 dispatcher 被用来传递数据到注册的回调事件，但是在 redux 中只能定义一个可更新状态的 store，redux 把 store 和 Dispatcher 合并,结构更加简单清晰
新增 state,对状态的管理更加明确，

通过 redux，流程更加规范了，减少手动编码量，提高了编码效率，同时缺点时当数据更新时有时候组件不需要，但是也要重新绘制，有些影响效率。一般情况下，我们在构建多交互，多数据流的复杂项目应用时才会使用它们

## redux 有什么缺点

一个组件所需要的数据，必须由父组件传过来，而不能像 flux 中直接从 store 取。
当一个组件相关数据更新时，即使父组件不需要用到这个组件，父组件还是会重新 render，可能会有效率影响，或者需要写复杂的 shouldComponentUpdate 进行判断。

## ajax 跨域

1
JSONP 方式解决跨域问题
jsonp 解决跨域问题是一个比较古老的方案(实际中不推荐使用),这里做简单介绍(实际项目中如果要使用 JSONP,一般会使用 JQ 等对 JSONP 进行了封装的类库来进行 ajax 请求)

实现原理
JSONP 之所以能够用来解决跨域方案,主要是因为 <script> 脚本拥有跨域能力

2
CORS 请求原理
CORS 是一个 W3C 标准，全称是"跨域资源共享"（Cross-origin resource sharing）。它允许浏览器向跨源服务器，发出 XMLHttpRequest 请求，从而克服了 AJAX 只能同源使用的限制。

## 概述下 React 中的事件处理逻辑

为了解决跨浏览器兼容性问题，React 会将浏览器原生事件（Browser Native Event）封装为合成事件（SyntheticEvent）传入设置的事件处理器中。这里的合成事件提供了与原生事件相同的接口，不过它们屏蔽了底层浏览器的细节差异，保证了行为的一致性。另外有意思的是，React 并没有直接将事件附着到子元素上，而是以单一事件监听器的方式将所有的事件发送到顶层进行处理。这样 React 在更新 DOM 的时候就不需要考虑如何去处理附着在 DOM 上的事件监听器，最终达到优化性能的目的。

## 类组件和函数式组件有何不同

this, state, 生命周期

## new

创建一个空对象
将所创建的对象的** proto **指向构造函数的 prototype
实行构造函数中的代码，构造函数中的 this 指向该对象
返回该对象（除非构造函数中返回了一个对象或者函数）

## 请求报文:

请求行, 请求头部, 空行, 请求体

## 一个程序至少有一个进程,一个进程至少有一个线程.

线程的划分尺度小于进程，使得多线程程序的并发性高。
另外，进程在执行过程中拥有独立的内存单元，而多个线程共享内存，从而极大地提高了程序的运行效率。
线程在执行过程中与进程还是有区别的。每个独立的线程有一个程序运行的入口、顺序执行序列和程序的出口。但是线程不能够独立执行，必须依存在应用程序中，由应用程序提供多个线程执行控制。
从逻辑角度来看，多线程的意义在于一个应用程序中，有多个执行部分可以同时执行。但操作系统并没有将多个线程看做多个独立的应用，来实现进程的调度和管理以及资源分配。这就是进程和线程的重要区别。

进程是具有一定独立功能的程序关于某个数据集合上的一次运行活动,进程是系统进行资源分配和调度的一个独立单位.
线程是进程的一个实体,是 CPU 调度和分派的基本单位,它是比进程更小的能独立运行的基本单位.线程自己基本上不拥有系统资源,只拥有一点在运行中必不可少的资源(如程序计数器,一组寄存器和栈),但是它可与同属一个进程的其他的线程共享进程所拥有的全部资源.
一个线程可以创建和撤销另一个线程;同一个进程中的多个线程之间可以并发执行.

进程和线程的主要差别在于它们是不同的操作系统资源管理方式。进程有独立的地址空间，一个进程崩溃后，在保护模式下不会对其它进程产生影响，而线程只是一个进程中的不同执行路径。

定义方面：进程是程序在某个数据集合上的一次运行活动；线程是进程中的一个执行路径。（进程可以创建多个线程）
角色方面：在支持线程机制的系统中，进程是系统资源分配的单位，线程是 CPU 调度的单位。
资源共享方面：进程之间不能共享资源，而线程共享所在进程的地址空间和其它资源。同时线程还有自己的栈和栈指针，程序计数器等寄存器。
独立性方面：进程有自己独立的地址空间，而线程没有，线程必须依赖于进程而存在。
开销方面。进程切换的开销较大。线程相对较小。（前面也提到过，引入线程也出于了开销的考虑。）
