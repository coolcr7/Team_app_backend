from flask import Flask, request, jsonify
import MySQLdb
from flask_cors import CORS

app = Flask(__name__)
db = MySQLdb.connect(host="localhost", user="saurabh", passwd="password", db="team_management_app")
CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}})

# User routes
@app.route("/users", methods=["GET"])
def get_users():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return jsonify(users)

@app.route("/users", methods=["POST"])
def create_user():
    username = request.json.get("username")
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (username) VALUES (%s)", (username,))
    db.commit()
    return jsonify({"message": "User created successfully"})

# Team routes
@app.route("/teams", methods=["GET"])
def get_teams():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM teams")
    teams = cursor.fetchall()
    return jsonify(teams)

@app.route("/teams", methods=["POST"])
def create_team():
    teamname = request.json.get("teamname")
    cursor = db.cursor()
    cursor.execute("INSERT INTO teams (team_name) VALUES (%s)", (teamname,))
    db.commit()
    return jsonify({"message": "Team created successfully"})

# Relationship routes
@app.route("/relationships", methods=["GET"])
def get_relationships():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM relationships")
    relationships = cursor.fetchall()
    return jsonify(relationships)

@app.route("/relationships", methods=["POST"])
def create_relationship():
    userid = request.json.get("userid")
    teamid = request.json.get("teamid")
    cursor = db.cursor()
    cursor.execute("INSERT INTO relationships (user_id, team_id) VALUES (%s, %s)", (userid, teamid))
    db.commit()
    return jsonify({"message": "Relationship created successfully"})

if __name__ == "__main__":
    app.run()
  
