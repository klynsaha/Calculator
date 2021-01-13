import tkinter
from tkinter import *
from tkinter import messagebox

val = ""
op = ""

def btn_no_clicked(value):
    global val
    val += str(value)
    data.set(val)

def btn_op_isClicked(operator):
    global val, op
    if val[-1] in {"+", "-", "*", "/"}:
        val = val[:-1] + operator
        op = operator
        data.set(val)
        return

    op = operator
    if op == "C":
        op = ""
        val = ""
    else:
        val += op
    data.set(val)

def result():
    global val, op
    values = val.split(op)
    x = float(values[0])
    y = float(values[1])
    if op == "+":
        val = str(x+y)
    elif op == "-":
        val = str(x-y)
    elif op == "*":
        val = str(x*y)
    elif op == "/":
        if y == 0:
            # messagebox.showerror("Error", "Division by Zero not Allowed!")
            data.set("Error")
            val = ""
            op = ""
            return
        else:
            val = str(x/y)
    data.set(val)


root = Tk()
root.geometry("300x400+400+400")
# root.resizable(0, 0)
root.title("Calculator")

data = StringVar()
lbl = Label(
    root,
    text = "Label",
    anchor = SE,
    font = ("Verdana", 20),
    textvariable = data,
)
lbl.pack(expand = True, fill = "both")

# 4 Frames
btnrow1 = Frame(root, background = "white")
btnrow1.pack(expand = True, fill = "both")

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both")

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both")

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both")

# The buttons section
btn1 = Button(
    btnrow1,
    text = "1",
    font = ("Verdana", 22),
    relief = GROOVE,
    borderwidth = 0,
    background = "white",
    command = lambda: btn_no_clicked(1),
)
btn1.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(
    btnrow1,
    text = "2",
    font = ("Verdana", 22),
    relief = GROOVE,
    borderwidth = 0,
    command = lambda: btn_no_clicked(2),
)
btn2.pack(side = LEFT, expand = True, fill = "both",)

btn3 = Button(
    btnrow1,
    text = "3",
    font = ("Verdana", 22),
    relief = GROOVE,
    bd = 0,
    command = lambda: btn_no_clicked(3),
)
btn3.pack(side = LEFT, expand = True, fill = "both",)

btnplus = Button(
    btnrow1,
    text = "+",
    font = ("Verdana", 22),
    relief = GROOVE,
    bd = 0,
    command = lambda: btn_op_isClicked("+"),
)
btnplus.pack(side = LEFT, expand = True, fill = "both",)

# buttons for frame 2

btn4 = Button(
    btnrow2,
    text = "4",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: btn_no_clicked(4),
)
btn4.pack(side = LEFT, expand = True, fill = "both",)

btn5 = Button(
    btnrow2,
    text = "5",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: btn_no_clicked(5),
)
btn5.pack(side = LEFT, expand = True, fill = "both",)

btn6 = Button(
    btnrow2,
    text = "6",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: btn_no_clicked(6),
)
btn6.pack(side = LEFT, expand = True, fill = "both",)

btnsub = Button(
    btnrow2,
    text = "-",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: btn_op_isClicked("-"),
)
btnsub.pack(side = LEFT, expand = True, fill = "both",)

# button for frame 3

btn7 = Button(
    btnrow3,
    text = "7",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: btn_no_clicked(7),
)
btn7.pack(side = LEFT, expand = True, fill = "both",)

btn8 = Button(
    btnrow3,
    text = "8",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: btn_no_clicked(8),
)
btn8.pack(side = LEFT, expand = True, fill = "both",)

btn9 = Button(
    btnrow3,
    text = "9",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: btn_no_clicked(9),
)
btn9.pack(side = LEFT, expand = True, fill = "both",)

btnmult = Button(
    btnrow3,
    text = "*",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: btn_op_isClicked("*"),
)
btnmult.pack(side = LEFT, expand = True, fill = "both",)

# button for frame4

btnc = Button(
    btnrow4,
    text = "C",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: btn_op_isClicked("C"),
)
btnc.pack(side = LEFT, expand = True, fill = "both",)

btn0 = Button(
    btnrow4,
    text = "0",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: btn_no_clicked(0),
)
btn0.pack(side = LEFT, expand = True, fill = "both",)

btnequal = Button(
    btnrow4,
    text = "=",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = result,
)
btnequal.pack(side = LEFT, expand = True, fill = "both",)

btndiv = Button(
    btnrow4,
    text = "/",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = lambda: btn_op_isClicked("/"),
)
btndiv.pack(side = LEFT, expand = True, fill = "both",)


root.mainloop()