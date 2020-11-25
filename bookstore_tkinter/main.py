from tkinter import *
import backend


def get_selected_row(event):
  # mark selected_row as global variable so that other function can access it.
  global selected_row
  index = -1
  if len(book_list.curselection()) > 0:
    index = book_list.curselection()[0]
    selected_row = book_list.get(index)
  
  # show selected_row onto input fields
  title_input.delete(0, END)
  title_input.insert(END, selected_row[1])
  author_input.delete(0, END)
  author_input.insert(END, selected_row[2])
  year_input.delete(0, END)
  year_input.insert(END, selected_row[3])
  isbn_input.delete(0, END)
  isbn_input.insert(END, selected_row[4])
  
  return selected_row
  

def view_all_command():
  book_list.delete(0, END)
  rows = backend.view_all()
  book_count_text.set(f"{len(rows)} books in stock")
  for row in rows:
    book_list.insert(END, row)

def insert_command():
  backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
  view_all_command()
    # Since select_row inserted, input fields should be cleared.
  title_input.delete(0, END)
  author_input.delete(0, END)
  year_input.delete(0, END)
  isbn_input.delete(0, END)

def search_command():
  rows = backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
  book_list.delete(0, END)
  for row in rows:
    book_list.insert(END, row)

def delete_command():
  backend.delete(selected_row[0])
  # Since select_row deleted, input fields should be cleared.
  title_input.delete(0, END)
  author_input.delete(0, END)
  year_input.delete(0, END)
  isbn_input.delete(0, END)
  view_all_command()


def update_command():
  backend.update(selected_row[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
  view_all_command()

  

window = Tk()
window.wm_title('Book Store')

title_label = Label(master=window, text="Title")
title_label.grid(row=0, column=0)

author_label = Label(master=window, text="Author")
author_label.grid(row=0, column=2)

year_label = Label(master=window, text="year")
year_label.grid(row=1, column=0)

isbn_label = Label(master=window, text="ISBN")
isbn_label.grid(row=1, column=2)

book_count_text = StringVar()
book_count_text.set("0 books in stock")
book_count_label = Label(master=window, textvariable=book_count_text)
book_count_label.grid(row=8, column=0, columnspan=4)


# Entries
title_text = StringVar()
title_input = Entry(master=window, textvariable=title_text)
title_input.grid(row=0, column=1)

author_text = StringVar()
author_input = Entry(master=window, textvariable=author_text)
author_input.grid(row=0, column=3)

year_text = StringVar()
year_input = Entry(master=window, textvariable=year_text)
year_input.grid(row=1, column=1)

isbn_text = StringVar()
isbn_input = Entry(master=window, textvariable=isbn_text)
isbn_input.grid(row=1, column=3)

# list
book_list = Listbox(master=window, height=6, width=35)
book_list.grid(row=2, column=0, rowspan=6, columnspan=2)

book_list.bind('<<ListboxSelect>>', get_selected_row)

# scrollbar
scrollbar = Scrollbar(master=window)
scrollbar.grid(row=2,column=2, rowspan=6)

book_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=book_list.yview)

# buttons
view_all = Button(master=window, text='View all', width=12, command=view_all_command)

view_all.grid(row=2, column=3)

search_entry = Button(master=window, text='Search entry', width=12, command=search_command)
search_entry.grid(row=3, column=3)

add_entry = Button(master=window, text='Add entry', width=12, command=insert_command)
add_entry.grid(row=4, column=3)

update_entry = Button(master=window, text='Update entry', width=12, command=update_command)
update_entry.grid(row=5, column=3)

delete_entry = Button(master=window, text='Delete entry', width=12, command=delete_command)
delete_entry.grid(row=6, column=3)

close = Button(master=window, text='Close', width=12, command=window.destroy)
close.grid(row=7, column=3)

# Call view_all_command to load all books at start
view_all_command()

window.mainloop()
