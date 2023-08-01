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
  #print(tickets_list)
 
#------------------------------------------------------------   
def convertMatrixToDictionary(tickets_list): #O(N) 
  tickets_dic = {} #convert tickets_list to dictionary
  for x in range(len(tickets_list)):#O(N) where N is length of ticket_list
    key = tickets_list[x][0] #set tickID as a key
    value = [tickets_list[x][1], tickets_list[x][2], tickets_list[x][3],
tickets_list[x][4]] #set the infos as values for tickId
    tickets_dic[key] = value
  return tickets_dic
#------------------------------------------------------------
def createEventIdDic(ticket_dic):#O(N)
  ticket_dic = convertMatrixToDictionary(tickets_list)#call the method and assign its return value to ticket_dic
  #so it's O(N) where N is also length of this list
  list = []
#source to acccess dictionary elements inside a list: https://statisticsglobe.com/access-element-lists-within-dictionary-python#:~:text=The%20elements%20of%20a%20dictionary%20(which%20are%20lists%20in%20this,square%20brackets%2C%20as%20shown%20below.&text=To%20access%20the%20elements%20inside,access%20the%20elements%20inside%20them.
  for key in ticket_dic.keys(): #O(N) 
    list.append(ticket_dic[key][0])#create a list that contains only events_id
  event_dict = {}#create a dictionary that contain eventId as key and its count as value
  for j in list: #O(N)
    if j in event_dict:
      event_dict[j] +=1
    else:
      event_dict[j] =1
  #print(list)
  return event_dict
#-------------------------METHODS OF ADMIN MENU-----------------------
def displayStatistics():#O(N)
   ticket_dic = convertMatrixToDictionary(tickets_list)#O(N) n=length of ticket_list
   event_dict = createEventIdDic(ticket_dic)#call the method and assign its return value to event_dict which is the dic containing eventId as key and its count as value /it is O(N) n= nb of ticket
   max_value = max(event_dict.values()) #O(N)
   highest_eventId = [k for k, v in event_dict.items() if v ==
   max_value]#O(N) where it iterate through the dict to chek the values
  #above is to find the keys(event_id)which map the max value(its count),i used this resouce:
  #https://stackoverflow.com/questions/47861737/how-to-get-multiple-max-key-values-in-a-dictionary
   return highest_eventId
   #print(dic[key]) 

#--------------------------------------------------
def bubleSort(tickets_list):#Using Bubble Sort O(N*N)(take the max O)
  #this sort is used first to rearrange the list by 1-date(all dates) and 2-eventID
  l = len(tickets_list)
  for x in range(l):#O(N) where N is the lenght of list
    check_swap = False
    for y in range(l-x-1):#O(N*N)
      if tickets_list[y][3] > tickets_list[y + 1][3]:#here we want to compare the dateOfEvent so we put [3]
        check_swap = True
        temp = tickets_list[y]
        tickets_list[y] = tickets_list[y + 1]
        tickets_list[y + 1] = temp
      if tickets_list[y][3] == tickets_list[y+1][3]:#here if same date do the sort on event_id
        if tickets_list[y][1] > tickets_list[y + 1][1]:#bubble sort for event_id alse O(N*N)
          check_swap = True
          temp = tickets_list[y]
          tickets_list[y] = tickets_list[y + 1]
          tickets_list[y + 1] = temp
  if not check_swap: 
   return tickets_list
    
#-------------------------------------------------- 
def displayAllTickets(tickets_list,current_date): #O(N*N) where N is the len of list
  new_list = [] #here to add only the events' info from the current date and beyond and append them in a new list
  tickets_list = bubleSort(tickets_list) #O(N*N)
  for i in range(len(tickets_list)):#O(N)
    if tickets_list[i][3] >= current_date:
      new_list.append(tickets_list[i])#O(N) n=nb of elements in the l
  return new_list

#--------------------------------------------------
def changePriority(tickets_list):#O(N)
  ticket_id = input("Enter the ticket_ID to change its Priority: ")
  #priority = int(input("Enter the Priority you want to change"))
  tick_found = False 
  for i in range(len(tickets_list)):#O(N)
    if ticket_id == tickets_list[i][0]: #and priority == tickets_list[i][4]:
      new_priority = input("Enter the new Priority: ")
      tickets_list[i][4] = new_priority
      tick_found = True
      print("Priority of ticket_id:",ticket_id,"is updated to:",new_priority)
      updated_t = tickets_list[i] 
      return updated_t
      break
  if not tick_found:#here tick_found used instead of else to avoid displaying the return messge i times(outside for loop)
    return "Ticket of Id: ",ticket_id," not found!"

#--------------------------------------------------
def removeTicket(tickets_list):
  ticket_id = input("Enter the ticket_ID to remove: ")
  tick_index = -1 #to store the index of the ticket to be removed.
  for i in range(len(tickets_list)):
    if tickets_list[i][0] == ticket_id:
        tick_index = i
        break

  if tick_index != -1:
    del tickets_list[tick_index]
    print("Ticket of Id:", ticket_id, "is removed!")
  else:
    print("Ticket of Id:", ticket_id, "not found!")
    
  return tickets_list

#--------------------------------------------------
def runEvent(tickets_list, current_date): #O(N*N) (take the worst case)
  todayEvent = []
  for i in range(len(tickets_list)):#O(N) n is the length of tickets_list
    if tickets_list[i][3] == current_date:
      todayEvent.append(tickets_list[i])
      todayEvent = sorted(todayEvent, key=lambda x: int(x[4]))#O(NlogN) 
  # I convert priority to int since it is reading it as string
  #sorted() source: https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/
  #I use it instead on bubble sort since its time comlexity is O(NlogN) where after researching,I conclude that N in the number of element being sorted, and the sorted() fnc uses sorting algorithm called Timsort, which is derived from insertion sort, where it break the input into small ones and sort them using insertion sort
      print("\nToday's Event you want to remove:\n", todayEvent)
      print("\nAfter removing events of date:",current_date,":")
      print(removeValuesRecursive(tickets_list,todayEvent))# i call the fnc here bcs if it is called in main it will display the list with no deletion eveb if the date is not found
      #it is O(N*N) Since the call to removeValuesRecursive is inside the for loop
  if tickets_list[i][3] != current_date:
      print("\nThe date is not found!")
 
  return(todayEvent)
#---------------------------------------------------
def removeValuesRecursive(original_list, remove_list): #O(N), where n is the length of the original list. This is because we are iterating through each element of the original list exactly once.
    if len(original_list) == 0:#base case
        return []
    else:
        if original_list[0] in remove_list:#to check if element of index 0 in the original list is in remove list/if it exist it is true else it is false
            return removeValuesRecursive(original_list[1:], remove_list)
        else:
            return [original_list[0]] + removeValuesRecursive(original_list[1:], remove_list)
#------------------------------------------------------------

#Admin login part:
def loginAdmin(): #O(N) where n= max nb of login attempts
  max_attempt = 5
  username = "admin"
  password = "admin123"
  for i in range(max_attempt):#O(N) where n = max attempt
    name = input("Enter your username: ")
    psw = input("Enter you password: ")
    if name == username and psw == password:
      print("\nlogin Successful, you'r Welcome as Admin!")
      return True
    attempt_new = max_attempt-1 - i
    print("\nIncorrect username and/or password.You have", attempt_new,"attempts left:")
      
  print("You've exceeded the allowed login attempts!!")
  return False
#_____________________________________________________________
def adminMenu(tickets_list):
  exit_admin_menu = False
  while not exit_admin_menu:
    print(" ----- Admin Menu -----")
    print("1. Display Statistics")
    print("2. Book a Ticket")
    print("3. Display all Tickets")
    print("4. Change Ticket’s Priority")
    print("5. Disable Ticket")
    print("6. Run Events")
    print("7. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
      eventId_with_highest_tickets = displayStatistics()
      print("the events IDs with highest nb of tickets:",eventId_with_highest_tickets)
    elif choice == "2":
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
      #print(tickets_list)
    elif choice == "3":
      current_date = input("Enter the current Date (YYYYNNDD): ")
      new_list = displayAllTickets(tickets_list,current_date)
      print(new_list)
    elif choice == "4":
      t = changePriority(tickets_list)
      print(t)
    elif choice == "5":
      tickets_list = removeTicket(tickets_list)
      print(tickets_list)
    elif choice == "6":
      current_date = input("Enter the current Date (YYYYNNDD): ")
      runEvent(tickets_list, current_date)
      #print("\nToday's Event you want to remove:\n", todayEvent)
      
    elif choice == "7":
      print("\n------>You Exited!")
      exit_admin_menu = True
    else:
      print("Your choice is invalid! Try again.")

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
def saveTicket(new_ticket):#O(N) where n = nb of element in new_ticket
  #from https://stackabuse.com/reading-and-writing-lists-to-a-file-in-python/
  with open('ticket.txt', 'a') as filehandle:
    comma_separated_strings = ','.join(map(str,new_ticket))
    #from https://java2blog.com/convert-list-to-comma-separated-string-python/
    filehandle.write("\n")
    filehandle.write(comma_separated_strings) 
    
#______________________________________________________________
#User Menu Part:
def userMenu(username):#set username as parameter to userMenu() to use it in this fcn
  exit_user_menu = False
  print(" ----- Normal User Menu ----- ")
  print("1.Book a ticket")
  print("2.Exit")
  while not exit_user_menu:
    choice = input("\nEnter your choice 1 or 2: ")
    if choice == "1" :
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
      
    elif choice == "2":
      print("\n-----> You Exited!")
      exit_user_menu = True
      
    else:
      print("Invalid choice! Please try again.")
      
      
#______________________________________________________________
#Main Part:
def main():
  print("Welcome to the Ticketing System :)")
  exit_program = False
  while not exit_program:
    input_type = input("\nType A/a for Admin or U/u for normal User or E/e to exit: ")
    if input_type == "a" or input_type == "A":
      if loginAdmin():#check if the result of loginAdmin is True
        adminMenu(tickets_list)#if true, call adminMenu() fnc
      
      exit_program = True
      #break
    elif input_type == "u" or input_type == "U":
      username = loginUser()#here the username is returned from loginUser() fnc and assigned to username variable
      if username:#to check if username is not None when entering invalid pass or invalid username(empty)
        userMenu(username)#So if the condition is true(successful user login) call the userMenu() fnc and pass username as parameter to the fnc
        break
      else:
        exit_program = True
      new_ticket = userMenu(username)#here new_ticket is returned from userMenu() fnc and assigned to new_ticket variable
      if new_ticket:#same as above
        saveTicket(new_ticket)#call the saveTicket fnc and pass the new_ticket list as parameter to the saveTicket() fnc
    elif input_type == "e" or input_type == "E":
      exit_program = True
    else:
      print("\nInvalid input! Please enter A/a for Admin or U/u for normal User")

main()