from tkinter import *

root = Tk()
root.title("ENCRYPTION WITH ASCII CODE")
root.geometry("500x500")

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

profits = (20000, 45000, 78000, 97000, 12000, 456000, 65000, 54000, 10000, 30000, 70000, 90000)

months_label = Label(root)
months_label['text'] = months
months_label.place(relx=0.5, rely=0.1, anchor=CENTER)

profits_label = Label(root)
profits_label['text'] = profits
profits_label.place(relx=0.5, rely=0.2, anchor=CENTER)

max_profits_label = Label(root, text="")
max_profits_label.place(relx=0.5, rely=0.4, anchor=CENTER)

min_profits_label = Label(root, text="")
min_profits_label.place(relx=0.5, rely=0.6, anchor=CENTER)

def maxProfit(): 
    max_profit = max(profits)
    max_profit_index = profits.index(max_profit)
    print(max_profit_index)


    max_profit_month = months[max_profit_index]
    print("The max profit of " + str(max_profit) + " was recorded in the month of " + str(max_profit_month))
    max_profits_label['text'] = "The max profit of " + str(max_profit) + " was recorded in the month of " + str(max_profit_month)

btn = Button(root, text="Show Max Profitable Month", command=maxProfit)
btn.place(relx=0.5, rely=0.3, anchor=CENTER)

def minProfit():
    min_profit = min(profits)
    min_profit_index = profits.index(min_profit)
    print(min_profit_index)

    min_profit_month = months[min_profit_index]
    print("The min profit of " + str(min_profit) + " was recorded in the month of " + str(min_profit_month))
    min_profits_label['text'] = "The min profit of " + str(min_profit) + " was recorded in the month of " + str(min_profit_month)

btn1 = Button(root, text="Show Min Profitable Month", command=minProfit)
btn1.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()