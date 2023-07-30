#1)read tickets from the text file named ticket.txt and store them in a list named ticketsList
#read from file resource (how to read a file into a list):  https://pythonhow.com/how/read-a-file-line-by-line-into-a-list/#:~:text=lines%20print(lines)-,To%20read%20a%20file%20line%2Dby%2Dline%20into%20a%20list,method%20of%20the%20file%20object.&text=In%20both%20cases%2C%20the%20list,of%20the%20file%20as%20elements.
tickets_list = [] 
with open('ticket.txt', 'r') as file:
  # Create an empty list to store the lines
  # Iterate over the lines of the file
  for line in file:
    # Remove the newline character at the end of the line
    line = line.strip().split(",")
    # Append the line to the list
    tickets_list.append(line)
#------------------------------------------------------------   
def convertMatrixToDictionary(tickets_list):
  tickets_dic = {} #convert tickets_list to dictionary
  for x in range(len(tickets_list)):
    key = tickets_list[x][0]
    value = [tickets_list[x][1], tickets_list[x][2], tickets_list[x][3],
tickets_list[x][4]]
    tickets_dic[key] = value
  return tickets_dic
#------------------------------------------------------------
def createEventIdDic(ticket_dic):
  ticket_dic = convertMatrixToDictionary(tickets_list)#call the method andassign its return value to ticket_dic
  list = []
#source to acccess dictionary elements inside a list: https://statisticsglobe.com/access-element-lists-within-dictionary-python#:~:text=The%20elements%20of%20a%20dictionary%20(which%20are%20lists%20in%20this,square%20brackets%2C%20as%20shown%20below.&text=To%20access%20the%20elements%20inside,access%20the%20elements%20inside%20them.
  for key in ticket_dic.keys():
    list.append(ticket_dic[key][0])#create a list that contains only events_id
  event_dict = {}#create a dictionary that contain eventId as key and its count as value
  for j in list:
    if j in event_dict:
      event_dict[j] +=1
    else:
      event_dict[j] =1
  #print(list)
  return event_dict
#-------METHODS OF ADMIN MENU-----------
def displayStatistics():
   ticket_dic = convertMatrixToDictionary(tickets_list)
   event_dict = createEventIdDic(ticket_dic)#call the method and assign its return value to event_dict
   max_value = max(event_dict.values()) #https://www.entechin.com/how-to-find-the-max-value-in-a-dictionary-in-python/?expand_article=1
   highest_eventId = [k for k, v in event_dict.items() if v == 
   max_value]#https://stackoverflow.com/questions/47861737/how-to-get-multiple-max-key-values-in-a-dictionary
   return highest_eventId

    #print(dic[key]) 
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
def adminMenu(tickets_list):
  while True:
    print(" ----- Admin Menu -----")
    print("1. Display Statistics")
    print("2. Book a Ticket")
    print("3. Display all Tickets")
    print("4. Change Ticket’s Priority")
    print("5. Disable Ticket")
    print("6. Run Events")
    print("7. Exit")
    choice = eval(input("Enter your choice: "))
    if choice == 1:
      eventId_with_highest_tickets = displayStatistics()
      print(eventId_with_highest_tickets)
    if choice == 2:
      id_incr = (len(tickets_list)+1) + 1 #automatically increment ticket ID
      ticket_id = "tick1" + str(id_incr) 
      event_id = input("Enter the Event ID: ")
      username = input("Enter your name: ")
      timestamp = input("Enter the Event date(YYYYMMDD): ")
      priority = int(input("Enter the Priority: ")) 
      new_ticket = [ticket_id,event_id,username,timestamp,priority]
      tickets_list.append(new_ticket)
      print("Ticket booked succesfully")
      print(new_ticket)
    #if choice == 3:
      
    
      
    
  

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
    print(" ----- Normal User Menu ----- ")
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
        adminMenu(tickets_list)#if true, call adminMenu() fnc
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