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
    
    def move(self, direction):
        if direction == 'up' and self.y > 0:
            self.y -= 1
        elif direction == 'right' and self.x < SIZE - 1:
            self.x += 1
        elif direction == 'down' and self.y < SIZE - 1:
            self.y += 1
        elif direction == 'left' and self.x > 0:
            self.x -= 1
        else:
            return False
        return True


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

@app.route('/move')
def move():
    username = request.args.get('username')
    direction = request.args.get('direction')
    if username in users:
        if users[username].move(direction):
            return 'ok'
    return 'fail'

app.run(debug=True)