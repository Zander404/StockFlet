import pyrebase


def initialize_firebase():
    config = {
    }

    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    db = firebase.database()

    return auth, db