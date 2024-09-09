class Employee:
    def __init__(self):
        self.dic={}
    def addemp(self,id,name,sal,dept):
        if id not in self.dic:
            self.dic[id]=id
            self.dic["name"]=name
            self.dic["dept"]=dept
            self.dic["salary"]=sal
            print("\nemployee added successfully")
        else:
            print("\nemployee exists already")
            
    def updateemp(self,id,newdept,newsalary):
        
         if id in self.dic:
            self.dic["dept"]=dept
            self.dic["salary"]=sal
            print("\nemployee details changed successfully")
            
#         else:
#             print("\nemployee do not exists already")
            
    def searchemp(self,id):
        
        if id in self.dic:
            print("\nemployee exits!!, details are: ")
            print(self.dic[id])
            print(self.dic["name"])
            print(self.dic["dept"])
            print(self.dic["salary"])
            
        else:
            print("\nemployee do not exits!!")
            
    def deptreport(self,deptt):
        
        
        for deptt in self.dic:
                print(self.dic["name"])
                print(self.dic["salary"])
            
        else: 
            print("\ndepartment do not exists")

emp=Employee()
emp.addemp(1,"sabeeh",50000,"ECE")
emp.addemp(2,"abhi",50000,"CSE")

emp.searchemp(1)

emp.deptreport("ECE")


            
