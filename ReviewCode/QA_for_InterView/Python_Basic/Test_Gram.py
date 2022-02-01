import tkinter
import tkinter.messagebox


def main():
    flag = True

    top = tkinter.Tk()
    top.geometry('240x160')
    top.title('小游戏')
    label = tkinter.Label(top, text='hello,world', font='Arial -32', fg='red')
    label.pack(expand=1)
    panel = tkinter.Frame(top)

    def change_label_text():
        nonlocal flag
        flag = not flag
        colr, msg = ('red', 'hello,world') if flag else(
            'blue', "goodbye,world")
        label.config(text=msg, fg=colr)

    def confim_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗？'):
            top.quit()

    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confim_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()

main()
