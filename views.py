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
        {"label": "Notebook", "route": "ticket_views.notebook"},
        {"label": "Persona", "route": "ticket_views.persona"},
        {"label": "Studies", "route": "ticket_views.studies"}
        ]
    
    # 2. Centralized Metric Data (Mocking data.json for now)
    dashboard_stats = {
        "pages_read": 50,
        "push_ups": 20,
        "top_recipes": ["Alfajor", "Chicken breast with rice"],
        "project_name": "Thoth Center",
        "weekly_commits": 2
    }


    return render_template(
        "homepage.html",
        cssPath="../static/homepage/homepage.css",
        pageTitle="Stermax Ticket AI",
        userName="Triple T",
        nav = nav,
        stats=dashboard_stats 
        
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

@ticket_blueprint.route("/persona")
def persona():
    return render_template(
        "persona/persona.html"
    )

@ticket_blueprint.route("/studies")
def studies():
    return render_template(
        "studies/studies.html"
    )