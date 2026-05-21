from flask import Blueprint, render_template, request

# 1. Define the blueprint. 
# 'ticket_views' is the internal name, and we point it to our templates folder.
ticket_blueprint = Blueprint('ticket_views', __name__, template_folder='templates')

@ticket_blueprint.route("/ThothAI")
def ThothAI():
    return render_template(
        "Ai/thothAI.html"
    )

@ticket_blueprint.route("/")
def home():
    nav = [
        {"label": "Thoth AI", "route": "ticket_views.ThothAI"},
        {"label": "Notebook", "route": "ticket_views.notebook"}
        ]


    return render_template(
        "homepage.html",
        cssPath="../static/homepage/homepage.css",
        pageTitle="Stermax Ticket AI",
        userName="Triple T",
        nav = nav   
        
    )

@ticket_blueprint.route("/login")
def login():
    return render_template(
        "login.html",
        cssPath="styles/login/styles.css",
        siteName="Life on Internet"
    )

@ticket_blueprint.route("/notebook")
def notebook():
    return render_template(
        "notebook/notebook.html"
    )