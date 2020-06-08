## 数据的关联性

RESTful 所操作的资源相对是离散的；而 GraphQL 的数据更有整体性。

首先我们需要给 User 定义 Schema (GraphQL 有一套完整的类型系统)：

type User {
id: ID!
name: String!
friends: [User]
}
假设我们在 Graph root 上只挂了一个 Node，叫 user:

It’s Graphs All the Way Down \*

它就像是一颗无限向下延伸的树。所以在我看来，GraphQL 更应该叫 TreeQL，当然在图论里，Tree 就是 Graph 也没毛病啦。需要注意的是，这也会引出 “N + 1 problem” 的话题——naive 的 GraphQL 服务端实现会让这段 query 变得异常慢！

怎么解决这个棘手的问题？心急的小伙伴请跳转到 6.1 N+1 问题！

4. GraphQL 能做到修改数据吗？
   看了上面的 query 的例子，你肯定很好奇，graphql 这种看上去好像只为查询而存在的语言，是不是有办法做到修改数据呢？

答案是：能。

仅仅为了使得 GraphQL 这个 data platform 变得更加完整，GraphQL 标准中加入了一种操作符，名为 mutation。因为我觉得这种设计确实比较一般，此处就不举例了，详情见：https://graphql.org/learn/queries/#mutations

## 5. GraphQL 与 RESTful 相比有什么优点？

1. 数据的关联性和结构化更好
   这一点已经在本文的第 3 个问题中有所描述。

1. 更易于前端缓存数据
   这个一般像 Relay 和 apollo-client 都替你做好了，如果你想了解它的缓存原理，请移步 GraphQL Caching

1. Versionless API
   相比于 RESTful 为了兼容新老客户端所添加的版本号，在 GraphQL 中，如果你需要服务端提供与以前不一样的行为，只需要修改 root Query 的定义，在上面额外添加你想要的 Node 即可。

1. 更健壮的接口
   不用再因为在缺乏沟通的情况下修改接口，而为系统埋下不稳定的定时炸弹。一切面向前端的接口都有强类型的 Schema 做保证，且完整类型定义因 introspection 完全对前端可见，一旦前端发送的 query 与 Schema 不符，能快速感知到产生了错误。

1. 令人期待的 subscription
   如何在浏览器中接受服务端的推送信息是个老生常谈的问题。从最初的轮询，到后来的 WebSocket。如今 GraphQL 也计划引入除了 query, mutation 以外的第三种操作符 subscription，以便于直接接受服务器推送数据。在 2015 年底 GraphQL 官方发布了一篇博文：Subscriptions in GraphQL and Relay 来介绍 subscription 在他们的 iOS 和 Android App 中的应用。可惜的是相关的代码仍未开源，目前开源社区能找到的解决方案目前只有 Apollo 社区为 Node.js 写的 graphql-subscriptions。

1. GraphQL 有什么缺点？
   说了 GraphQL 的那么多优点，那么它有没有缺点呢？当然也是有的。

6.1. N+1 问题
最大的问题莫过于：在实现 GraphQL 服务端接口时，很容易就能写出效率极差的代码，引起 “N+1 问题”。

什么是 N+1 问题？首先我们来举个简单的例子：

def get:
users = User.objects.all()
for user in users:
print(user.score)
这是一段简单的 python 代码，使用了 Django 的 QuerySet 来从数据库抓取数据。假设我们的数据库中有两张表 User 和 UserScore 这两张表的关系如下所示：

UML

由于用户的分数并没有保存在 User 表中，又因为 QuerySet 有 lazy load 的特性，所以在 for 循环中，每一次获取 user.score 都会查一次表，最终原本 1 次数据库查询能搞定的问题，却在不恰当的实现中产生了 N+1 次对数据库的访问。

相对于 RESTful，在 GraphQL 中更加容易引起 N+1 问题。主要是由于 GraphQL query 的逐层解析方式所引起的，关于 GraphQL 如何执行 query 的细节，可以参阅 Graphql Execution。

6.2. 如何解决在 GraphQL 中的 N + 1 问题？
以下解决方案仅针对关系型数据库，如果你的项目中使用的是 NoSQL，可能解决方案有较大差别。

针对一对一的关系（比如我上面举例中提到的这个 User 与 UserScore 的关系），在从数据库里抓取数据时，就将所需数据 join 到一张表里。别等着 ORM 框架替你懒加载那些你需要的数据。
针对多对一或者多对多的关系，你就要用到一个叫做 DataLoader 的工具库了。其中，Facebook 为 Node.js 社区提供了 DataLoader 的实现。DataLoader 的主要功能是 batching & caching，可以将多次数据库查询的请求合并为一个，同时已经加载过的数据可以直接从 DataLoader 的缓存空间中获取到。这个话题要是展开说也得写一篇新的文章了，此处不多赘述。
