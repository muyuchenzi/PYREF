## Python的多线程与多进程处理

### 概念

多线程：threading模块，利用单个CPU，由于IO和计算可以分开，计算不用等着IO.

多进程:mulitprocessing ，利用多个CPU来进行运算，真正实现并行处理

异步IO:asyncio，在单线程利用CPU 和IO同时执行的原理，实现函数异步执行



使用lock对资源加锁，防止访问冲突

使用Queue来对不同线程、进程进行数据通信

使用Pool来对线程、进程进行数据结果的存取与接收

### 多线程、多进程、多协程

![(E:\李震祥\PYGIT\PYref\ReviewCode\MD\data\多线程_进程_协程_对比.png)

详细笔记：

https://codeantenna.com/a/tTsAW8BYYc#subprocess_804