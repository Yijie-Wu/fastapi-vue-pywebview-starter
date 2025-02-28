from fastapi import HTTPException, status


class ResponseException:
    HTTP_400_BAD_REQUEST = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="bad request")
    HTTP_401_UNAUTHORIZED = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid token", headers={"WWW-Authenticate": "Bearer"})
    HTTP_403_FORBIDDEN = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="permission denied", headers={"WWW-Authenticate": "Bearer"})
    HTTP_404_NOT_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    HTTP_409_CONFLICT = HTTPException(status_code=status.HTTP_409_CONFLICT, detail="conflict")
    HTTP_500_INTERNAL_SERVER_ERROR = HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="internal server error")
