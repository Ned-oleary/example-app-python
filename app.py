from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user
from ssoready.client import SSOReady
from config import Config, Messages, FictionalUsers, ErrorMessages, ShorthandStyles


app = Flask(__name__, static_folder='src/styles', static_url_path='/styles')
app.config.from_object(Config)

login_manager = LoginManager()
login_manager.init_app(app)


#UserMixin just includes some pre-built functionality that works with flask-login
#You can implement a flask-login- compatible User class from scratch without too much effort
class User(UserMixin):
    def __init__(self, user_id, is_active=True):
        self.id = user_id
        self.active = is_active
        self.organization_external_id = None
        self._is_authenticated = False

    @property
    def is_authenticated(self):
        return self._is_authenticated

    def set_authentication(self, input = True):
        self._is_authenticated = input

YOUR_USERS = {
    0: User(user_id=FictionalUsers.USER1)
}

def exists_user(user_id):
    known_emails = [users.id for users in YOUR_USERS.values()]
    return (user_id in known_emails)
    
def add_user(user):
    if not isinstance(user, User) or not user:
        raise ValueError(ErrorMessages.VALUE_ERROR_ADD_USER)
    if not exists_user(user.id):
        next_key = max(YOUR_USERS.keys()) + 1
        YOUR_USERS[next_key] = user

#flask-login requires a method that looks like this
@login_manager.user_loader
def load_user(id):
    for user in YOUR_USERS.values():
        if user.id == id:
            return user
    return None

#login
@app.route("/")
def home():
    if current_user.is_authenticated:
        status = Messages.STATUS_MESSAGE_SUCCESS_HOME + current_user.id
        nextStep = Messages.NEXT_STEP_SUCCESS_HOME
        nextPath = url_for("process_logout")
    else:
        status = Messages.STATUS_MESSAGE_FAILURE_HOME
        nextStep = Messages.NEXT_STEP_FAILURE_HOME
        nextPath = url_for("auth_preview")
    return(render_template("index.html", status = status, nextStep=nextStep, nextPath = nextPath, tab_1_bg = ShorthandStyles.TAB_SELECTED))

@app.route("/initiate_auth")
def auth_preview():

    status = Messages.STATUS_MESSAGE_AUTH
    nextStep = Messages.NEXT_STEP_AUTH

    client = SSOReady(api_key = Config.SSOREADY_API_KEY)
    nextPath = (client.saml.get_saml_redirect_url(organization_external_id="organization_alpha",)).redirect_url

    return(render_template("index.html", status = status, nextStep=nextStep, nextPath = nextPath, tab_2_bg = ShorthandStyles.TAB_SELECTED))

@app.route("/ssoready/callback")
def process_callback():

    try:
        saml_access_code = request.args["saml_access_code"]
        client = SSOReady(api_key = Config.SSOREADY_API_KEY)
        ssoready_output = client.saml.redeem_saml_access_code(saml_access_code=saml_access_code,)

        assert ssoready_output.organization_external_id == "organization_alpha"

        new_user = User(user_id = ssoready_output.email)
        new_user.set_authentication()
        add_user(new_user)
        login_user(new_user)
    except:
        pass

    status = Messages.STATUS_MESSAGE_CALLBACK
    nextStep = Messages.NEXT_STEP_CALLBACK
    nextPath = url_for("home")
    return(render_template("index.html", status = status, nextStep=nextStep, nextPath = nextPath, tab_3_bg = ShorthandStyles.TAB_SELECTED))

@app.route("/process_logout")
def process_logout():
    status = Messages.STATUS_MESSAGE_LOGOUT
    nextStep = Messages.NEXT_STEP_LOGOUT
    nextPath = url_for("logout")
    return(render_template("index.html", status = status, nextStep=nextStep, nextPath = nextPath, tab_4_bg = ShorthandStyles.TAB_SELECTED))

@app.route("/logout")
def logout():
    if current_user.is_authenticated:
        logout_user()
    return(redirect(url_for("home")))

