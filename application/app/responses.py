from fastapi import HTTPException, status


class ResponseException:
    HTTP_400_BAD_REQUEST = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="bad request")
    HTTP_404_NOT_FOUND = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    HTTP_500_INTERNAL_SERVER_ERROR = HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="internal server error")
