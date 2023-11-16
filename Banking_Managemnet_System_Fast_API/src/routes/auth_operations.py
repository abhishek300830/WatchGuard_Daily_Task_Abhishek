import os
from typing import Optional
from datetime import timedelta, datetime

from dotenv import load_dotenv

from jose import jwt

from fastapi import APIRouter, Body, HTTPException, Request, Response, status

from src.helpers.custom_response import error_response, valid_response
from src.helpers.rbac_decorator import role_based_access
from src.helpers.extract_jwt import extract_jwt_token
from src.helpers.validation_decorator import validate

from src.controllers.authentication_operations import AuthenticationOperations

from src.schemas.login_schema import login_schema
from src.schemas.change_password_schema import change_password_schema

from src.helpers.logger_config import CustomLogger


router = APIRouter(prefix="", tags=["auth_operations"])

load_dotenv()


@router.post("/login")
@validate(login_schema)
def login(response: Response, body_data=Body()):
    """login using username and password

    Args:
        response (Response): setting cookies
        body_data : data containing username and password


    Returns:
        dict: login successfully response
    """
    auth = AuthenticationOperations(body_data["username"], body_data["password"])
    user_details = auth.login()
    logger.debug("user details retrived")

    if user_details is not None:
        user_id = user_details[0]
        username = user_details[1]
        role = user_details[3]

        access_token = __create_access_token(user_id, username, role)
        logger.debug("access token created successfully")

        response.set_cookie(key="access_token", value=access_token, httponly=True)
        logger.info(" login successful")

        return valid_response(200, "Login Successfully")

    raise HTTPException(
        status.HTTP_401_UNAUTHORIZED, error_response(401, "Invalid Credentials")
    )


def __create_access_token(
    user_id, username, role, expires_delta: Optional[timedelta] = timedelta(minutes=20)
):
    """create a new access token

    Args:
        user_id (int):  ID of the user
        username (string):  username of the user
        role (string):  role of the user
        expires_delta (Optional[timedelta], optional): expire time of token in minutes. Defaults to 20 Min.

    Returns:
        string: jwt access token
    """
    encode = {
        "sub": username,
        "user_id": user_id,
        "role": role,
    }
    expire = datetime.utcnow() + expires_delta

    encode.update({"exp": expire})
    return jwt.encode(encode, os.getenv("SECRET_KEY"), os.getenv("ALGORITHM"))


@router.put("/changepassword")
@validate(change_password_schema)
@role_based_access(["Customer", "Cashier", "Manager"])
def change_password(request: Request, body_data=Body()):
    """change_password

    Args:
        request (Request): Fast API request object
        body_data (dict): username and password

    Returns:
        dict: Json Response object
    """
    user_details = extract_jwt_token(request)
    logger.debug("user details extracted successfully")

    user_id = user_details["user_id"]
    old_password = body_data["old_password"]
    new_password = body_data["new_password"]

    if old_password == new_password:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            error_response(400, "Make Sure old and new password are different."),
        )

    instance = AuthenticationOperations()
    response = instance.change_password(user_id, old_password, new_password)

    if response is str:
        logger.debug(f"password not changed details: {response}")
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            error_response(401, response),
        )

    logger.info("password changed successfully")

    return response
