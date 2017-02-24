# Classes : Customer, Employee, Items
'''
    Customer Class
        Attributes : 
            Id
            Name
            Address
            Type of Customer(Regular, Card Holder)
    
    Card Class
        Attributes : 
            Card Id 
            Name of Holder
            Date of Issue
            Expiry Date
            Type of Card (Gold, Silver, Platinum)
    
    Employee Class
        Attributes:
            ID
            Name
            Type of employee(Regular or not)
    
    Item Class
        Attributes :
            Id
            Name
            Price
            Discount
            Type of item
            No of items available
    
    Billing Class
        Attributes :
            sales_tax = x%
            credit_card_processing_charge = 2%
        Methods :
            checkCustomerType(CustomerID)
            calculateBill(CustomerType)
            payment(bill, mode='Cash')
            payment(bill, mode='Credit Card')
            calculateTotalBill(bill_from_payment)
            
            
'''