import openpyxl
import requests
import json
import http.client

# API endpoint for sending SMS
SMS_API_ENDPOINT = http.client.HTTPSConnection("api.goto.com")

# Your fixed phone number
OWNER_PHONE_NUMBER = "+18722770714"


payload = "{\"ownerPhoneNumber\":\"+18722770714\",\"contactPhoneNumbers\":[\"+12623\"],\"body\":\"Testing live messages 5!\"}"

# Parse the JSON payload
data = json.loads(payload)


headers = { 
	'content-type': "application/json",
	'Authorization': 'Bearer eyJraWQiOiI2MjAiLCJhbGciOiJSUzUxMiJ9.eyJzYyI6ImNhbGwtY29udHJvbC52MS5jYWxscy5jb250cm9sIGNhbGxzLnYyLmluaXRpYXRlIG1lc3NhZ2luZy52MS53cml0ZSBpZGVudGl0eTpzY2ltLm1lIGNhbGwtZXZlbnRzLnYxLmV2ZW50cy5yZWFkIG1lc3NhZ2luZy52MS5ub3RpZmljYXRpb25zLm1hbmFnZSB2b2ljZW1haWwudjEubm90aWZpY2F0aW9ucy5tYW5hZ2UgcmVjb3JkaW5nLnYxLm5vdGlmaWNhdGlvbnMubWFuYWdlIHN1cHBvcnQ6IHZvaWNlbWFpbC52MS52b2ljZW1haWxzLndyaXRlIGZheC52MS53cml0ZSB2b2ljZS1hZG1pbi52MS53cml0ZSBpZGVudGl0eTogd2VicnRjLnYxLnJlYWQgd2VicnRjLnYxLndyaXRlIGNvbGxhYjogdm9pY2UtYWRtaW4udjEucmVhZCBwcmVzZW5jZS52MS5yZWFkIHJlY29yZGluZy52MS5yZWFkIGNhbGwtZXZlbnRzLnYxLm5vdGlmaWNhdGlvbnMubWFuYWdlIGlkZW50aXR5OnNjaW0ub3JnIHByZXNlbmNlLnYxLndyaXRlIGZheC52MS5yZWFkIGNhbGwtaGlzdG9yeS52MS5ub3RpZmljYXRpb25zLm1hbmFnZSBwcmVzZW5jZS52MS5ub3RpZmljYXRpb25zLm1hbmFnZSBtZXNzYWdpbmcudjEuc2VuZCBtZXNzYWdpbmcudjEucmVhZCBjci52MS5yZWFkIGZheC52MS5ub3RpZmljYXRpb25zLm1hbmFnZSB1c2Vycy52MS5saW5lcy5yZWFkIHZvaWNlbWFpbC52MS52b2ljZW1haWxzLnJlYWQiLCJzdWIiOiIxMDM2MDQ2MDUxNDIyMjM4Mjc0IiwiYXVkIjoiNWM0ZGJlMTEtMDY1OS00MmIwLWE5NGItNzZkYTkzODQzMzIyIiwib2duIjoicHdkIiwibHMiOiIxN2VkYjRmOS0yNjc1LTQ0ZmUtOThhNS0zNmRkMzI5NTQ2NDIiLCJ0eXAiOiJhIiwiZXhwIjoxNjk2MjY3ODM2LCJpYXQiOjE2OTYyNjQyMzYsImp0aSI6Ijg2MDdhMjJmLWM2MWUtNDk2NC04ZWUyLTRkMTMzMzEwZDNlYiJ9.GyOQsDkmEgJfrUugn1RfeKcmWp144iL9CJIx2B1Z6FMm530sNv9Xc06rOKRmKry3_zS9AMN8vL9mddBf64MEkg8QRmdR-Syn1qGRFLk2u3OGWpW89q1P4ffP1k6HMbkNc4SbaW_6ejTZyNRCwjWMxJdPHdISNAr2aaKWfZQQ2bcQUqKjnowJphxiyxfnktBfKO7qXVcgl6AasIe9vSDDdwqoq9paSzieqw-tUL469ZL44MC3cWss09bduS4lhTUNBukbVEmNIr67Ing0QgaiSvDwaCzMNUgkxY4rMXESxvi7E5aWjHdMdDtaHat5uz0olFunydCnfMUine9dO7kPzA'

}


def send_sms(phone_number, message):

    try:
        # Send the SMS using the API
        data["ownerPhoneNumber"] = OWNER_PHONE_NUMBER
        data["contactPhoneNumbers"] = [phone_number, ]
        data["body"] = message

        updated_payload = json.dumps(data)

        SMS_API_ENDPOINT.request("POST", "/messaging/v1/messages", updated_payload, headers)

        res = SMS_API_ENDPOINT.getresponse()

        read_response = res.read()
        print(read_response.decode("utf-8"))

    except Exception as e:
        print(f"Error sending SMS: {str(e)}")

def main():
    # Load the Excel file
    workbook = openpyxl.load_workbook('file.xlsx')
    sheet = workbook.active

    # Iterate through rows and send SMS
    for row in sheet.iter_rows(min_row=2, values_only=True):
        phone_number, message = row
        print(phone_number, message)
        send_sms(phone_number, message)

if __name__ == "__main__":
    main()
