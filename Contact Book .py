
# import json module

import json

# data=[{'name':'Arbaj','age':21}]

# with open(r'C:\Python\pydroid\My projects\contact data.json','w') as f:
#     json.dump(data,f,indent=4)

# with open(r"C:\Python\pydroid\My projects\contact data.json",'r')as f:
#     file_data=json.load(f)
#     print(file_data)
#     print(file_data.items())

print('Contact Book\n')

print('1. Add contact')

print('2. Delet contact')

print('3. Update contact')

print('4. Search contact')

print('5. View all contact\n')

option=int(input('Choose Option ....'))

if(option==1):
    contact_name=input('Enter contact name :')
    contact_number=input('Enter contact number :')
    with open("C:\Python\pydroid\My projects\contact data.json")as f:
        data=json.load(f)
    new_data={'name':contact_name,'number':contact_number}
    data.append(new_data)
    with open("C:\Python\pydroid\My projects\contact data.json",'w')as f:
        json.dump(data,f,indent=4)
        print('Add Succesfully')

elif(option==2):
    contact_name=input('Enter contact name :')
    # contact_number=input('Enter contact number :')
    with open("C:\Python\pydroid\My projects\contact data.json")as f:
        data=json.load(f)
        for item in data:
            print(item)
            if item['name'] == contact_name:
                data.remove(item)
                print('Delet Succesfully')
                break
    with open("C:\Python\pydroid\My projects\contact data.json",'w')as f:
        json.dump(data,f,indent=4)
        print('Confirm')

elif(option==3):
    contact_name=input('Enter contact name :')
    contact_number=input('Enter contact number :')
    with open("C:\Python\pydroid\My projects\contact data.json")as f:
        data=json.load(f)
        for item in data:
            print(item)
            if item['name'] == contact_name:
                name=input('enter new name')
                number=input('enter new number')
                item['name']=name
                item['number']=number
                print('Update Succesfully')
                break
    data=[{'name':contact_name,'number':contact_number}]
    with open("C:\Python\pydroid\My projects\contact data.json",'w')as f:
        json.dump(data,f,indent=4)

if(option==4):
    contact_name=input('Enter contact name :')
    with open("C:\Python\pydroid\My projects\contact data.json")as f:
        data=json.load(f)
        
        for item in data:
            if item['name']==contact_name:
                print(item)
                break
            else:
                print('dont match contact')
                break
    with open("C:\Python\pydroid\My projects\contact data.json",'w')as f:
        json.dump(data,f,indent=4)
        print('Add Succesfully')

if(option==5):
    with open("C:\Python\pydroid\My projects\contact data.json")as f:
        data=json.load(f)
        print(data)
        for item in data:
            print(item)



