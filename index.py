import time
# Reading the inventory
fd = open('Inventory.txt','r')
products = fd.read().split("\n")
fd.close()

# taking the user input
ui_username = input("Enter your Name: ")
ui_phone = input("Enter your Phone no.: ")
ui_mail = input("Enter your e-mail: ")
ui_prod_id = input("Enter product ID: ")
ui_prod_qn = input("Enter product quantity: ")

updated_product_list = []

#Going through each product detail

for product in products:
    prod_details = product.split(",")
    if prod_details[0] == ui_prod_id:
        #Checking if product exists or not 
        if(int(ui_prod_qn)<=int(prod_details[3])):
            #if we are having enough quantity
            print('-'*30)
            print("Product Name      : ", prod_details[1])
            print("Price             : ", prod_details[2])
            print("Quantity          : ", ui_prod_qn)
            print('-'*30)
            print("Billing Amount    : ", int(ui_prod_qn)* int(prod_details[2]))

            #updating inventory list
            prod_details[3] = str(int(prod_details[3])-int(ui_prod_qn))

            #Generating sales in sales.txt
            fd= open("sales.txt","a")
            sales_detail = ui_username + "," + ui_phone + "," + ui_mail + "," + prod_details[1] + "," + ui_prod_id + "," + ui_prod_qn +","+ str(int(ui_prod_qn) * int(prod_details[2]))+","+time.ctime()+ "\n"
            fd.write(sales_detail)
            fd.close()

        else:
            #If we are not having enough quantity
            print("Sorry! We are not having enough quantity.")
            print("We are having only",prod_details[3],"pieces.")
            print("Would you like to purchase it?")

            ch= input("Press Y/N: ")

            if(ch=='Y' or ch=='y'):
                 # If you want to purchase with remaining quantity
            
                print("-----------------------------")
                print("Product Name     : ", prod_details[1])
                print("Price            : ", prod_details[2]) 
                print("Quantity         : ", prod_details[3]) 
                print("-----------------------------")
                print("Billing Amount   : ", int(prod_details[3]) * int(prod_details[2]))
                print("-----------------------------")
                
                # Generating Sales in Sales.txt
                fd = open("Sales.txt",'a')
                sales_detail = ui_username +","+ ui_phone +","+ ui_mail +","+prod_details[1] +","+ ui_prod_id +","+ prod_details[3] +","+ str(int(prod_details[3]) * int(prod_details[2]))+","+time.ctime()+ "\n"
                fd.write(sales_detail)
                fd.close()
                
                # Updating Inventory list
                prod_details[3] = '0'

            else:
                print("Thanks")    

    updated_product_list.append(prod_details)

lst=[]

# Updating my Inventory String
for i in updated_product_list:
    prod = i[0] +","+  i[1] +","+ i[2] +","+ i[3] + '\n'
    lst.append(prod)

# Removing Last \n from the list
lst[-1] = lst[-1][:-1]
    

# Updating Inventory File
fd = open('Inventory.txt','w')

for i in lst:
    fd.write(i)
fd.close()

print("Inventory Updated")