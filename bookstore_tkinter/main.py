from tkinter import *
from backend import Database

database = Database("bookstore.db")

class BookStoreMgrWindow(object):

  def __init__(self, window):
    self.window = window

    self.window.wm_title('Book Store')

    title_label = Label(master=window, text="Title")
    title_label.grid(row=0, column=0)

    author_label = Label(master=window, text="Author")
    author_label.grid(row=0, column=2)

    year_label = Label(master=window, text="year")
    year_label.grid(row=1, column=0)

    isbn_label = Label(master=window, text="ISBN")
    isbn_label.grid(row=1, column=2)

    self.book_count_text = StringVar()
    self.book_count_text.set("0 books in stock")
    self.book_count_label = Label(master=window, textvariable=self.book_count_text)
    self.book_count_label.grid(row=8, column=0, columnspan=4)


    # Entries
    self.title_text = StringVar()
    self.title_input = Entry(master=window, textvariable=self.title_text)
    self.title_input.grid(row=0, column=1)

    self.author_text = StringVar()
    self.author_input = Entry(master=window, textvariable=self.author_text)
    self.author_input.grid(row=0, column=3)

    self.year_text = StringVar()
    self.year_input = Entry(master=window, textvariable=self.year_text)
    self.year_input.grid(row=1, column=1)

    self.isbn_text = StringVar()
    self.isbn_input = Entry(master=window, textvariable=self.isbn_text)
    self.isbn_input.grid(row=1, column=3)

    # list
    self.book_list = Listbox(master=window, height=6, width=35)
    self.book_list.grid(row=2, column=0, rowspan=6, columnspan=2)

    self.book_list.bind('<<ListboxSelect>>', self.get_selected_row)

    # scrollbar
    self.scrollbar = Scrollbar(master=window)
    self.scrollbar.grid(row=2,column=2, rowspan=6)

    self.book_list.configure(yscrollcommand=self.scrollbar.set)
    self.scrollbar.configure(command=self.book_list.yview)

    # buttons
    self.view_all = Button(master=window, text='View all', width=12, command=self.view_all_command)

    self.view_all.grid(row=2, column=3)

    self.search_entry = Button(master=window, text='Search entry', width=12, command=self.search_command)
    self.search_entry.grid(row=3, column=3)

    self.add_entry = Button(master=window, text='Add entry', width=12, command=self.insert_command)
    self.add_entry.grid(row=4, column=3)

    self.update_entry = Button(master=window, text='Update entry', width=12, command=self.update_command)
    self.update_entry.grid(row=5, column=3)

    self.delete_entry = Button(master=window, text='Delete entry', width=12, command=self.delete_command)
    self.delete_entry.grid(row=6, column=3)

    self.close = Button(master=window, text='Close', width=12, command=window.destroy)
    self.close.grid(row=7, column=3)

    # Call view_all_command to load all books at start
    self.view_all_command()

  def get_selected_row(self, event):
    # mark selected_row as global variable so that other function can access it.
    # global selected_row
    index = -1
    if len(self.book_list.curselection()) > 0:
      index = self.book_list.curselection()[0]
      self.selected_row = self.book_list.get(index)
    
    # show selected_row onto input fields
    self.title_input.delete(0, END)
    self.title_input.insert(END, self.selected_row[1])
    self.author_input.delete(0, END)
    self.author_input.insert(END, self.selected_row[2])
    self.year_input.delete(0, END)
    self.year_input.insert(END, self.selected_row[3])
    self.isbn_input.delete(0, END)
    self.isbn_input.insert(END, self.selected_row[4])
    
    return self.selected_row

  def view_all_command(self):
    self.book_list.delete(0, END)
    rows = database.view_all()
    self.book_count_text.set(f"{len(rows)} books in stock")
    for row in rows:
      self.book_list.insert(END, row)

  def insert_command(self):
    database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
    self.view_all_command()
      # Since select_row inserted, input fields should be cleared.
    self.title_input.delete(0, END)
    self.author_input.delete(0, END)
    self.year_input.delete(0, END)
    self.isbn_input.delete(0, END)

  def search_command(self):
    rows = database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
    self.book_list.delete(0, END)
    for row in rows:
      self.book_list.insert(END, row)

  def delete_command(self):
    database.delete(self.selected_row[0])
    # Since select_row deleted, input fields should be cleared.
    self.title_input.delete(0, END)
    self.author_input.delete(0, END)
    self.year_input.delete(0, END)
    self.isbn_input.delete(0, END)
    self.view_all_command()


  def update_command(self):
    database.update(self.selected_row[0], self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
    self.view_all_command()

  
window = Tk()
BookStoreMgrWindow(window)
window.mainloop()

