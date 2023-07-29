#1)read tickets from the text file named ticket.txt and store them in a list named ticketsList
#read from file resource (how to read a file into a list): https://favtutor.com/blogs/read-file-line-by-line-python
tickets_list = []
with open("ticket.txt" , "r") as file:
  for line in file:
    tickets_info = line.strip().split(", ")#.split() to convert the string here to a list
    tickets_list.append(tickets_info)  
#------------------------------------------------------------   
#2)create a dictionary with unique ticket IDs
# tickets_dict = {}
# for ticket_info in tickets_list:
#   ticket_id = ticket_info[0]
#   tickets_dict[ticket_id] = {
#      ticket_info[1],
#      ticket_info[2],
#      ticket_info[3],
#      int(ticket_info[4]) #priotiy here is an integer as asked
#   }
 
#------------------------------------------------------------
#Admin login part:
def loginAdmin():
  max_attempt = 5
  username = "admin"
  password = "admin123"
  for i in range(max_attempt):
    name = input("Enter your username: ")
    psw = input("Enter you password: ")
    if name == username and psw == password:
      print("login Successful, you'r Welcome as Admin!")
      return True
    attempt_new = max_attempt-1 - i
    print("Incorrect username and/or password.You have", attempt_new,"attempts left:")
      
  print("You've exceeded the allowed login attempts!!")
  return False
#_____________________________________________________________
def adminMenu():
  return None
  

#_____________________________________________________________
#User login part:
def loginUser():#return username
  while True:
    username = input("Enter your username: ")
    psw = input("Enter you password(leave empty if you are a normal user): ")
    if psw == "" and username != "":
      print("Login Successful. Welcome", username,"!")
      return username
    else:
      print("Incorrect password or empty username for normal user!\nleave Password empty to login as normal user")

#______________________________________________________________
def saveTicket(new_ticket): #from https://stackabuse.com/reading-and-writing-lists-to-a-file-in-python/
  with open('ticket.txt', 'a') as filehandle:
    comma_separated_strings = ','.join(map(str,new_ticket))
    #from https://java2blog.com/convert-list-to-comma-separated-string-python/
    filehandle.write("\n")
    filehandle.write(comma_separated_strings) 
    
#______________________________________________________________
#User Menu Part:
def userMenu(username):#set username as parameter to userMenu() to use it in this fcn
  while True: #To display the menu again multiple times
    print("Normal User Menu:")
    print("1.Book a ticket")
    print("2.Exit")
    choice = eval(input("Enter your choice 1 or 2: "))
    if choice == 1:
      id_inc = (len(tickets_list)+1) + 1 #automatically increment ticket ID
      ticket_id = "tick1" + str(id_inc) 
      event_id = input("Enter the Event ID: ")
      timestamp = input("Enter the Event date(YYYYMMDD): ")
      priority = 0 
      new_ticket = [ticket_id,event_id,username,timestamp,priority]
      tickets_list.append(new_ticket)
      print("Ticket booked succesfully")
      print(tickets_list)
      saveTicket(new_ticket)
      
    elif choice == 2:
      print("----> You Exited!")
      break
    else:
      print("Invalid choice! Please try again.")
      
#______________________________________________________________
#Main Part:
def main():
  print("Welcome to the Ticketing System :)")
  while True:
    input_type = input("Type A/a for Admin or U/u for normal User: ")
    if input_type == "a" or input_type == "A":
      if loginAdmin():#check if the result of loginAdmin is True
        adminMenu()#if true, call adminMenu() fnc
      else:#if return false
        break
    elif input_type == "u" or input_type == "U":
      username = loginUser()#here the username is returned from loginUser() fnc and assigned to username variable
      if username:#to check if username is not None when entering invalid pass or invalid username(empty)
        userMenu(username)#So if the condition is true(successful user login) call the userMenu() fnc and pass username as parameter to the fnc
        break
      new_ticket = userMenu(username)#here new_ticket is returned from userMenu() fnc and assigned to new_ticket variable
      if new_ticket:#same as above
        saveTicket(new_ticket)#call the saveTicket fnc and pass the new_ticket list as parameter to the saveTicket() fnc
    else:
      print("Invalid input! Please enter A/a for Admin or U/u for normal User")

main()