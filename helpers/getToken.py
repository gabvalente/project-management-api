import jwt
from flask import request
import app_config as config

def getToken():
    token = None

    try:
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return 400
        try:
            userInformation = jwt.decode(token, key = config.TOKEN_SECRET, algorithms=["HS256"])
        except Exception:
            return 401

        return token
        
    except jwt.ExpiredSignatureError:
        return 401
    except:
        return 400