# lambda_sms
Sends a text message to a phone number from AWS Lambda

This is a sample script of how to send a text message from Lambda.

You will require: 
- Appropriate permissions to send via SMS
- An AWS active origination number to send from
- Registered destination numbers while in Sandbox mode

The execution role must contain the following to allow the message to be sent:

{
  "Effect": "Allow",
  "Action": [
    "sns:Publish",
    "sns:SetSMSAttribute"
  ],
  "Resource": "*"
}

