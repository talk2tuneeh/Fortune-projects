

from tkinter import *
import math as m
root = Tk()
root.title("Scientific Calculator")
e = Entry(root, width=50, borderwidth=5, relief=RIDGE, fg="White", bg="Black")
e.grid(row=0, column=0, columnspan=5, padx=10, pady=15)

def click(to_print):
    old=e.get()
    e.delete(0, END)
    e.insert(0, old+to_print)
    return

def sc(event):
    key=event.widget
    text=['text']
    no=e.get()
    result=''
    if text=='deg':
        result=str(m.degrees(float(no)))
    if text=='sin':
        result=str(m.sin(float(no)))
    if text=='cos':
        result=str(m.cos(float(no)))
    if text=='tan':
        result=str(m.tan(float(no)))
    if text=='lg':
        result=str(m.log10(float(no)))
    if text=='ln':
        result=str(m.log(float(no)))
    if text=='sqrt':
        result=str(m.sqrt(float(no)))
    if text=='x!':
        result=str(m.factorial(float(no)))
    if text=='1/x':
        result=str(1/(float(no)))
    if text=='pi':
        if no=="":
            result=str(m.pi)
        else:
            result=str(float(no) * m.pi)
    if text=='e':
        if no=="":
            result=str(m.e)
        else:
            result=str(m.e ** float(no))

    e.delete(0, END)
    e.insert(0, result)


def clear():
    e.delete(0, END)
    return

def bksps():
    current=e.get()
    length=len(current)-1
    e.delete(length, END)

def evaluate():
    ans=e.get()
    ans=eval(ans)
    e.delete(0, END)
    e.insert(0, ans)

ac = Button(root, text="C", padx=29, pady=10, relief=RAISED, fg="White", bg="Dark Red", command=lambda: clear())
bksp = Button(root, text="Bksp", padx=19, pady=10, relief=RAISED, fg="White", bg="Red", command=lambda: bksps())
mod = Button(root, text="mod", padx=19, pady=10, relief=RAISED, fg="White", bg="Black", command=lambda: click("%"))
par1st = Button(root, text="(", padx=30, pady=10, relief=RAISED, fg="White", bg="Black", command=lambda: click("("))
par2nd = Button(root, text=")", padx=30, pady=10, relief=RAISED, fg="White", bg="Black", command=lambda: click(")"))

degb = Button(root, text="deg", padx=23, pady=10, relief=RAISED, fg="White", bg="Black")
degb.bind("<Button-1>", sc)
sinb = Button(root, text="sin", padx=26, pady=10, relief=RAISED, fg="White", bg="Black")
sinb.bind("<Button-1>", sc)
cosb = Button(root, text="cos", padx=23, pady=10, relief=RAISED, fg="White", bg="Black")
cosb.bind("<Button-1>", sc)
tanb = Button(root, text="tan", padx=24, pady=10, relief=RAISED, fg="White", bg="Black")
tanb.bind("<Button-1>", sc)
exp = Button(root, text="^", padx=29, pady=10, relief=RAISED, fg="White", bg="Black", command=lambda: click("**"))

lg = Button(root, text="lg", padx=28, pady=10, relief=RAISED, fg="White", bg="Black")
lg.bind("<Button-1>", sc)
one = Button(root, text="1", padx=30, pady=10, relief=RAISED, fg="White", bg="Grey", command=lambda: click("1"))
two = Button(root, text="2", padx=29, pady=10, relief=RAISED, fg="White", bg="Grey", command=lambda: click("2"))
three = Button(root, text="3", padx=29, pady=10, relief=RAISED, fg="White", bg="Grey", command=lambda: click("3"))
div = Button(root, text="/", padx=29, pady=10, relief=RAISED, fg="White", bg="Black", command=lambda: click("/"))

ln = Button(root, text="ln", padx=28, pady=10, relief=RAISED, fg="White", bg="Black")
ln.bind("<Button-1>", sc)
four = Button(root, text="4", padx=30, pady=10, relief=RAISED, fg="White", bg="Grey", command=lambda: click("4"))
five = Button(root, text="5", padx=29, pady=10, relief=RAISED, fg="White", bg="Grey", command=lambda: click("5"))
six = Button(root, text="6", padx=29, pady=10, relief=RAISED, fg="White", bg="Grey", command=lambda: click("6"))
mult = Button(root, text="*", padx=29, pady=10, relief=RAISED, fg="White", bg="Black", command=lambda: click("*"))


sqrtm = Button(root, text="Sqrt", padx=23, pady=10, relief=RAISED, fg="White", bg="Black")
sqrtm.bind("<Button-1>", sc)
seven = Button(root, text="7", padx=30, pady=10, relief=RAISED, fg="White", bg="Grey", command=lambda: click("7"))
eight = Button(root, text="8", padx=29, pady=10, relief=RAISED, fg="White", bg="Grey", command=lambda: click("8"))
nine = Button(root, text="9", padx=29, pady=10, relief=RAISED, fg="White", bg="Grey", command=lambda: click("9"))
minus = Button(root, text="-", padx=29, pady=10, relief=RAISED, fg="White", bg="Black", command=lambda: click("-"))

fact = Button(root, text="x!", padx=29, pady=10, relief=RAISED, fg="White", bg="Black")
fact.bind("<Button-1>", sc)
dot = Button(root, text=".", padx=31, pady=10, relief=RAISED, fg="White", bg="Black", command=lambda: click("."))
zero = Button(root, text="0", padx=29, pady=10, relief=RAISED, fg="White", bg="Grey", command=lambda: click("0"))
equal = Button(root, text="=", padx=29, pady=10, relief=RAISED, fg="Black", bg="Dark Orange", command=lambda: evaluate())
plus = Button(root, text="+", padx=29, pady=10, relief=RAISED, fg="White", bg="Black", command=lambda: click("+"))

e_b = Button(root, text="e", padx=29, pady=10, relief=RAISED, fg="Black", bg="Sky Blue")
e_b.bind("<Button-1>", sc)
pib = Button(root, text="pi", padx=28, pady=10, relief=RAISED, fg="Black", bg="Sky Blue")
pib.bind("<Button-1>", sc)
frac = Button(root, text="1/x", padx=25, pady=10, relief=RAISED, fg="Black", bg="Sky Blue")
frac.bind("<Button-1>", sc)


ac.grid(row=1, column=0)
bksp.grid(row=1, column=1)
mod.grid(row=1, column=2)
par1st.grid(row=1, column=3)
par2nd.grid(row=1, column=4)

degb.grid(row=2, column=0)
sinb.grid(row=2, column=1)
cosb.grid(row=2, column=2)
tanb.grid(row=2, column=3)
exp.grid(row=2, column=4)

lg.grid(row=3, column=0)
one.grid(row=3, column=1)
two.grid(row=3, column=2)
three.grid(row=3, column=3)
div.grid(row=3, column=4)

ln.grid(row=4, column=0)
four.grid(row=4, column=1)
five.grid(row=4, column=2)
six.grid(row=4, column=3)
mult.grid(row=4, column=4)

sqrtm.grid(row=5, column=0)
seven.grid(row=5, column=1)
eight.grid(row=5, column=2)
nine.grid(row=5, column=3)
minus.grid(row=5, column=4)

fact.grid(row=6, column=0)
dot.grid(row=6, column=1)
zero.grid(row=6, column=2)
equal.grid(row=6, column=3)
plus.grid(row=6, column=4)

e_b.grid(row=7, column=1)
pib.grid(row=7, column=2)
frac.grid(row=7, column=3)




root.mainloop()