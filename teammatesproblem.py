teammates_names={
                 1:"tarun",
                 2:"Chai",
                 3:"Priya",
                 4:"Debbie",
                 5:"Jason",
                 6:"Sunil",
                 7:"Maria",
                 8:"Geoff",
                }

numberOfTeammates=6
numberOfWorkingDaysInAWeek=5
numberOfDaysToPrintResult=2
output_office_teammates={}

numberOfTeammatesInOffice=(numberOfTeammates/2)

for x in range(1, numberOfDaysToPrintResult+1):
    teammates_per_day={}
    for id, name in enumerate(teammates_names):
       # print(teammates_names[name])
        if not id in teammates_per_day and (len(teammates_per_day)<=numberOfTeammatesInOffice):

            # each teammate should not repeat for more that numberOfDaysToPrintResult/2
            # check if the teammate is already repeated for n/2 days 
    

            teammates_per_day[id] = teammates_names[name]
    output_office_teammates[x] = teammates_per_day

print(output_office_teammates)
    
    