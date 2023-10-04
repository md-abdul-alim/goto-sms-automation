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

        response = res.read().decode("utf-8")
        json_response = json.loads(response)

        if 'errorCode' in response and json_response['errorCode'] == 'AUTHN_EXPIRED_TOKEN':
            print(json_response['message'])
            return 0
        return 1


    except Exception as e:
        return 0
        print(f"Error sending SMS: {str(e)}")

def main():
    # Load the Excel file
    workbook = openpyxl.load_workbook('file.xlsx')
    sheet = workbook.active
    count, success, fail = 0, 0, 0

    # Iterate through rows and send SMS
    for row in sheet.iter_rows(min_row=2, values_only=True):
        phone_number, message = row

        if 'None' not in str(phone_number):
            count +=1
            status = send_sms(phone_number, message)

            if status == 1:
                success +=1
            else:
                fail +=1

    print(f"Total Message sent: {count}, successful: {success}, failed: {fail}")

if __name__ == "__main__":
    main()
