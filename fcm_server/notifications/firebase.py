import firebase_admin
from firebase_admin import credentials, messaging

# Path to your service account key JSON file
cred = credentials.Certificate(r"C:\Users\navdeep singh\fcm_server\notifications\alumify-507f9-firebase-adminsdk-hz9pp-6246138526.json")

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred)

def send_push_notification(token, title, body):
    # Define the message payload
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        token=token,
    )

    # Send the message
    response = messaging.send(message)
    return response
