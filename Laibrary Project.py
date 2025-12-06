
# create a library class

class Library:
    Books=["Quran",'Torat','jabur','injil']
    no_of_books=len(Books)
    
    def main(ob):
     for ob.i in range(10):
      print('1. Add book ')
      print('2. Remove book ')
      print('3. show numbers of books ')
      try:
       num=int(input('enter your choice : '))
      except ValueError:
        print('please enter numric value')
        break
      if(num==1):
        book=input('enter book name')    
        ob.Books.append(book)
      elif(num==2):
        rmbook=input('enter remove book name')
        ob.Books.remove(rmbook)
      elif(num==3):  
        print('length of Books :',len(ob.Books))
        # print(f'no_of_Books : {ob.no_of_books}')
        for ob.index,ob.i in enumerate(ob.Books):
            print(f'Index : {ob.index} Book : {ob.i}')
      else:
         break
            

obj=Library()
obj.main()
