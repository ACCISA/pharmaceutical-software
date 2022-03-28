print("==============================")
print("---------Protoype XBD---------")
print("------------------------------")
print("------You have logged in------")
print("------------------------------")
print("-------------Menu-------------")
print("==============================")
print("------ 1. User Database ------")
print("------ 2. Storage Menu  ------")
print("------ 3. Clients Menu  ------")
print("------ 4. Start Process ------")
print("==============================")



Menus = [1, 2, 3, 4]

while True:
    h = print("Awaiting Input...")

    x = input()


    if int(x) in Menus:
        if int(x) == 1:
            exec(open("user_database.py").read())
            break
        if int(x) == 2:
            exec(open("storage_menu.py").read())
            break
        if int(x) == 3:
            exec(open("Client DB\client_database.py").read())
            break
        if int(x) == 4:
            exec(open("Process\process_order.py").read())
            break
    if int(x) not in Menus:
        print("Invalid Input")
        continue
