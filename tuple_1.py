#𝐧𝐞𝐬𝐓𝐮𝐩𝐥𝐞=(𝟏,𝟐,(𝟑,(𝟒,(𝟓,𝟔,(𝟕,𝟖,𝟗,(𝟏𝟎,𝟏𝟏))),(𝟏𝟐,𝟏𝟑))))

#𝐎𝐮𝐭𝐩𝐮𝐭=(𝟏, 𝟐, 𝟑, 𝟒, 𝟓, 𝟔, 𝟕, 𝟖, 𝟗, 𝟏𝟎, 𝟏𝟏, 𝟏𝟐, 𝟏𝟑)

def flatten_tuple(ip_tuple):
    op_list = []
    op_tuple =()

    for i in ip_tuple:
        if isinstance(i,tuple):
            op_list.extend(flatten_tuple(i))
        else:
            op_list.append(i)
    
    op_tuple = tuple(op_list)
    
    return op_tuple


ip_tuple = (1,2,(3,(4,(5,6,(7,8,9,(10,11))),(12,13))))
op_tuple = flatten_tuple(ip_tuple)

print(op_tuple)
                  
