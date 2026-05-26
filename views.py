import os
from datetime import datetime, timedelta
import requests
from flask import Blueprint, render_template

ticket_blueprint = Blueprint('ticket_views', __name__, template_folder='templates')

def get_total_weekly_commits():
    token = os.environ.get("GITHUB_TOKEN")
    # Grab the raw string "repo1,repo2,..."
    repos_raw = os.environ.get("GITHUB_REPOS")
    
    if not token or not repos_raw:
        return 0

    # Convert the comma-separated string into a clean Python list
    repo_list = [repo.strip() for repo in repos_raw.split(",")]
    
    # Calculate the date exactly 7 days ago
    since_date = (datetime.utcnow() - timedelta(days=7)).isoformat() + "Z"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    params = {
        "since": since_date
    }

    total_commits = 0

    # Loop through all 6 repositories
    for repo in repo_list:
        url = f"https://api.github.com/repos/{repo}/commits"
        try:
            response = requests.get(url, headers=headers, params=params, timeout=5)
            if response.status_code == 200:
                commits = response.json()
                total_commits += len(commits) # Add this repo's commits to our grand total
            else:
                print(f"GitHub API Error for {repo}: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Connection failed for {repo}: {e}")
            
    return total_commits

@ticket_blueprint.route("/")
def home():
    nav = [
        {"label": "Thoth AI", "route": "ticket_views.thothAI"},
        {"label": "Notebook", "route": "ticket_views.notebook"},
        {"label": "Persona", "route": "ticket_views.persona"}
    ]
    
    # This now scans all 6 repositories seamlessly!
    total_commits = get_total_weekly_commits()

    dashboard_stats = {
        "pages_read": 50,
        "push_ups": 20,
        "top_recipes": ["Alfajor", "Chicken breast with rice"],
        "total_repos": 6,
        "weekly_commits": total_commits 
    }

    return render_template(
        "homepage.html",
        cssPath="../static/homepage/homepage.css",
        pageTitle="Stermax Ticket AI",
        userName="Triple T",
        nav=nav,
        stats=dashboard_stats 
    )

@ticket_blueprint.route("/thothAI")
def thothAI():
    return render_template("Ai/thothAI.html")

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
        "notebook/notebook.html",
        cssPath="../static/notebook/notebook.css"
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