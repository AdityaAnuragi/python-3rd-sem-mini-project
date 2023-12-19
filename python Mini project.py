class User:
  def __init__(self,user_name, user_id, school_name, address, phone_no, email_id, dob, age):
    self.user_name = user_name
    self.user_id = user_id
    self.school_name = school_name
    self.address = address
    self.phone_no = phone_no
    self.email_id = email_id
    self.dob = dob
    self.age = age

  def setUserName(self,newData):
    self.user_name = newData

  def setUserId(self,newData):
    self.user_id = newData

  def setSchoolName(self,newData):
    self.school_name = newData

  def setAddress(self,newData):
    self.address = newData

  def setPhoneNo(self,newData):
    self.phone_no = newData

  def setEmailId(self,newData):
    self.email_id = newData

  def setDob(self,newData):
    self.dob = newData

  def setAge(self,newData):
    self.age = newData


allUsers = []

allUsers.append(User("Aditya","001","reva","address1",1,"aditya@mail.com","1st Jan",10))
allUsers.append(User("Benjamin","002","reva","address2",2,"benjamin@mail.com","2nd Feb",20))
allUsers.append(User("Connor","003","reva","address3",3,"connor@mail.com","3rd Mar",30))
allUsers.append(User("Dave","004","reva","address4",4,"dave@mail.com","4th Apr",40))
allUsers.append(User("Eve","005","reva","address5",5,"eve@mail.com","5th May",50))

allUsers.append(User("Franklin","006","reva","address6",6,"franklin@mail.com","6th June",60))
allUsers.append(User("Gerald","007","reva","address7",7,"gerald@mail.com","7th July",70))
allUsers.append(User("Hank","008","reva","address8",8,"hank@mail.com","8th Aug",80))
allUsers.append(User("Ivan","009","reva","address9",9,"ivan@mail.com","9th Sept",90))
allUsers.append(User("James","010","reva","address10",10,"james@mail.com","10th Oct",100))

def addUser():
  global allUsers

  print("Enter user_name, user_id, school_name, address, phone_no, email_id, dob, age")
  user_name = input("")
  user_id = input("")
  school_name = input("")
  address = input("")
  phone_no = int(input(""))
  email_id = input("")
  dob = input("")
  age = int(input(""))

  allUsers.append(User(user_name, user_id, school_name, address, phone_no, email_id, dob, age))

def deleteUser():
  nameToDelete = input("Enter name of user to delete ")
  for i in range(0,len(allUsers)):
    if(nameToDelete == allUsers[i].user_name):
      allUsers.pop(i)
      break
  
def editUser():
  nameToEdit = input("Enter name of user to edit ")
  
  for i in range(0,len(allUsers)):
    if(nameToEdit == allUsers[i].user_name):
      whatToEdit = input("which property to edit user_name, user_id, school_name, address, phone_no, email_id, dob, age ")
      newValue = input("Enter new data ")

      if (whatToEdit == "user_name"):
        allUsers[i].setUserName(newValue)

      elif (whatToEdit == "user_id"):
        allUsers[i].setUserId(newValue)

      elif (whatToEdit == "school_name"):
        allUsers[i].setSchoolName(newValue)

      elif (whatToEdit == "address"):
        allUsers[i].setAddress(newValue)

      elif (whatToEdit == "phone_no"):
        allUsers[i].setPhoneNo(newValue)

      elif (whatToEdit == "email_id"):
        allUsers[i].setEmailId(newValue)

      elif (whatToEdit == "dob"):
        allUsers[i].setDob(newValue)

      elif (whatToEdit == "setAge"):
        allUsers[i].setUserId(newValue)
      
      else:
        print("invalid choice")

def display():
  for i in allUsers:
    print(i.user_name, i.user_id, i.school_name, i.address, i.phone_no, i.email_id, i.dob, i.age)

while(True):
  print("1 - add user")
  print("2 - delete user")
  print("3 - edit user")
  print("4 - display")
  print("5 - exit")

  choice = int(input(""))

  if(choice == 1):
    addUser()

  elif(choice == 2):
    deleteUser()

  elif(choice == 3):
    editUser()
  
  elif(choice == 4):
    display()
  
  else:
    break

myFile = open(r"./pythonProjectFile.txt","w")

for user in allUsers:
  tempArr = []
  tempArr.extend([str(user.user_name), str(user.user_id), str(user.school_name), str(user.address), str(user.phone_no), str(user.email_id), str(user.dob), str(user.age)+'\n'])
  myFile.writelines(tempArr)

myFile.close()
