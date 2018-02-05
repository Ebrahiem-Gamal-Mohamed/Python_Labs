import smtplib
from email.mime.text import MIMEText

class Person():
    def __init__(self, name="user", money=0, mood="good", healthRate=100):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate
    
    @property
    def name(self):
        return self.__name

    @property
    def money(self):
        return self.__money

    @property
    def mood(self):
        return self.__mood

    @property
    def healthRate(self):
        return self.__healthRate

    @name.setter
    def name(self, name):
        self.__name = name

    @money.setter
    def money(self, money):
        self.__money = money

    @mood.setter
    def mood(self, mood):
        self.__mood = mood

    @healthRate.setter
    def healthRate(self,healthRate):    
	    if healthRate >=0 and healthRate <=100 :
		    self.__healthRate = healthRate
	    else: 
            self.__healthRate =50    

    def sleep(self, hours):
        if hours == 7:
            self.__mood =  "happy"
        elif hours < 7:
            self.__mood =  "tired"
        else:
            self.__mood =  "lazy"

    def eat(self, meals):
        if meals == 3:
            self.__healthRate = 100
        elif meals == 2:
            self.__healthRate = 75
        elif meals == 1:
            self.__healthRate = 50

    def buy(self, items):
        if items == 1:
            self.__money -= (10 * items)

class Employee(Person):
    def __init__(self, name="user", money=0, mood="good", healthRate=100, id=0, car="no car", salary=1000, distanceToWalk=20):
        super(Employee, self).__init__(name, money, mood, healthRate)
        self.id = id
        self.car = car
        self.salary = salary
        self.distanceToWalk = distanceToWalk

    def id(self):
        return self.__id
    
    @property
    def car(self):
        return self.__car
    
    @property
    def email(self):
        return self.__email
    
    @property
    def salary(self):
        return self.__salary

    @property
    def distanceToWork(self):
        return self.__distanceToWork

    @id.setter
    def id(self, id):
        self.__id = id

    @car.setter
    def car(self,car):
        self.__car = car

    @email.setter
    def email(self, email):
        self.__email = email

    @salary.setter
    def salary(self, salary):
        if salary > 1000:
            self.__salary = salary 
        else: 
            self.__salary =1000

    @distanceToWork.setter
    def distanceToWork(self, distanceToWork):
        self.__distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self.__mode = "happy"
        elif hours > 8:
            self.__mode = "tired"
        else:
            self.__mode = "lazy"

    def drive(self, distanceToWork):
        self.car.run(10, self.__distanceToWork)

    def refual(self, gasAmount = 100):
        self.fuelRate = self.gasAmount

    def send_mail(self, to,subject,msg,receiver_name):
        pass

class Office():
    employeesNum = 0

    def __init__(self, name, employee=[],late):
        self.name = name
        self.employee = employee
        self.late = late

    @property
    def name(self):
        return self.__name

    @property
    def empolyee(self):
        return self.__empolyee

    @property
    def late(self):
        return self.late

    @name.setter
    def name(self,name):
        self.__name = name

    @empolyee.setter
    def empolyee(self, employee):
        self.__empolyee = employee

    @late.setter
    def late(self, late):
        self.__late = late    

    def get_all_emplyees(self):
        return self.__empolyee 

    def get_emplyee(self, empid):
        return self.__empolyee[empid]

    def hire(self, employee):
        self.__empolyee = employee
        return True

    def fire(self, empid):
        emp = get_employee(empid)
        return emp

    @staticmethod    
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        pass

    def deduct(self, empid, deduction):
        late -= 10;
        pass

    def reward(self, empid, reward):
        late += 10;        
        pass

    def check_lateness(self, empid, moveHour):
        if status == 'late':
		    deduct(empid)
	    else:
            reward(empid)  
            
    @classmethod
    def change_emps_num(num):
        employee += 1
        pass    

class Car():
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    def run(self, velocity, distance):
        if self.fuelRate > 0:
            self.fuelRate -= 1
            self.velocity = velocity
        elif fuelRate == 0:
            self.stop(distance)
    
    def stop(self):
        velocity = 0
        if self.distance == distance:
            print("You arrived your distance : ".distance)
        else:
            print("The Remaining distance is : ".distance)    
        
                                                                            