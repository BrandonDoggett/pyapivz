#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/graphin')
def graphin():
    with open('/home/student/sshpass.yml') as sshpass:
        creds = yaml.load(sshpass)
    srvuptime = []
    xtick = []
    for cred in creds:

