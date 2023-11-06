from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
from config import DATABASE_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(app)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(80), nullable=False)
    participant_1 = db.Column(db.String(80))
    participant_2 = db.Column(db.String(80))
    participant_3 = db.Column(db.String(80))
    participant_4 = db.Column(db.String(80))
    participant_5 = db.Column(db.String(80))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    team_name = request.form['team_name']
    participants = [request.form[f'name_{i}'] for i in range(1, 6) if request.form[f'name_{i}'].strip() != ""]

    if not team_name.strip():
        return "Error: Team name is required."
    
    if len(participants) > 0:
        new_team = Team(
            team_name=team_name,
            participant_1=participants[0] if len(participants) >= 1 else None,
            participant_2=participants[1] if len(participants) >= 2 else None,
            participant_3=participants[2] if len(participants) >= 3 else None,
            participant_4=participants[3] if len(participants) >= 4 else None,
            participant_5=participants[4] if len(participants) >= 5 else None
        )
        db.session.add(new_team)
        db.session.commit()
        return "Successfully signed up!"
    else:
        return "Error: Invalid team size."

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, use_reloader=False)

