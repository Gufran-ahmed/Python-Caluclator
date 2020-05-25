from tkinter import *


def OnClick(number):
    global displayNumber
    displayNumber = displayNumber + str(number)
    text_input.set(displayNumber)


def clearDisp():
    global displayNumber
    displayNumber = ""
    text_input.set(displayNumber)


def equalOp():
    global displayNumber
    text_input.set(str(eval(displayNumber)))


calculator = Tk()
calculator.title('Calculator')
calculator.geometry("300x330")
displayNumber = ""
text_input = StringVar()
display = Entry(calculator, font=('sans serif', 18), textvariable=text_input, bd=10,
                bg="orange", justify='right').grid(columnspan=4, rowspan=1)

button1 = Button(calculator, padx=20, pady=12, bd=6, text="7", font=20, command=lambda: OnClick(7)).grid(row=1, column=0, columnspan=1)
button2 = Button(calculator, padx=20, pady=12, bd=6, text="8", font=20, command=lambda: OnClick(8)).grid(row=1, column=1)
button3 = Button(calculator, padx=20, pady=12, bd=6, text="9", font=20, command=lambda: OnClick(9)).grid(row=1, column=2)
button4 = Button(calculator, padx=20, pady=12, bd=6, text="x", font=20, command=lambda: OnClick("*")).grid(row=1, column=3)
button5 = Button(calculator, padx=20, pady=12, bd=6, text="4", font=20, command=lambda: OnClick(4)).grid(row=2, column=0)
button6 = Button(calculator, padx=20, pady=12, bd=6, text="5", font=20, command=lambda: OnClick(5)).grid(row=2, column=1)
button7 = Button(calculator, padx=20, pady=12, bd=6, text="6", font=20, command=lambda: OnClick(6)).grid(row=2, column=2)
button8 = Button(calculator, padx=20, pady=12, bd=6, text="-", font=20, command=lambda: OnClick("-")).grid(row=2, column=3)
button9 = Button(calculator, padx=20, pady=12, bd=6, text="1", font=20, command=lambda: OnClick(1)).grid(row=4, column=0)
button10 = Button(calculator, padx=20, pady=12, bd=6, text="2", font=20, command=lambda: OnClick(2)).grid(row=4, column=1)
button11 = Button(calculator, padx=20, pady=12, bd=6, text="3", font=20, command=lambda: OnClick(3)).grid(row=4, column=2)
button12 = Button(calculator, padx=20, pady=12, bd=6, text="+", font=20, command=lambda: OnClick("+")).grid(row=4, column=3)
button13 = Button(calculator, padx=20, pady=12, bd=6, text="=", font=20, command=lambda: equalOp()).grid(row=5, column=0)
button14 = Button(calculator, padx=20, pady=12, bd=6, text="0", font=20, command=lambda: OnClick(0)).grid(row=5, column=1)
button15 = Button(calculator, padx=20, pady=12, bd=6, text="C", font=20, command=lambda: clearDisp()).grid(row=5, column=2)
button16 = Button(calculator, padx=20, pady=12, bd=6, text="÷", font=20, command=lambda: OnClick("/")).grid(row=5,column=3)


calculator.mainloop()
