#!/usr/bin/python -tt
#pip install requests
print ("We will overcome this - Saurabh Wasule")
import winsound
import requests, sys
import time
from datetime import date
import json
import src.multiprocessing

from twilio.rest import Client

account_sid = 'AC1fa943a39d4fb52fa1a26e1e5cc66767'
auth_token = '8135a3424f4b10385067323f301ee167'
client = Client(account_sid, auth_token)
avail_details = []
inputs = ['400080','400081','400082','400601','400603','400708','411039','411015','411039','411003','411026','412105','455001','400056','400004']
# avail_details = ""
# for whatsapp
def sendWhatsapp(msg):
    message = client.messages.create(
        body='Alert : '"\n"+msg,
        from_='whatsapp:+14155238886',
        to='whatsapp:+919004927347'
    )
    message = client.messages.create(
        body='Alert : '+msg,
        from_='whatsapp:+14155238886',
        to='whatsapp:+918962129334'
    )


def alert():
	frequency = 4500
	duration = 5000
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
                print ("Pin code: "+pinCode + ","+ str(ele['district_name'])+","+str(ele['state_name'])+"\n")
                print ("fee_type: Free" + "\n")
                print ("Hospital Name: " + str(ele['name']) + "\n")
                print ("Hospital Address: " + str(hospitalAddress) + "\n")
                print ("Charge: " + '0'+ "\n")
                print ("Vaccine Name: " + str(ele['sessions'][0]['vaccine']) + "\n")
				
                for counter in ele['sessions']:
                    # avail_details = avail_details+"Hospital Name: " + str(ele['name']) + " Available Vaccine count: " + str(counter['available_capacity']) +"\n"
                    # print("Whatapps"+avail_details)
                    print ("Available Vaccine count: " + str(counter['available_capacity']))
                    if int(counter['available_capacity']) > 0 and int(counter['min_age_limit']) == 18:
                        print ("Date: " + str(counter['date']))
                        print ("Min Age Limit: " + str(counter['min_age_limit']))
                        print ("Available Slots: ") + "\n"
                        for slot in counter['slots']:
                            print (slot)
                        alert()
                        avail_details.append("Pincode :"+pinC+ ","+ str(ele['district_name'])+","+str(ele['state_name'])+ "\n" +"Hospital Name: " + str(ele['name']) +"\n" + "Date: " + str(counter['date'])+"\n" + "Available Vaccine count "+"["+str(counter['vaccine'])+"]:" + str(counter['available_capacity']) )
                    print ("Date: " + str(counter['date']))
                    print ("Min Age Limit: " + str(counter['min_age_limit']))
                    #print ("Available Slots: ") + "\n"
                    # for slot in counter['slots']:
                    #      print (slot)
                    print ("\n\n")
            else:
                hospitalAddress = ele['address']
                print ("Pin code: "+pinCode + ","+ str(ele['district_name'])+","+str(ele['state_name'])+"\n")
                print ("fee_type: Free" + "\n")
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

                        # for slot in counter['slots']:
                        #     print (slot)
                            #slot1 = slot+slot1
                        alert()
                        avail_details.append("Pincode :"+pinC+ ","+ str(ele['district_name'])+","+str(ele['state_name'])+ "\n" +"Hospital Name: " + str(ele['name']) +"\n" + "Date: " + str(counter['date'])+"\n" + "Available Vaccine count "+"["+str(counter['vaccine'])+"]:" + str(counter['available_capacity']) )
                    print ("Date: " + str(counter['date']))
                    print ("Min Age Limit: " + str(counter['min_age_limit']))
                    print ("Available Slots: " + "\n")
                    for slot in counter['slots']:
                        print (slot)


                    print ("\n\n")
                   # choice = input("Press Y to search for any other Pincode\n")
                   # while(choice.casefold()=='y'):
                    #    pinCode = input("Enter Pin code you wish to search\n")
                     #   checkVaccineAvailability(pinCode)
					
                #sys.exit(0)
    else:
        print ("Please enter a valid PINCODE\n")
        sys.exit(0)

    #print("Whatsapp"+avail_details)
    #
    if len(avail_details) > 0:
    #     for x in range(len(avail_details)):
    #         #print (avail_details[x])
            #aval_slot =avail_details[x]
        aval_slot = '\n'.join(avail_details)
        sendWhatsapp(aval_slot)
        inputs.remove(pinC)
        sys.exit(0)

    time.sleep(10)
if __name__ == '__main__':
    while True:
        pool = src.multiprocessing.Pool()
        pool = src.multiprocessing.Pool(processes=15)
        outputs = pool.map(checkVaccineAvailability, inputs)
        print("Input: {}".format(inputs))
        print("Output: {}".format(outputs))
        # outputs_async = pool.map_async(checkVaccineAvailability, inputs)
        # outputs = outputs_async.get()
        # print("Output: {}".format(outputs))
