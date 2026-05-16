from flask import Blueprint, render_template, request

# 1. Define the blueprint. 
# 'ticket_views' is the internal name, and we point it to our templates folder.
ticket_blueprint = Blueprint('ticket_views', __name__, template_folder='templates')

@ticket_blueprint.route("/")
def home():
    return render_template(
        "homepage.html.jinja",
        cssPath="styles/main.css",
        pageTitle="Stermax Ticket AI",
        userName="Triple T"
    )

@ticket_blueprint.route("/login")
def login():
    return render_template(
        "login.html",
        cssPath="styles/login/styles.css",
        siteName="Life on Internet"
    )