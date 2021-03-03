# !bin/bash/python3

old_name=input("Please input your file name:")
index=old_name.rfind('.')
new_name=old_name[:index]+'[backup]'+old_name[index:]

if index >0: # except for the name like .txt
    old_f=open(old_name,'rb+')
    new_f=open(new_name,'wb+')
    con=old_f.read()
    new_f.write(con)
    old_f.close()
    new_f.close()


