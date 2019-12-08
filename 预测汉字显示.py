from  tkinter import *
root = Tk()
def show(predict):
    root.title('预测汉字')
    lb = Label(root,text=predict,\
            bg='#fff',\
            fg='black',\
            font=('华文新魏',80),\
            width=5,\
            height=2,\
            relief=RAISED)
    lb.pack()
    root.mainloop()

show('与')