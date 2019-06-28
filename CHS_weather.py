import csv
from datetime import datetime

with open('1781298.csv', 'r') as readFile, open('seabreeze_hourly_data_2000-2009.csv', mode='w') as new_hourly_csv, open('Pressure_Tendancy_Am_Change_Dates_2000-2009.csv', mode='w') as press_csv:
    reader = csv.DictReader(readFile) 
    
    writer = csv.writer(new_hourly_csv)
    writer2 = csv.writer(press_csv)
    i = 0

    for row in reader:

        i += 1
        
        if i == 1:
            writer.writerow(row)

        date = row['DATE']

        time_part = date.split('T')

        observ_date = time_part[0]

        observ_time = time_part[1]

        time = datetime.strptime(observ_time, "%H:%M:%S")

        ten_am = datetime.strptime('10:50:00', "%H:%M:%S")

        six_pm = datetime.strptime('18:00:00', "%H:%M:%S")

        seven_am = datetime.strptime('07:00:00', "%H:%M:%S")

        eleven_am = datetime.strptime('11:00:00', "%H:%M:%S")

        ## hourly wind direction cleaner
        if (row['HourlyWindDirection'] == 'VRB') or row['HourlyWindDirection'] == '':
            
           hourly_wD = 0
           
        else:
            hourly_wD = int(row['HourlyWindDirection'])
            
        ## hourly wind speed cleaner
        if row['HourlyWindSpeed'] == '':
           hourly_wS = 0
        elif row['HourlyWindSpeed'] == '28s':
           hourly_wS = 28
        else:
            hourly_wS = int(row['HourlyWindSpeed'])

        ## pressure tendency cleaner
        if row['HourlyPressureTendency'] == '':
            hourly_pressT = -1
        else:
            hourly_pressT = int(row['HourlyPressureTendency'])
            
        ## Case for Pressure tendency in AM before seabreeze       
        if time > seven_am and time < eleven_am:

            if hourly_pressT == 0 or hourly_pressT == 4 or hourly_pressT == 6 or hourly_pressT == 7 or hourly_pressT == 8:

                writer2.writerow(row.values())

##                print(date, hourly_pressT)

                continue

        ## Case for seabreeze based on hourly data of wind speed and direction between 10am and 6pm 
        if time > ten_am and time < six_pm:

            if (hourly_wD < 175) and (hourly_wD > 140):

                if (hourly_wS < 18) and (hourly_wS > 6):

##                    print(observ_date, observ_time + " Seabreeze test Passed - Hourly Data is as Follows: " + '\n' + "HourlyStationPressure: " + row['HourlyStationPressure'] + '\n' + "HourlyWindDirection: " + row['HourlyWindDirection'] + '\n' + "HourlyWindSpeed: " + row['HourlyWindSpeed'])
                    
                    writer.writerow(row.values())                   
                    

            
            

