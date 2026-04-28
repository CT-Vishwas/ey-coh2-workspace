# When we start the program first we need a list to store
ip_list = []

# Add, Remove, Search, quit
# Print a menu
while True:
    print("1.Add an IP\n2.Remove an IP\n3.Search an IP\n4.Quit")

    choice = input("Enter a choice: ")

    if choice == "1":
        ip = input("Enter the IP Address: ")
        ip_list.append(ip)
    elif choice == "2":
        ip = input("Enter the IP Address: ")
        if len(ip_list) == 0:
            print("cannot remove the ip, list empty")
        
        for idx in range(len(ip_list)):
            if ip_list[idx] == ip:
                del ip_list[idx]
                break
    elif choice == "3":
        ip = input("Enter the IP Address: ")
        for idx in range(len(ip_list)):
            if ip_list[idx] == ip:
                print(f"{ip} is found in records")

        print(f"{ip} is not found")
    elif choice == "4":
        print("Aborting......")
        break
    else:
        print("Enter Valid Choice")
