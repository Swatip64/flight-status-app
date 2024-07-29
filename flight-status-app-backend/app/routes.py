from flask_restful import Resource, reqparse
from app import db
from app.models import Flight
from app.firebase_service import send_push_notification
from app.notification_service import publish_notification

class FlightListResource(Resource):
    def get(self):
        flights = Flight.query.all()
        return [{'id': flight.id, 'flight_number': flight.flight_number, 'status': flight.status, 'gate': flight.gate, 'arrival_time': flight.arrival_time, 'boarding_time': flight.boarding_time} for flight in flights], 200

class FlightResource(Resource):
    def get(self, flight_id):
        flight = Flight.query.get_or_404(flight_id)
        return {'id': flight.id, 'flight_number': flight.flight_number, 'status': flight.status, 'gate': flight.gate, 'arrival_time': flight.arrival_time, 'boarding_time': flight.boarding_time}, 200

    def put(self, flight_id):
        flight = Flight.query.get_or_404(flight_id)
        parser = reqparse.RequestParser()
        parser.add_argument('status', type=str, required=True, help='Status is required')
        parser.add_argument('gate', type=str)
        parser.add_argument('arrival_time', type=str)
        parser.add_argument('boarding_time', type=str)
        args = parser.parse_args()

        flight.status = args['status']
        flight.gate = args['gate']
        flight.arrival_time = args['arrival_time']
        flight.boarding_time = args['boarding_time']
        db.session.commit()

        # Notify users about the flight update
        notification_title = f"Flight {flight.flight_number} Update"
        notification_body = f"Your flight {flight.flight_number} has a status update: {flight.status}."

        # Example token - Replace with actual user tokens
        user_device_token = "USER_DEVICE_TOKEN_HERE"
        send_push_notification(user_device_token, notification_title, notification_body)

        # Publish notification to RabbitMQ
        publish_notification(notification_body, 'email')  # Or 'SMS' based on logic

        return {'message': 'Flight updated successfully'}, 200

class NotificationResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('flight_id', type=int, required=True, help='Flight ID is required')
        parser.add_argument('message', type=str, required=True, help='Message is required')
        parser.add_argument('token', type=str, required=True, help='Device token is required')
        args = parser.parse_args()

        flight = Flight.query.get_or_404(args['flight_id'])

        # Send the push notification
        notification_title = f"Flight {flight.flight_number} Notification"
        notification_body = args['message']
        user_device_token = args['token']
        
        # Call the FCM function
        send_push_notification(user_device_token, notification_title, notification_body)

        # Publish notification to RabbitMQ
        publish_notification(notification_body, 'email')  # Or 'SMS'

        return {'message': 'Notification sent'}, 201

def initialize_routes(api):
    api.add_resource(FlightListResource, '/api/flights')
    api.add_resource(FlightResource, '/api/flights/<int:flight_id>')
    api.add_resource(NotificationResource, '/api/notifications')
