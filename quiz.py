from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import os
from config import DATABASE_URI
from random_names import get_random_team_name
from datetime import datetime
import pytz

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(app)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(80), nullable=False)    
    e_mail = db.Column(db.String(255), nullable=False)
    participant_1 = db.Column(db.String(80))
    participant_2 = db.Column(db.String(80))
    participant_3 = db.Column(db.String(80))
    participant_4 = db.Column(db.String(80))
    participant_5 = db.Column(db.String(80))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    if Team.query.count() >= 12:
        return "Error: Maximum limit of teams reached. Sign-up is closed."

    team_name = request.form['team_name']
    e_mail = request.form['e_mail']
    participants = [request.form[f'name_{i}'] for i in range(1, 6) if request.form[f'name_{i}'].strip() != ""]

    if not team_name.strip():
        return "Error: Team name is required."
    
    if not e_mail.strip():
        return "Error: E-mail is required."
    
    # Check if the team name already exists in the database (case and whitespace-insensitive)
    existing_team = Team.query.filter(func.lower(func.replace(Team.team_name, ' ', '')) == func.lower(func.replace(team_name, ' ', ''))).first()
    if existing_team:
        return f"Error: Team name '{team_name}' is already taken. Please choose a different team name."

    if len(participants) > 0:
        # Convert to local timezone using pytz
        timestamp_utc = datetime.utcnow()
        local_tz = pytz.timezone('Europe/Copenhagen')
        timestamp_local = timestamp_utc.replace(tzinfo=pytz.utc).astimezone(local_tz)

        new_team = Team(
            team_name=team_name,
            e_mail=e_mail,
            participant_1=participants[0] if len(participants) >= 1 else None,
            participant_2=participants[1] if len(participants) >= 2 else None,
            participant_3=participants[2] if len(participants) >= 3 else None,
            participant_4=participants[3] if len(participants) >= 4 else None,
            participant_5=participants[4] if len(participants) >= 5 else None,
            timestamp=timestamp_local
        )
        db.session.add(new_team)
        db.session.commit()
        return "Successfully signed up!"
    else:
        return "Error: Invalid team size. You must at least have one member on your team."

@app.route('/random_team_name')
def random_team_name():
    random_name = get_random_team_name()
    return jsonify({'random_team_name': random_name})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, use_reloader=False)

