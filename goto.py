import openpyxl
import requests
import json
import os
import base64
import http.client


# API endpoint for sending SMS
SMS_API_ENDPOINT = http.client.HTTPSConnection("api.goto.com")

# Your fixed phone number
OWNER_PHONE_NUMBER = "+18722770714"


headers = { 
	'content-type': "multipart/form-data",
    'Accept': 'application/json',
    'Authorization': 'Bearer eyJraWQiOiI2MjAiLCJhbGciOiJSUzUxMiJ9.eyJzYyI6ImNhbGwtY29udHJvbC52MS5jYWxscy5jb250cm9sIGNhbGxzLnYyLmluaXRpYXRlIG1lc3NhZ2luZy52MS53cml0ZSBpZGVudGl0eTpzY2ltLm1lIGNhbGwtZXZlbnRzLnYxLmV2ZW50cy5yZWFkIG1lc3NhZ2luZy52MS5ub3RpZmljYXRpb25zLm1hbmFnZSB2b2ljZW1haWwudjEubm90aWZpY2F0aW9ucy5tYW5hZ2UgcmVjb3JkaW5nLnYxLm5vdGlmaWNhdGlvbnMubWFuYWdlIHN1cHBvcnQ6IHZvaWNlbWFpbC52MS52b2ljZW1haWxzLndyaXRlIGZheC52MS53cml0ZSB2b2ljZS1hZG1pbi52MS53cml0ZSBpZGVudGl0eTogd2VicnRjLnYxLnJlYWQgd2VicnRjLnYxLndyaXRlIGNvbGxhYjogdm9pY2UtYWRtaW4udjEucmVhZCBwcmVzZW5jZS52MS5yZWFkIHJlY29yZGluZy52MS5yZWFkIGNhbGwtZXZlbnRzLnYxLm5vdGlmaWNhdGlvbnMubWFuYWdlIGlkZW50aXR5OnNjaW0ub3JnIHByZXNlbmNlLnYxLndyaXRlIGZheC52MS5yZWFkIGNhbGwtaGlzdG9yeS52MS5ub3RpZmljYXRpb25zLm1hbmFnZSBwcmVzZW5jZS52MS5ub3RpZmljYXRpb25zLm1hbmFnZSBtZXNzYWdpbmcudjEuc2VuZCBtZXNzYWdpbmcudjEucmVhZCBjci52MS5yZWFkIGZheC52MS5ub3RpZmljYXRpb25zLm1hbmFnZSB1c2Vycy52MS5saW5lcy5yZWFkIHZvaWNlbWFpbC52MS52b2ljZW1haWxzLnJlYWQiLCJzdWIiOiIxMDM2MDQ2MDUxNDIyMjM4Mjc0IiwiYXVkIjoiNWM0ZGJlMTEtMDY1OS00MmIwLWE5NGItNzZkYTkzODQzMzIyIiwib2duIjoicHdkIiwibHMiOiIxN2VkYjRmOS0yNjc1LTQ0ZmUtOThhNS0zNmRkMzI5NTQ2NDIiLCJ0eXAiOiJhIiwiZXhwIjoxNjk2MjcyNjU2LCJpYXQiOjE2OTYyNjkwNTYsImp0aSI6IjMwODlmNmI1LTI4YTktNDcxZi05OGYwLTRiNmE3YzIxMGE0MiJ9.xHEc_BD_SjlYAWpGGt1e55U9fLWONQAxkUPnvYAqE_vQOyKgGuY04cbIgBQW2NwCKAB0RbBB8kvwoK20Bp60lyLABTccYLxFEq7rkb9LbqOTg6PKBNDyPfdahS4bXjroryTu72CdRJ1ziGk-u8Rm0eJziipmlQNJKotkz3gbAlR_AAF_cDhYbfLGH-Z3gSajFZMJdoWcXObOIRhjDJqsYi2nhOneP8g2cpuN74j9Rqeqm2PBUPrwFskdPQ0MItAXCJpcSyXdi3LR65l-j0Fi_5POgfXoLA_aDUC8gIhzOx8BYeYx-dCoU235WErWugcLcGbXSrEskbiOzzLlfvPJDQ'

}


def send_sms(phone_number, message, media_path):
    payload = "{\"ownerPhoneNumber\":\"\",\"contactPhoneNumbers\":[\"\"],\"body\":\"\", \"media\":\"\"}"
    # Parse the JSON payload
    data = json.loads(payload)

    try:

        if os.path.exists(media_path):
            # Send the SMS with media using the API
            with open(media_path, 'rb') as media_file:
                print(media_file)
                media_data = base64.b64encode(media_file.read()).decode('utf-8')
                # data["media"] = [media_data, ]
                data["media"] = media_data

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
        phone_number, message, media_path = row
        print(phone_number, message, media_path)
        send_sms(phone_number, message, media_path)

if __name__ == "__main__":
    main()
