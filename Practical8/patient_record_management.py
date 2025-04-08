class patients(object):
    def __init__(self,name,age,date_of_latest_admission,medical_history):
        self.name=name
        self.age=age
        self.date_of_latest_admission=date_of_latest_admission
        self.medical_history=medical_history
    def print_details(self):
        print(f'Name: {self.name}, Age: {self.age}, Date of latest admission: {self.date_of_latest_admission}, Medical history: {self.medical_history}')
patient=patients('JQJ',19,'April 8','healthy')
patient.print_details()
