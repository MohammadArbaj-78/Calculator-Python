
# new project

import time as t

class todo_reward:
    ac_timing=[]
    tomorrow_ac={}
    total_reward=0
    list=[]
    def todo_list(self):
        for i in range(5):
            self.item=input(f'enter your daily Action {i+1}')
            self.list.append(self.item)

    def show_ac(self):
        print(self.list)
        print('your daily actions')
        print('setup actions')

    def ac_setup(self):
        for self.ac in self.list:
            print('set action :',self.ac)
            self.ac_timing=input('enter timing')
            self.key=self.ac
            self.value=self.ac_timing
            self.tomorrow_ac[self.key]=self.value
            print('set :',self.tomorrow_ac)

    def time_run(self):
        a_timing=t.strftime('%H')
        print(a_timing)
        self.length=len(self.ac_timing)
        for self.i in range(self.length):
           for self.one in self.tomorrow_ac(1):
            if(a_timing==self.ac_timing):
                print(self.tomorrow_ac[self.i])
                print('Popup')
            elif(a_timing==self.ac_timing):
                print('complete your work')
            else:

                print(f'not {self.one} work time')

obj=todo_reward()
obj.todo_list()
obj.show_ac()
obj.ac_setup()
for i in range(1):
   obj.time_run()
            