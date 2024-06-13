from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SSOREADY_API_KEY = os.getenv("API_KEY")
    SECRET_KEY = os.getenv("SECRET")

class ErrorMessages:
    VALUE_ERROR_ADD_USER = "add_user() requires a valid User object."

class Messages:
    STATUS_MESSAGE_SUCCESS_HOME = "You have successfully logged in as the following user: "
    STATUS_MESSAGE_FAILURE_HOME = "You're not currently logged in"
    STATUS_MESSAGE_AUTH = "To login, follow the redirect URL -- it will take you to your identity provider"
    STATUS_MESSAGE_CALLBACK = "You've landed back at the 'Callback' endpoint -- return to the 'Home' tab to see whether you had a successful login."
    STATUS_MESSAGE_LOGOUT = "Are you sure you want to logout?"

    NEXT_STEP_SUCCESS_HOME = "Log out >>"
    NEXT_STEP_FAILURE_HOME = "Sign in >>"
    NEXT_STEP_AUTH = "Proceed to IDP for sign-in >>"
    NEXT_STEP_CALLBACK = "See your login status >>"
    NEXT_STEP_LOGOUT = "Yes, I'm sure"

    NEXT_PATH_SUCCESS_HOME = ""
    NEXT_PATH_FAILURE_HOME = ""
    NEXT_PATH_AUTH = ""
    NEXT_PATH_CALLBACK = ""
    NEXT_PATH_LOGOUT = ""

class FictionalUsers:
    USER1 = "ronald@mcdonald.net"

class ShorthandStyles:
    TAB_SELECTED = "bg-gray1 rounded-t-md"

