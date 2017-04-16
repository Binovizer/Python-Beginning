import uuid
class Address:
    
    def __init__(self, line_1 = None, line_2 = None, city = None, state = None, pincode = None):
        if(line_1 is not None):
            self.line1 = line_1
        if(line_2 is not None):
            self.line2 = line_2
        if(city is not None):
            self.city = city
        if(state is not None):
            self.state = state
        if(pincode is not None):
            self.pincode = pincode

    def get_address_id(self):
        return self.__address_id


    def set_address_id(self, value = None):
        if(value is None):
            self.__address_id = uuid.uuid4()
        else:
            self.__address_id = value

    def del_address_id(self):
        del self.__address_id


    def get_line_1(self):
        return self.__line1


    def get_line_2(self):
        return self.__line2


    def get_city(self):
        return self.__city


    def get_state(self):
        return self.__state


    def get_pincode(self):
        return self.__pincode


    def set_line_1(self, value):
        self.__line1 = value


    def set_line_2(self, value):
        self.__line2 = value


    def set_city(self, value):
        self.__city = value


    def set_state(self, value):
        self.__state = value


    def set_pincode(self, value):
        self.__pincode = value


    def del_line_1(self):
        del self.__line1


    def del_line_2(self):
        del self.__line2


    def del_city(self):
        del self.__city


    def del_state(self):
        del self.__state


    def del_pincode(self):
        del self.__pincode

    line1 = property(get_line_1, set_line_1, del_line_1, "line1's docstring")
    line2 = property(get_line_2, set_line_2, del_line_2, "line2's docstring")
    city = property(get_city, set_city, del_city, "city's docstring")
    state = property(get_state, set_state, del_state, "state's docstring")
    pincode = property(get_pincode, set_pincode, del_pincode, "pincode's docstring")
    
    def __str__(self):
        return "Address Line 1: "+self.get_line_1()+" \nAddress Line 2: "+self.get_line_2()+" \nCity: "+self.get_city()+" \nState: "+self.get_state()+" \nPincode: "+self.get_pincode()
    address_id = property(get_address_id, set_address_id, del_address_id, "address_id's docstring")
    