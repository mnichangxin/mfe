webpack 的打包原理

识别入口文件
通过逐层识别模块依赖(Commonjs、amd 或者 es6 的 import，webpack 都会对其进行分析，来获取代码的依赖)
webpack 做的就是分析代码，转换代码，编译代码，输出代码
最终形成打包后的代码

对于 loader，它是一个转换器，将 A 文件进行编译形成 B 文件，这里操作的是文件，比如将 A.scss 转换为 A.css，单纯的文件转换过程

plugin 是一个扩展器，它丰富了 webpack 本身，针对是 loader 结束后，webpack 打包的整个过程，它并不直接操作文件，而是基于事件机制工作，会监听 webpack 打包过程中的某些节点，执行广泛的任务

1. 打包

```javascript
__JSONP
(function() {
    var moduleList = [
        function(require, module, exports) {
            require.ensure['1']
            .then(res => {}

            )
        },
        function(require, module, exports) {

        }
    ];

    var moduleDepIdList = [
        {'./moduleA' : 1},
        {}
    ];

    function require(id, parentId) {
        currentModuleId == undefined? moduleDepIdList[parentId][id] : parentId;
        moduleFunc = moduleList[currentModuleId];
        module = {exports: {}}
        moduleFunc((id) => require(id, currentModuleId), module, module.exports);
        return module.exports


    window.__JSONP = function(chunkId, moduleFunc) {
        var currentChunkStatus = cache[chunkId];
        var resolve = currentChunkStatus[0];
        // 导出结果进入resolve, 输出then
        var module = {export:{}};
        moduleFunc(require, module, module.exports);
        resolve(module.exports);

    }
    // 异步加载 ensure jsonp
    require.ensure = function(chunkId, parentId) {
        var currentModuleId = moduleDepIdList[parentId][chunkId];
        var currentChunkStatus = cache[currentModuleId];
        // 首次加载
        if (currentChunkStatus == undefined){
            var $script = documment.createElement['script'];
            script.src = chunckId + currentChunkStatus + '.js';
            document.body.appendChild($script);
            var promise = new Promise(function(resolve) {
                // 执行函数， 提前resolve 掉， resolve 执行就去then
                var chunkCache = [resolve];
                // 已经开始加载 避免2次加载
                chunkCache.status = true;
                cache[currentModuleId] = chunkCache;
            });
            // resolve 状态存储
            // 缓存promise 实例
            cache[currentModuleId].push(promise);
            return promise;
        }

        if (currentChunkStatus.status) {
            return currentChunkStatus[1];
        }
        return

    }


    require(0);

})
```

## reference

https://webpack.wuhaolin.cn/1%E5%85%A5%E9%97%A8/1-7%E6%A0%B8%E5%BF%83%E6%A6%82%E5%BF%B5.html

https://webpack.wuhaolin.cn/
