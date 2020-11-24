class checker:

  def missing_num(list_of_num):
    ordered_list = [x for x in range(1,11)]

    for number in ordered_list:
      if number not in list_of_num:
        return number
