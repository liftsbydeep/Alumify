from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from notifications.firebase import send_push_notification  # Correct import path

@csrf_exempt
def send_signup_notification(request):
    if request.method == 'POST':
        try:
            # Parse the JSON body
            data = json.loads(request.body)
            # Get the FCM token
            fcm_token = data.get('fcm_token')

            if not fcm_token:
                return JsonResponse({'error': 'FCM token not provided'}, status=400)

            # Define notification details
            title = 'Welcome to Alumify!'
            body = 'Thank you for signing up.Fell free to contact us for any queries'

            # Send the notification
            response = send_push_notification(fcm_token, title, body)

            return JsonResponse({'status': 'Notification sent', 'response': response})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
