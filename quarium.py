import os
import datetime
import sys
import cPickle
import json
import zmq
import time
from flask import Flask
from flask import g
from flask import render_template
from flask import abort
from flask import request
from flask import url_for
from flask import redirect
from flask import session

from contextlib import closing


app = Flask(__name__)

def set_subscriber():
    # Setup tweet subscriber
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5556")
    socket.setsockopt_string(zmq.SUBSCRIBE, u"")
    print "established socket"
    return socket


@app.route('/', methods=['GET'])
def quarium_style():
    return render_template('base.html', style='quarium')


@app.route('/Space', methods=['GET'])
def space_style():
    return render_template('base.html', style='space')



@app.route('/changefilter', methods=['POST'])
def change_filter():
    a = socket.close(0)
    print "closed socket"
    # try:
    # except UnboundLocalError:
    #     pass
    global socket
    socket = set_subscriber()
    # time.sleep(5)
    # print socket
    # socket.connect("tcp://localhost:5551")
    print "got to routing"
    thefilter = request.form['thefilter']
    print "sending filter: " + str(thefilter)
    socket1.send_string(u"%s" % (unicode(thefilter)))
    print "sent filter"
    # print entries # debugging
    return render_template('base.html', style='quarium')



@app.route('/gettweet', methods=['GET'])
def contact():
    string = socket.recv_string()
    try:
        pass
    except zmq.error.ZMQError:
        pass
        # socket = context.socket(zmq.SUB)
        # socket.connect("tcp://localhost:5556")
        # socket.setsockopt_string(zmq.SUBSCRIBE, u"10")
    tweet_list = string.split()
    json_pack = {}
    json_pack['tweet'] = []
    for word in tweet_list:
        if 'http' in word:
            json_pack['thelink'] = word
        else:
            json_pack['tweet'].append(word)
    json_pack['tweet'] = " ".join(json_pack['tweet'])
    print json_pack['tweet']
    encoded = json.JSONEncoder().encode(json_pack)

    return encoded



if __name__ == '__main__':
    context = zmq.Context()
    global socket
    socket = set_subscriber()

    # Setup filter publisher
    context1 = zmq.Context()
    socket1 = context1.socket(zmq.PUB)
    socket1.bind("tcp://*:5559")
    # try:
    # except zmq.error.ZMQError:
    #     print "Already connected..."
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8000, app)
    srv.serve_forever()
    # app.run()