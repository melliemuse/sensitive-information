# Create a class to represent a patient of a doctor's office. The Patient class will accept the following information during initialization
# Social security number
# Date of birth
# Health insurance account number
# First name
# Last name
# Address
# The first three properties should be read-only. 


class Patient:
    def __init__(self, social, birthDate, accountNumber, firstName, lastName, address):
        self.__social = social
        self.__birthDate = birthDate
        self.__accountNumber = accountNumber
        self.__firstName = firstName
        self.__lastName = lastName
        self.__address = address

        
    @property
    def social(self):
        return self.__social

    @property
    def birthDate(self):
        return self.__birthDate
            
    @property
    def accountNumber(self):
        return self.__accountNumber

# First name and last name should not be exposed as properties at all, but instead expose a calculated property of full_name. Address should have a getter and setter. 

    @property
    def fullName(self):
        return f"{self.__firstName} {self.__lastName}"

    @property
    def address(self):
            return self.__address

    @address.setter
    def address(self, newAddress):
        if type(newAddress) is str: 
            self.__address = newAddress
        else: 
            raise TypeError("Please enter a string")

    def __str__(self):
        return f"{str(self.social)} {str(self.birthDate)} {str(self.accountNumber)} {self.address} {self.fullName}"

patient = Patient("003-345-2127", "11/23/87", "443-002-4556", "Michelle", "Pfieffer", "2456 Rodeo Dr")


# # This should not change the state of the object
# patient.social_security_number = "838-31-2256"

# # Neither should this
# patient.date_of_birth = "01-30-90"

# # But printing either of them should work
# print(patient.social_security_number)   # "097-23-1003"

# # These two statements should output nothing
# print(patient.first_name)
# print(patient.last_name)

# # But this should output the full name
# print(patient.full_name)   # "Daniela Agnoletti"
patient.address = "another place"
print(patient)