#coding=utf-8
import win32con
import win32clipboard as w

def getText(): #读取剪切板
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d
def setText(aString): #写入剪切板
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, aString)
    w.CloseClipboard()


if __name__ =='__main__':
    a= '666'
    setText(a.encode('gb2312'))
    d = getText()
    print (d)

