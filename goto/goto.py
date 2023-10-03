import openpyxl
import requests
import json
import http.client
import constant_string

# API endpoint for sending SMS
SMS_API_ENDPOINT = http.client.HTTPSConnection("api.goto.com")

headers = { 
	'content-type': "application/json",
    'Authorization': f'Bearer {constant_string.TOKEN}'
}

def send_sms(phone_number, message):
    payload = "{\"ownerPhoneNumber\":\"\",\"contactPhoneNumbers\":[\"\"],\"body\":\"\"}"
    data = json.loads(payload)

    try:
        # Send the SMS using the API
        data["ownerPhoneNumber"] = constant_string.OWNER_PHONE_NUMBER
        data["contactPhoneNumbers"] = [phone_number, ]
        data["body"] = message

        updated_payload = json.dumps(data)

        SMS_API_ENDPOINT.request("POST", "/messaging/v1/messages", updated_payload, headers)

        res = SMS_API_ENDPOINT.getresponse()

        read_response = res.read()


    except Exception as e:
        print(f"Error sending SMS: {str(e)}")

def main():
    # Load the Excel file
    workbook = openpyxl.load_workbook('file.xlsx')
    sheet = workbook.active
    count = 0

    # Iterate through rows and send SMS
    for row in sheet.iter_rows(min_row=2, values_only=True):
        phone_number, message = row
        send_sms(phone_number, message)
        count +=1
        print("Sending Message - ", count)
    print("Total Message sent: ", count)

if __name__ == "__main__":
    main()
