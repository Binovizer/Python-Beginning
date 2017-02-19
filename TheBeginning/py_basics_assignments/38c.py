def compare(blr_to_mys, blr_to_mlr):
    if (blr_to_mlr < blr_to_mys):
        print("Mysore is far from Banglore compared to Manglore")
    elif (blr_to_mlr > blr_to_mys):
        print("Manglore is far from Banglore compared to Mysore")
    else :
        print("Both Manglore and Mysore is Equidistant from Banglore")
        
compare(506, 1790) # Required Arguments
compare(blr_to_mys=506, blr_to_mlr=1790) # Keyword Arguments
