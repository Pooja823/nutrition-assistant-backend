import os
import json
import firebase_admin
from firebase_admin import credentials, auth, storage

# Get Firebase credentials from environment variable
firebase_credentials = os.getenv("FIREBASE_CREDENTIALS")

if firebase_credentials:
    cred = credentials.Certificate(json.loads(firebase_credentials))
else:
    raise ValueError("Missing FIREBASE_CREDENTIALS environment variable")

firebase_admin.initialize_app(cred, {
    'storageBucket': 'nutricheck-app.appspot.com'
})

bucket = storage.bucket()

def upload_image_to_firebase(filename, file_path):
    blob = bucket.blob('images/' + filename)
    blob.upload_from_filename(filename=file_path)

def verifyGoogleAccessToken(token):
    return auth.verify_id_token(token)
