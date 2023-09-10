from twilio.rest import Client
import os

# Important twilio AUTH_KEY stored as environment variable
account_sid = "AC4f183a5a3527be369675e890c6f08666"
auth_token = os.environ['AUTH_KEY']


class NotificationManager:
    def sms_best_offer(self, best_offer):
        """Sends an SMS with the best offer available."""
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"Low price alert! Only £{best_offer['flightPrice']} from {best_offer['departureCity']}-{best_offer['flyFrom']} to {best_offer['destinationCity']}-{best_offer['flyTo']}, from {best_offer['dateFrom']} to {best_offer['dateTo']}.",
            from_='+13344686603',
            to='+' + os.environ['MY_CONTACT'],
        )

        print(message.status)
