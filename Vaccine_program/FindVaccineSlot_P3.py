#!/usr/bin/python -tt
#pip install requests
print ("We will overcome this - Saurabh Wasule")
import winsound
import requests, sys
import time
from datetime import date
import json

    
def alert():
	frequency = 4500
	duration = 500000
	winsound.Beep(frequency, duration)
    
def checkVaccineAvailability(pinC):
    
    if (pinC.isdigit() and len(pinC)) == 6:
        pinCode = str(pinC)
        searchDate = date.today().strftime("%d-%m-%Y")
	
        param1 = {'pincode' : pinCode, 'date' : searchDate}
	
        resp1 = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin", headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36","Referer":"https://www.cowin.gov.in/"}, params = param1)
        data = json.loads(resp1.text)
		
        for ele in data['centers']:
            if str(ele['fee_type']) == 'Paid': 
                hospitalAddress = ele['address']	
                vacCost = (ele['vaccine_fees'])[0]['fee']
                vacName = (ele['vaccine_fees'])[0]['vaccine']
                print ("Hospital Name: " + str(ele['name'])) + "\n"
                print ("Hospital Address: " + str(hospitalAddress)) + "\n"
                print ("Charge: " + str(vacCost)) + "\n"
                print ("Vaccine Name: " + str(vacName)) + "\n"
				
                for counter in ele['sessions']:
                    print ("Available Vaccine count: " + str(counter['available_capacity']))
                    if int(counter['available_capacity']) > 0 and int(counter['min_age_limit']) == 18:
                        print ("Date: " + str(counter['date']))
                        print ("Min Age Limit: " + str(counter['min_age_limit']))
                        print ("Available Slots: ") + "\n"
                        for slot in counter['slots']:
                            print (slot)
                        alert()
                    print ("Date: " + str(counter['date']))
                    print ("Min Age Limit: " + str(counter['min_age_limit']))
                    print ("Available Slots: ") + "\n"
                    for slot in counter['slots']:
                        print (slot)
                    print ("\n\n")
            else:
                hospitalAddress = ele['address']	
                print ("Hospital Name: " + str(ele['name']) + "\n")
                print ("Hospital Address: " + str(hospitalAddress) + "\n")
                print ("Charge: " + '0'+ "\n")
                print ("Vaccine Name: " + str(ele['sessions'][0]['vaccine']) + "\n")

                for counter in ele['sessions']:
                    print ("Available Vaccine count: " + str(counter['available_capacity']))
                    if int(counter['available_capacity']) > 0 and int(counter['min_age_limit']) == 18:
                        print ("Date: " + str(counter['date']))
                        print ("Min Age Limit: " + str(counter['min_age_limit']))
                        print ("Available Slots: " + "\n")
                        for slot in counter['slots']:
                            print (slot)
                        alert()
                    print ("Date: " + str(counter['date']))
                    print ("Min Age Limit: " + str(counter['min_age_limit']))
                    print ("Available Slots: " + "\n")
                    for slot in counter['slots']:
                        print (slot)
					
                    print ("\n\n")
                    #choice = input("Press Y to search for any other Pincode\n")
                    #while(choice.casefold()=='y'):
                     #   pinCode = input("Enter Pin code you wish to search\n")
                      #  checkVaccineAvailability(pinCode)
					
                #sys.exit(0)
    else:
        print ("Please enter a valid PINCODE\n")
        sys.exit(0)
        
    time.sleep(10)

pinCode = input("Enter Pin code you wish to search\n")
while True:
    checkVaccineAvailability(pinCode)
