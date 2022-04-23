# import all classes / functions from the tkinter
from tkinter import *
from turtle import width

# Function for clearing the
# contents of all entry boxes


def clear_all():
    principle_field.delete(0, END)
    interestRate_field1.delete(0, END)
    compoundingPeriod_field1.delete(0, END)
    interestRate_field2.delete(0, END)
    compoundingPeriod_field2.delete(0, END)
    interestRate_field3.delete(0, END)
    compoundingPeriod_field3.delete(0, END)
    apy_field.delete(0, END)
    apy_field2.delete(0, END)
    apy_field3.delete(0, END)
    bank_field.delete(0, END)
    balance1.delete(0, END)
    balance2.delete(0, END)
    balance3.delete(0, END)
    principle_field.focus_set()


def calculate_apy():
    principle = int(principle_field.get())
    interestRate = float(interestRate_field1.get())
    compoundingPeriod = int(compoundingPeriod_field1.get())
    interestRate2 = float(interestRate_field2.get())
    compoundingPeriod2 = int(compoundingPeriod_field2.get())
    interestRate3 = float(interestRate_field3.get())
    compoundingPeriod3 = int(compoundingPeriod_field3.get())
    APY = ((1 + (interestRate/100)/compoundingPeriod)**(compoundingPeriod))-1
    APY2 = ((1 + ((interestRate2/100)/compoundingPeriod2))
            ** (compoundingPeriod2))-1
    APY3 = ((1 + ((interestRate3/100)/compoundingPeriod3))
            ** (compoundingPeriod3))-1
    bl1 = principle * ((1 + (interestRate/100) /
                       compoundingPeriod) ** compoundingPeriod)
    bl2 = principle * ((1 + (interestRate2/100) /
                       compoundingPeriod2) ** compoundingPeriod2)
    bl3 = principle * ((1 + (interestRate3/100) /
                       compoundingPeriod3) ** compoundingPeriod3)
    apy_field.insert(1, APY*100)
    apy_field2.insert(1, APY2*100)
    apy_field3.insert(1, APY3*100)
    balance1.insert(1, bl1)
    balance2.insert(1, bl2)
    balance3.insert(1, bl3)
    l = {'bank1': APY, 'bank2': APY2, 'bank3': APY3}
    val = max(l.values())
    for key, value in l.items():
        if val == value:
            bank_field.insert(1, key)
            break

# from tkinter import *


window = Tk()
window.configure(background='light blue')
window.geometry("600x700")
window.title("APY Calculator")

label1 = Label(window, text="Enter the Principle Amount : ",
               fg='black', bg='light blue')
label2 = Label(window, text="Enter Interest Rate for Bank 1 (%) : ",
               fg='black', bg='light blue')
label3 = Label(window, text="Enter Compounding Period for Bank 1 : ",
               fg='black', bg='light blue')
label4 = Label(window, text="Enter Interest Rate for Bank 2 (%) : ",
               fg='black', bg='light blue')
label5 = Label(window, text="Enter Compounding Period for Bank 2 : ",
               fg='black', bg='light blue')
label6 = Label(window, text="Enter Interest Rate for Bank 3 (%) : ",
               fg='black', bg='light blue')
label7 = Label(window, text="Enter Compounding Period for Bank 3 : ",
               fg='black', bg='light blue')
label8 = Label(window, text="APY for Bank 1 : ", fg='black', bg='light blue')
label9 = Label(window, text="APY for Bank 2 : ", fg='black', bg='light blue')
label10 = Label(window, text="APY for Bank 3 : ", fg='black', bg='light blue')
label11 = Label(window, text="Which Bank is better : ",
                fg='black', bg='light blue')
label12 = Label(window, text="Balance after one year in bank 1",
                fg="black", bg="light blue")
label13 = Label(window, text="Balance after one year in bank 2",
                fg="black", bg="light blue")
label14 = Label(window, text="Balance after one year in bank 3",
                fg="black", bg="light blue")

label1.grid(row=1, column=2, padx=10, pady=5, sticky=W)
label2.grid(row=2, column=2, padx=10, pady=5, sticky=W)
label3.grid(row=3, column=2, padx=10, pady=5, sticky=W)
label4.grid(row=4, column=2, padx=10, pady=5, sticky=W)
label5.grid(row=5, column=2, padx=10, pady=5, sticky=W)
label6.grid(row=6, column=2, padx=10, pady=5, sticky=W)
label7.grid(row=7, column=2, padx=10, pady=5, sticky=W)
label8.grid(row=9, column=2, padx=10, pady=5, sticky=W)
label9.grid(row=10, column=2, padx=10, pady=5, sticky=W)
label10.grid(row=11, column=2, padx=10, pady=5, sticky=W)
label11.grid(row=12, column=2, padx=10, pady=5, sticky=W)
label12.grid(row=13, column=2, padx=10, pady=5, sticky=W)
label13.grid(row=14, column=2, padx=10, pady=5, sticky=W)
label14.grid(row=15, column=2, padx=10, pady=5, sticky=W)

principle_field = Entry(window)
interestRate_field1 = Entry(window)
compoundingPeriod_field1 = Entry(window)
interestRate_field2 = Entry(window)
compoundingPeriod_field2 = Entry(window)
interestRate_field3 = Entry(window)
compoundingPeriod_field3 = Entry(window)
apy_field = Entry(window)
apy_field2 = Entry(window)
apy_field3 = Entry(window)
bank_field = Entry(window)
balance1 = Entry(window)
balance2 = Entry(window)
balance3 = Entry(window)

principle_field.grid(row=1, column=3, padx=10, pady=5)
interestRate_field1.grid(row=2, column=3, padx=10, pady=5)
compoundingPeriod_field1.grid(row=3, column=3, padx=10, pady=5)
interestRate_field2.grid(row=4, column=3, padx=10, pady=5)
compoundingPeriod_field2.grid(row=5, column=3, padx=10, pady=5)
interestRate_field3.grid(row=6, column=3, padx=10, pady=5)
compoundingPeriod_field3.grid(row=7, column=3, padx=10, pady=5)
apy_field.grid(row=9, column=3, padx=10, pady=5)
apy_field2.grid(row=10, column=3, padx=10, pady=5)
apy_field3.grid(row=11, column=3, padx=10, pady=5)
bank_field.grid(row=12, column=3, padx=10, pady=5)
balance1.grid(row=13, column=3, padx=10, pady=5)
balance2.grid(row=14, column=3, padx=10, pady=5)
balance3.grid(row=15, column=3, padx=10, pady=5)

button1 = Button(window, text="Submit", bg="white",
                 fg="black", command=calculate_apy)
button2 = Button(window, text="Clear", bg="white",
                 fg="black", command=clear_all)
button3 = Button(window, text="Exit", bg="white",
                 fg="black", command=window.destroy)

button1.grid(row=8, column=3, pady=10)
button2.grid(row=17, column=3, pady=10)
button3.grid(row=19, column=3, pady=10)

window.mainloop()
