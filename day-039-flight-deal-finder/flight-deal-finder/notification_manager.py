from twilio.rest import Client
import os

account_sid = "AC4f183a5a3527be369675e890c6f08666"
auth_token = os.environ['AUTH_KEY']


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def sms_best_offer(self, best_offer):
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f"Low price alert! Only £{best_offer['flightPrice']} from {best_offer['departureCity']}-{best_offer['flyFrom']} to {best_offer['destinationCity']}-{best_offer['flyTo']}, from {best_offer['dateFrom']} to {best_offer['dateTo']}.",
            from_='+13344686603',
            to='+' + os.environ['MY_CONTACT'],
        )

        print(message.status)
