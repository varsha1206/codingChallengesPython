from datetime import datetime, timedelta
import random

class Patient:
    def __init__(self, id = 1, test_date = "not yet tested"):
        self.id = id
        self.test_date = test_date
    
    def update_test_date(self,updated_date):
        self.test_date = updated_date

    def printing_details(self):
        print(f'Patient {self.id} was last tested on {self.test_date}')



def creating_batches(batch_size, patient_list):
    random.shuffle(patient_list)
    return [patient_list[i:i + batch_size] for i in range(0, len(patient_list), batch_size)]

def show_testing_history(patient_list):
    for patient in patient_list:
        patient.printing_details()