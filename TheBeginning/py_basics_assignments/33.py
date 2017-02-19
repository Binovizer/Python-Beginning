furniture_list = [("SofaSet",20000),("Dining Table",8500),("TV stand",4599),("Cupboard",13920)]

fur_name = input("Enter the Name of furniture You want to buy : ").strip()

for fur_tuple in furniture_list:
    if (fur_tuple[0].lower() == fur_name.lower()):
        price = fur_tuple[1]
        print("\nFurniture Name : ",fur_tuple[0],", Price : ",price)
        no = int(input("\nEnter Quantity : ").strip())
        bill_amount = price * no;
        print("\nFurniture Name : ",fur_tuple[0],", Price : ",price)
        print("Quantity : ",no)
        print("Bill Amount : ",bill_amount)
        print("Thank You for Shopping With Us ;)")
        break;
else:
    print("No Results Found")
