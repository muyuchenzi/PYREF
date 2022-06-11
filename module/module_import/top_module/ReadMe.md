这个主要是在系统化变成或者形成模块的时候的使用

top_module

​		          ---inner

​							class_var

​							const_var #### list_alpha变量

​				   ---src

​							src_convert

​							src_func

​					main

这个模块结构通常做法是main作为程序入口，来引导所有的运算，但是如果inner import src 或者反过来会因为绝对引用与相对引用导致错误 ModuleNotFoundError: No module named '***'。

这里有两种解决办法

一、使用绝对引用来处理，import sys ，然后将top_module的文件夹路径添加到sys.path中，然后from top_module.inner.const_var import list_alpha即可，但是这样容易导致一旦文件路径出现问题，那么很多模块的引用都会有问题，一般如果是常规模块或者很小的代码可以这么处理。

二使用相对引用来处理，如果在src.convert 引入const_var，那么Python会认为src.convert是顶层模块，不存在层次结构，所以找不到相对路径。使用python -m top.src.convert 命令来进行处理

三最好的办法还是在模块的设计时候尽量保持最上面的结构，这样使用相对模块容易理解，易用性更好。