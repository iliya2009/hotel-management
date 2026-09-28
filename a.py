#برنامه مدیریت مسافرخانه کوچک
import json
mosaferan = []
room=[1 , 2 , 3 , 4 , 5]
def first():
    name = input("please enter your name: ") 
    print(room)
    while 1 :
                  try:
                     ch=int(input("pleas enter your room :"))
                  except:
                     print("Please select one of the rooms.")
                     continue
                  if ch in room:
                        room.remove(ch)                       
                        mosaferan.append({"name":name,"room":ch})
                        save()
                        break
                  else:
                    print("The room number is invalid; please select one of the available rooms.")

  
def mis():
    if not mosaferan :
        print("list is empity")
        return
    for passenger in mosaferan:
        print(f"name:{passenger['name']}-room:{passenger['room']}")

def hazf():
    name=input("please enter name tou want remove:")
    found= False
    for passenger in mosaferan:
        if passenger ["name"] == name:
                found = True
                room_number=passenger["room"]
                room.append(room_number)
                mosaferan.remove(passenger)
                print(passenger," removed")
                save()
                break
    if not found :
            print("not found")


def end():
    print("good bye")

def menu():
    while 1 :
        try :
         x=int(input(" add 1 , remive 2 , show 3 , exit 4 :"))
        except:
         print("Please enter one of the options as a number.")
         continue
        if x == 1 :
            first()
        elif x == 2 :
            hazf()
        elif x == 3 :
            mis()
        elif x == 4 :
            end()
            break
        else:
            print("Please enter one of the options as a number.")

def save():
    data={
        "mosaferan": mosaferan,
        "room": room

    }
    with open("Hotel.json","w") as f:
        json.dump(data , f ,  indent=4)

def load():
    global mosaferan , room
    try:
        with open("Hotel.json","r") as f :
            data=json.load(f)
            mosaferan=data["mosaferan"]
            room=data["room"]
    except:
        pass

load()
menu()




            