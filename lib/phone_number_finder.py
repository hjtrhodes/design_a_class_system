import re

class PhoneNumberFinder():
    def __init__(self, ):
        self.phone_numbers = []
    
    
    def store_phone_number(self, diary_entry):
        number = re.findall(r"0[0-9]{10}", diary_entry.contents)
        if number not in self.phone_numbers:
            self.phone_numbers.append([str(number[0])])
# Was struggling with regex so used Kay's video to help me

    def return_phone_numbers(self):
        return self.phone_numbers