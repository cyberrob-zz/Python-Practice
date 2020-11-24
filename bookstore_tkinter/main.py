from tkinter import *
import backend


window = Tk()

title_label = Label(master=window, text="Title")
title_label.grid(row=0, column=0)

author_label = Label(master=window, text="Author")
author_label.grid(row=0, column=2)

year_label = Label(master=window, text="year")
year_label.grid(row=1, column=0)

isbn_label = Label(master=window, text="ISBN")
isbn_label.grid(row=1, column=2)

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

# scrollbar
scrollbar = Scrollbar(master=window)
scrollbar.grid(row=2,column=2, rowspan=6)

book_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=book_list.yview)

# buttons
view_all = Button(master=window, text='View all', width=12)

view_all = Button(master=window, text='View all', width=12)
view_all.grid(row=2, column=3)

search_entry = Button(master=window, text='Search entry', width=12)
search_entry.grid(row=3, column=3)

add_entry = Button(master=window, text='Add entry', width=12)
add_entry.grid(row=4, column=3)

update_entry = Button(master=window, text='Update entry', width=12)
update_entry.grid(row=5, column=3)

delete_entry = Button(master=window, text='Delete entry', width=12)
delete_entry.grid(row=6, column=3)

close = Button(master=window, text='Close', width=12)
close.grid(row=7, column=3)



window.mainloop()
