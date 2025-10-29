import os
import firebase_admin
from firebase_admin import credentials, auth, storage
import json

# Load Firebase credentials from environment variable
firebase_credentials = os.getenv("FIREBASE_CREDENTIALS")

if firebase_credentials:
    cred = credentials.Certificate(json.loads(firebase_credentials))
    firebase_admin.initialize_app(cred)
else:
    raise Exception("FIREBASE_CREDENTIALS not found in environment variables")

bucket = storage.bucket('nutricheck-app.appspot.com')


def upload_image_to_firebase(filename, file_path):
    blob = bucket.blob('images/'+filename)
    blob.upload_from_filename(filename=file_path)


def verifyGoogleAccessToken(token):
    return auth.verify_id_token(token)
