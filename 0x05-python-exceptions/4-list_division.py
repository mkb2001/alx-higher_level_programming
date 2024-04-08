#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    c = 0
    try:

        for i in range(list_length):
            try:
                c = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                c = 0
                print("division by 0")
            except TypeError:
                c = 0
                print("wrong type")
            except IndexError:
                print("out of range")
            finally:
                new_list.append(c)

    except IndexError:
        pass
    return new_list

