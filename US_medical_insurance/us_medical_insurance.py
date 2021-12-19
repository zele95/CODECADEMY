# import libraries

import csv
from statistics import mean
from matplotlib import pyplot as plt




# import all data from csv to lists

with open('insurance.csv') as ins:
    insurance_dict = csv.DictReader(ins)
    
    age_list = []
    sex_list = []
    bmi_list = []
    children_list = []
    smoker_list = []
    region_list = []
    charges_list = []
    
    for row in insurance_dict:
        age_list.append(row['age'])
        sex_list.append(row['sex'])
        bmi_list.append(row['bmi'])
        children_list.append(row['children'])
        smoker_list.append(row['smoker'])
        region_list.append(row['region'])
        charges_list.append(row['charges'])
   

# construct a class for patient data

class PatientsData:
    def __init__(self,ages,sexes,bmis,num_children,smoker_stats,regions,charges):
        self.ages = ages
        self.sexes = sexes
        self.bmis = bmis
        self.num_children = num_children
        self.smoker_stats = smoker_stats
        self.regions = regions
        self.charges = charges

    def analyze_age(self):
        # compute average patients age
        avg_age = round(mean(map(int,self.ages)),2)
        print('Average patient age is',avg_age,'years.')
        
        # what is the average age for someone who has at least one child
        age_with_child = []
        for i in range(len(children_list)):
            child = int(children_list[i])
            age = int(age_list[i])
            if  child:
                age_with_child.append(age)
        child_age_avg = mean(age_with_child)
        print('Average age of patients with at least one child is',round(child_age_avg,2))


        

    def cost_average(self):
        avg_cost = round(mean(map(float,self.charges)),2)
        print('Average patient charge is',avg_cost,'dollars.')
        return avg_cost

    def children_average(self):
        avg_chidren = round(mean(map(int,self.num_children)),2)
        print('Average number of children of the patients is',avg_chidren)
        return avg_chidren

    def analyze_regions(self):
        region_count = {}
        for region in self.regions:
            if region in region_count:
                region_count[region] += 1
            else:
                region_count[region] = 1
        most_patients_region = max(region_count, key = region_count.get)
        print('Patients are from following regions:',', '.join(list(region_count.keys())))
        print('Most patients are from', most_patients_region + 'ern region.')
        return most_patients_region

    def males_vs_females(self):
        males = 0
        females = 0
        for sex in self.sexes:
            if sex == 'female':
                females += 1
            else:
                males += 1
        print('There are', females, 'female and', males,'male patients.' )

    def analyze_smokers(self):
        smokers = 0
        nsmokers = 0
        nsmoker_cost = []
        smoker_cost = []
        smokers_bmi = []
        nsmokers_bmi = []
        for i in range(len(self.smoker_stats)):
            smoker = self.smoker_stats[i]
            cost = float(charges_list[i])
            if  smoker == 'no':
                nsmokers += 1
                nsmoker_cost.append(cost)
                nsmokers_bmi.append(float(self.bmis[i]))
            else:
                smokers += 1
                smoker_cost.append(cost)
                smokers_bmi.append(float(self.bmis[i]))
        smoker_avg = round(mean(smoker_cost),2)
        nsmoker_avg = round(mean(nsmoker_cost),2)
        print('There are', smokers, 'patients that smoke and', nsmokers,'that don\'t.' )
        print('Average cost of smoking patients is',smoker_avg,'dollars while for non smoking patients it is',nsmoker_avg,'dollars.')
        return smokers, nsmokers, smokers_bmi, nsmokers_bmi

    def analyze_bmi(self):
        _,_,smokers_bmi,nsmokers_bmi = self.analyze_smokers()
        avg_smoke_bmi = mean(smokers_bmi)
        avg_nsmoke_bmi = mean(nsmokers_bmi)
        if avg_nsmoke_bmi > avg_smoke_bmi:
            print('In average, a non-smoker person has a higher BMI.')
        elif avg_nsmoke_bmi < avg_smoke_bmi:
            print('In average, a smoker person has a higher BMI.')
        else:
            print('There is no difference between BMI in smokers and non-smokers.')


    def create_dictionary(self):
        self.patients_dict = {}
        self.patients_dict['age'] = list(map(int,self.ages))
        self.patients_dict['sex'] = self.sexes
        self.patients_dict['bmi'] = self.bmis
        self.patients_dict['children'] = list(map(int,self.num_children))
        self.patients_dict['smoker'] = self.smoker_stats
        self.patients_dict['regions'] = self.regions
        self.patients_dict['charges'] = list(map(float,self.charges))
        return self.patients_dict




# create patients data object
patients = PatientsData( age_list,sex_list,bmi_list,children_list,smoker_list,region_list,charges_list)


# analyze age of the patients
patients.analyze_age()

# average of the patients age 
patients.cost_average()

# average of number of children
patients.children_average()

# what are the regions of the patients and which are the most from 
patients.analyze_regions()

# count of the male and female patients
patients.males_vs_females()

# different cost between smokers and non smokers
patients.analyze_smokers()

# analyze smokers BMI
patients.analyze_bmi()

# create a dictionary with th epatients data
patients_dict = patients.create_dictionary()
print(patients_dict['age'])




f,ax = plt.scatter(patients.ages,patients.charges)
ax.set_yticks([x*10000 for x in range(1, 7)])
plt.show()