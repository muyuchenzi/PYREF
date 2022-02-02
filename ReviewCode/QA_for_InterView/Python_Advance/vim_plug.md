## VIM模式-----普通模式



**三种模式 主要是解决插入时的位置问题，在光标前面还是后面，在上一行还是下一行的问题**

切换快捷键 insert与normal切换 jj[ESC] 与 i相互切换。

![](E:\李震祥\PYGIT\PYref\ReviewCode\QA_for_InterView\Python_Advance\Data\img\vim模式.jpg)

### 光标移动

上下左右

![](E:\李震祥\PYGIT\PYref\ReviewCode\QA_for_InterView\Python_Advance\Data\img\上下左右.jpg)

单词之间移动

![](E:\李震祥\PYGIT\PYref\ReviewCode\QA_for_InterView\Python_Advance\Data\img\单词光标移动.png)

多行之间移动

![](E:\李震祥\PYGIT\PYref\ReviewCode\QA_for_InterView\Python_Advance\Data\img\行列光标移动.png)

代码块快速移动

!![](E:\李震祥\PYGIT\PYref\ReviewCode\QA_for_InterView\Python_Advance\Data\img\光标查找.png)

单词多选处理

![](E:\李震祥\PYGIT\PYref\ReviewCode\QA_for_InterView\Python_Advance\Data\img\光标动作范围.png)

![](E:\李震祥\PYGIT\PYref\ReviewCode\QA_for_InterView\Python_Advance\Data\img\动作组合.png)



![](E:\李震祥\PYGIT\PYref\ReviewCode\QA_for_InterView\Python_Advance\Data\img\操作符.png)

根据上面的可以 操作符+动作来进行处理

ci< 可以对 string="<this is a test>" 对<>进行修改；同样也可以di<、da< 、ya< 等等组合来进行对一个字符串进行处理，相对于鼠标非常方便。

p 粘贴

u 撤销动作+操作符

ciw 选中单词删除并进入插入模式

yiw 选中并复制单词

diw 选中并删除单词

ci< 选中被<>包围的单词并修改

ndd/cc/yy 向下删除/修改/复制n行,包括当前行

d/c/yf{char} 删除/修改/复制到向后的char字符

d/c/y^/$ 删除/修改/复制到开头/结尾切换大小写

## ~ 将光标下的字母改变大小写



![](E:\李震祥\PYGIT\PYref\ReviewCode\QA_for_InterView\Python_Advance\Data\img\切换大小写.png)



3~ 将光标位置开始的3个字母改变大小写

g~ 改变当前行字母的大小写

gUU 将当前行的字母改成大写

guu 将当前行的字母改成小写

gUaw(gUiw) 将光标下的单词改成大写

guaw(guiw) 将光标下的单词改成小写

![](E:\李震祥\PYGIT\PYref\ReviewCode\QA_for_InterView\Python_Advance\Data\img\终极.png)