
import os                           # import os module 

class clutter:                      # and create class clutter
    index=70                        # are class variable for index value
    def clear(ob,folder,formate):                 # clear function to clear folder clutter  
        print(f'Rename all {formate} files')      # print function
        ob.list=os.listdir(f'C:/{folder}')        # udsed os.listdir function for take folder list like C:/pngfiles
        # print(ob.list)
        for ob.filename in obj.list:              # for loop for take file by folder one by one
          ob.file_splite=os.path.splitext(obj.filename)    # split file name and extention
          ob.file_extention=ob.file_splite[1]              # and extention pass on file_extention variable
          if(ob.file_extention!=formate):                  # and copaire extention to given formate
            continue                                       # continue skip iterable to dont match extention
          ob.index+=1                                      # if extention match and 1 increment in index variable
          print(ob.index,ob.filename)                      # print index number and file name
          os.rename(f"C:/pngfiles/{obj.filename}",f"C:/pngfiles/{obj.index}{formate}")        # rename given extention file name
        print('Succesfully')                               # print succesfully

obj=clutter()                              # create object of class clutter
fo=input('please enter folder name')       # and given folder name by user
f=input('please enter file formate')       # given folder file extention by user
obj.clear(fo,f)                            # called clear method given two argument folder and extention

# exit