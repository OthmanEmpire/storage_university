### This program reads from two files, "RateOfPay.csv", "Timesheet.csv"
### and then calculates the total earnings of an employee

def employeesWorkingNonZeroHours():

    nonzero_hours_employees = {}

    rateofpay_dict = getRateOfPay()
    hoursworked_dict = getHoursWorked()

    for employee_number in rateofpay_dict:
        
        if(employee_number in hoursworked_dict):
            
            name_and_rate = rateofpay_dict[employee_number]
            name = name_and_rate[0]

            nonzero_hours_employees.update({employee_number:name})

    return nonzero_hours_employees

    

def getRateOfPay():

    import csv

    data = {}

    try:    
        with open("RateOfPay.csv", "r") as file:

            reader = csv.reader(file)

            for line in reader:
                
                employee_number = line[0].strip()
                employee_name = line[1].strip()
                rate_of_pay = line[2].strip()
                data[employee_number] = (employee_name, rate_of_pay)    

        return data

    except IOError as err:
        print("\n{}".format(err))



def getHoursWorked():

    import csv

    data = {}

    try:    
        with open("Timesheet.csv", "r") as file:

            reader = csv.reader(file)

            for line in reader:
                
                employee_number = line[0].strip()
                hours_worked = line[1].strip()                
                data[employee_number] = hours_worked    

        return data

    except IOError as err:
        print("\n{}".format(err))



def locateHardWorkers(hours_worked):

    hard_workers = {}

    for employee_number, hours in hours_worked.items():

        over_hours = float(hours) - 40

        if(over_hours > 0):

            hard_workers[employee_number] = over_hours

    return hard_workers



def rewardHardWorkers(rate_of_pay, hard_workers):

    reward_hard_workers = {}
    increase = 0.5      # bonus is 50% of base rate

    for employee_number in hard_workers:

        over_hours = float(hard_workers[employee_number])
        rate = float(rate_of_pay[employee_number][1])

        bonus = over_hours*rate*increase        # This bonus is added on top
                                                # of normal pay
        reward_hard_workers[employee_number] = bonus

        return reward_hard_workers

        

def weeklyPay(rate_of_pay, hours_worked, reward_hard_workers):

    weekly_pay_table = []

    for employee_number in rate_of_pay.keys():
        
        employee_name = rate_of_pay[employee_number][0]
        rate = float(rate_of_pay[employee_number][1])
        

        if employee_number in hours_worked:
            hours = float(hours_worked[employee_number])
        else:
            hours = 0
        
        
        if employee_number in reward_hard_workers:
            bonus = reward_hard_workers[employee_number]
        else:
            bonus = 0


        pay = hours*rate +  bonus


        employee_pay_data = [\
                             employee_number,
                             employee_name,
                             rate,
                             hours,
                             pay
                             ]

        weekly_pay_table.append(employee_pay_data)


    weekly_pay_table.sort()
                        
        
    return weekly_pay_table



def printWeeklyPayTable(weekly_pay_table):

    print("{:<15} | {:<12} | {} | {} | {}"\
      .format("Employee Number", "Name", "Hourly rate", "Number of hours", \
              "Total earning"))


    for employee in weekly_pay_table:
      
        print("{0[0]:<15} | {0[1]:<12} | {0[2]:<11} | {0[3]:<15} | {0[4]:<10.1f}"\
              .format(employee))



def sortAllWorkingEmployees(nonzero_hours_employees):

    all_working_employees = []
    for employee in nonzero_hours_employees.items():

        working_employee = list(employee)

        all_working_employees.append(working_employee)

    all_working_employees.sort()

    return all_working_employees




rate_of_pay = getRateOfPay()
hours_worked = getHoursWorked()

hard_workers = locateHardWorkers(hours_worked)
reward_hard_workers = rewardHardWorkers(rate_of_pay, hard_workers)

weekly_pay_table = weeklyPay(rate_of_pay, hours_worked, reward_hard_workers)
printWeeklyPayTable(weekly_pay_table)


nonzero_hours_employees = employeesWorkingNonZeroHours()
all_working_employees = sortAllWorkingEmployees(nonzero_hours_employees)

print("\nThe following employees have non-zero of work logged:")
for employee in all_working_employees:
    print(employee)




























