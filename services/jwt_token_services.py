import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from routers.auth import SECRET_KEY

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

def verify_jwt_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        sub = payload.get("sub")
        if sub is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return sub
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")