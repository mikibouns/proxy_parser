from tkinter import *
from proxies_list import ProxyList
from parse_proxy_requests import ParserProxy

class GUI_rate:
    def __init__(self, main):
        self.entry1 = Entry(main, width=15, font=15)
        self.button1 = Button(main, text='Get current rate')
        self.label1 = Label(main, width=27, font=15)

        self.entry1.grid(row=0, column=0)
        self.button1.grid(row=0, column=1)
        self.label1.grid(row=0, column=2)

        self.button1.bind('<Button-1>', self.answer)

    def answer(self, event):
        currency_pair = self.entry1.get()
        proxy_list = ProxyList()
        par_prox = ParserProxy(proxy_list, currency_pair)
        rate_cp = par_prox.get_rate()
        try:
            if rate_cp[0]:
                self.label1.configure(text=float(rate_cp[0]))
            else:
                self.label1.configure(text='Не могу получить значение!')
        except ValueError:
            self.label1.configure(text='Не корректное значение!')

root = Tk()
root.title('Get current rate')

exchange_rate_of_a_currency_pair = GUI_rate(root)

root.mainloop()
