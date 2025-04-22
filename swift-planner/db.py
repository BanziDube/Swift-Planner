import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
import bcrypt
import os

# Load environment variables (e.g., if you want to use any secret configs)
load_dotenv()

# Initialize Firebase app with the service account key
cred = credentials.Certificate(
    "./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()


def hash_password(password):
    """Hashes the provided password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')  # Decode for storage as string


def insert_user_data(name, email, password):
    """Inserts a new user into the Firestore 'users' collection with a hashed password."""
    hashed_pw = hash_password(password)
    user_ref = db.collection("users").document()  # Auto-generate a document ID
    user_ref.set({
        "name": name,
        "email": email,
        "password": hashed_pw
    })

    print(f"User data inserted into Firestore with ID: {user_ref.id}")
