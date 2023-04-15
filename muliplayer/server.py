from flask import Flask, request, json, jsonify
import random, json


app = Flask('game')

class User:
    def __init__(self, name):
        self.name = name
        self.x = random.randrange(0, SIZE)
        self.y = random.randrange(0, SIZE)
        self.color = random.randrange(0, 7)
        self.score = 0
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)

SIZE = 20

users = {}


@app.route('/')
def hello():
    return 'hello world'

@app.route('/register')
def register():
    username = request.args.get('name')
    user = User(username)
    users[username] = user
    print(username)
    return user.toJSON()

@app.route('/status')
def status():
    ans = {}
    for user in users:
        ans[user] = users[user].toJSON()
    return ans

app.run(debug=True)