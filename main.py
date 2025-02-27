from currency_convertor import CurrencyConvertor
import tkinter as tk

a = CurrencyConvertor()
window = tk.Tk()
window.geometry("500x360")

# Define the global label to avoid overlapping text
l5 = None


def clicked():
    global l5
    try:
        # Sanitize and validate input
        amount = int(e1.get())
        cur1 = e2.get().strip().upper()
        cur2 = e3.get().strip().upper()

        # Attempt to perform currency conversion
        data = a.convert(amount, cur1, cur2)
    except ValueError:
        data = "Invalid amount"
    except Exception as e:
        data = f"Error: {str(e)}"

    # Update the label to display the result
    if l5:
        l5.config(text=data)  # Update the existing label text
    else:
        l5 = tk.Label(window, text=data)
        l5.place(x=175, y=235)


# User interface components
tk.Label(window, text="Currency Convertor", font="Times 20 bold").place(x=120, y=0)
tk.Label(window, text="Enter amount: ", font="Times 15 bold").place(x=20, y=80)
e1 = tk.Entry(window)
e1.place(x=310, y=85)  # Place the entry widget

tk.Label(window, text="Enter Currency to be converted: ", font="Times 15 bold").place(x=20, y=115)
e2 = tk.Entry(window)
e2.place(x=310, y=120)  # Place the entry widget

tk.Label(window, text="Enter required Currency: ", font="Times 15 bold").place(x=20, y=150)
e3 = tk.Entry(window)
e3.place(x=310, y=150)  # Place the entry widget

tk.Button(window, text="Click to convert Currency", command=clicked).place(x=165, y=200)

# Start the Tkinter main loop
window.mainloop()
