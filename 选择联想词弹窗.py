from tkinter import *
def associational_word_select_window(the_list):
    root = Tk()
    v = IntVar()

    words = []
    i = 0
    for word in the_list:
        words.append((word, i))
        i += 1
    words.append(('以上都不是', -1))    
    var = StringVar()
    var.set("为您联想的词语有：")
    textLabel = Label(root, textvariable=var, justify=LEFT)
    textLabel.pack(pady=5, side=TOP)
    
    for lang, num in words:
        b = Radiobutton(root,text=lang,variable=v,value=num,indicatoron=False,padx=30,pady=3)
        l = Label(root, textvariable=v)
        b.pack(anchor=W, fill=X)

    mainloop()
    if v.get() != -1:
        return words[v.get()][0]
    else:
        return 0

ws = ['词1','词2', '词3']
associational_word_select_window(ws)