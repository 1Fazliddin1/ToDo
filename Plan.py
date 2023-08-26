import os
from abc import ABC,abstractmethod,abstractproperty
class Abstrac(ABC):
    @abstractmethod
    def add_task(self):
        pass
    
    
    @abstractmethod
    def completed(self):
        pass
    
    
    @abstractmethod
    def show_tasks(self):
        pass
    
    
class ToDo(Abstrac):
    
    def add_task(self,val):
        f = open('list.txt','a')
        d = open('list.txt','r')
        res = f'{len(d.readlines())+1} {val}'
        f.write(res+'\n')
        print('|','-'*21,'|')
        print(f"| Malumot qo\'shildi✅     |" )
        print('|','-'*21,'|')
    
    def completed(self,disabling):
        d = open('list.txt','r')
        s = d.readlines()
        f = open('list.txt','w')
        l = ''
        for i,row in enumerate(s):
            if i != disabling:
                f.write(row)
            elif i == disabling:
                l+=row
                f.write(f"{row[0:2]}Vasifa bajarilgan✅ \n")
        print('|','-'*21,'|')
        print(f"   {l[2::]}   Vazifa bajarildi✅  " )
        print('|','-'*21,'|')
        
    def show_tasks(self):
        d = open('list.txt','r')
        return d.read()
    
if __name__ == '__main__':
    os.system('clear')
    My = ToDo()
    print('          INFORMATION','              KEYS 🔑')
    print('|','-'*31,'+','-'*8,'|')
    print('|','Malumot qoshmoqchi bolsangiz    | 🅰 🅳 🅳    |')
    print('|','-'*31,'+','-'*8,'|')
    print('|','Malumot o\'chirmoqchi bo\'lsangiz | 🅲 🅾 🅼 🅿  |')
    print('|','-'*31,'+','-'*8,'|')
    print('|','Dastur tugatmoqchi bo\'lsangiz   | 🆂 🆃 🅾 🅿  |')
    print('|','-'*31,'+','-'*8,'|')
    print('|','Ro\'yxatni ko\'rmoqchi bolsangiz  | 🆂 🅷 🅾 🆆  |')
    print('|','-'*31,'+','-'*8,'|')

    TandF = True
    
    while TandF: 
            print()
            print('         KERAKLI 🔑 SO\'ZNI KIRITING!')
            print('|','-'*15,'|')
            n = input('  ').upper()   
            print('|','-'*15,'|')
            if n == 'ADD':
                print()
                My.add_task(input('         Malumot kiriting: '))
            elif n == 'COMP':
                My.completed(int(input('        Qilingan vazifa tartib raqami: '))-1)
                
            elif n == 'SHOW':
                print('_'*30+'\n')
                print(My.show_tasks())
                print('_'*30)
            elif n == 'STOP':
                print('  Good Bye')
                TandF = False
            else:
                print()
                print('  SIZ NOTO\'G\'RI 🔑 SO\'Z KIRITTINGIZ ❌ ')
                # os.system('clear')