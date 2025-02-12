from functions import * 

#Getting number of patients and testing_batch_size
number_of_patients = int(input("Enter the number of patients: "))
batch_size = int(input("Enter the batch size: "))

#Initializing Patient class objs
patient_list = [Patient(i) for i in range(number_of_patients)]

#Grouping them into batches
batches = creating_batches(batch_size,patient_list)

#Giving time to patients from lockdown to recover
start_date = datetime(2022, 1, 1)
end_date = datetime.today()

#Choosing one from each batch and testing
for batch in batches:
    current_patient = random.choice(batch)
    print(f'The patient chosen to test is: {current_patient.id}')
    random_days = random.randint(0, (end_date - start_date).days)
    date_tested = start_date + timedelta(days=random_days)
    current_patient.update_test_date(date_tested.strftime("%Y-%m-%d"))

print("\nTesting History of Patients:")

show_testing_history(patient_list)
    







