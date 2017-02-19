def checkBaggage(baggage_amount):
    if (baggage_amount >= 0 and baggage_amount <= 40):
        return True
    else:
        return False

def checkImmigration(expiryYear):
    if (expiryYear >= 2001 and expiryYear <= 2025):
        return True
    else:
        return False
    
def checkSecurity(noc_status):
    if (noc_status):
        return True
    else:
        return False
    
def traveller():
    traveller_id = 1001
    traveller_name = "Jim"
    baggageAmount = 35
    expiryYear = 2019
    nocStatus = True
    if (checkBaggage(baggageAmount) and checkImmigration(expiryYear) and checkSecurity(nocStatus)):
        print("Traveller ID : ",traveller_id,"Traveller Name : ",traveller_name)
        print("Allow Traveller to fly.")
    else:
        print("Traveller ID : ",traveller_id,"Traveller Name : ",traveller_name)        
        print("Detain Traveller for Re-checking")
        
traveller();
        