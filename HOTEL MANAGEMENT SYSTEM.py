table=["free"]*10
menu={
"farmhouse pizza":135,
"peri peri fries":90,
"oreo milkshake":60,
"pastry":80,
"coffee":50,
"pasta":120,
"sandwich":60,
"margherita pizza":150,
"cheese garlic bread":110,
"chocolate shake":90,
"cold drink":40,
"veg biryani":160,
"paneer tikka":180,
"noodles":130,
"manchurian":140,
"french fries":70,
"ice cream":50
}
def allocation():
    for i in range(len(table)):
        if table[i]=="free":
            table[i]="occupied"
            print(f"TABLE NUMBER {i+1} HAS BEEN ALLOTED TO YOU")
            return i+1
    print("SORRY WE HAVE NO TABLE AVAILABLE RIGHT NOW")
    return None
def print_menu():
    print("\n------MENU CARD------")
    for item,price in menu.items():
        print(f"{item} - INR {price}")
    print("-------------------------")
def take_order():
    order={}
    print("Start placing your order :")
    while True:
        item=input("Enter item name (or type 'done' to finish): ")
        item=item.lower()
        if item=="exit":
            return "exit"
        if item=="done":
            break
        if item in menu:
            qty=int(input("Enter Quantity: "))
            order[item]=qty
        else:
            print("Item not available ! Please choose again.")
    return order
def generate_bill(table_no,order):
    total=0
    filename=f"bill_table_{table_no}.txt"
    with open(filename,"w") as file:
        file.write(f"BILL FOR TABLE {table_no}\n")
        file.write("-------------------------------\n")
        for item,qty in order.items():
            amount=menu[item]*qty
            total+=amount
            file.write(f"{item} x {qty} = INR {amount}\n")
        file.write("-------------------------------\n")
        file.write(f"TOTAL AMOUNT = INR {total}\n")
    print(f"\nBill generated successfully: {filename}")
    print(f"TOTAL PAYABLE = INR {total}")
def free_table(table_no):
    table[table_no-1]="free"
    print(f"TABLE {table_no} IS NOW FREE")
def main():
    while True:
        print("=======================================")
        print("     WELCOME TO HOTEL MANAGEMENT       ")
        print("=======================================")
        choice=input("Type 'start' to continue or 'exit' to quit: ")
        if choice.lower()=="exit":
            print("Program Ended.")
            break
        t=allocation()
        if t is None:
            break
        print_menu()
        order=take_order()
        if order=="exit":
            print("Program Ended.")
            break
        if len(order)==0:
            print("No items ordered. Exiting...")
            continue
        generate_bill(t,order)
        paid=input("Did the customer pay the bill? (yes/no): ")
        if paid.lower()=="yes":
            free_table(t)
        print("\nTHANK YOU FOR VISITING!\n")
main()
