def flatten_list(my_list):
    op_list = []
    for i in my_list:
        if isinstance(i,list):
            op_list.extend(flatten_list(i)) # Recursively flatten the sublist
        else:
            op_list.append(i) # Append non-list item

    return  op_list

my_list = [1,2,[3,[4,[5,6]]]]
op_list =  flatten_list (my_list) 

print(op_list)

