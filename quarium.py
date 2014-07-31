import os
import datetime
import sys
import cPickle
import json

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


def numGen():
    i = 0
    while i < 10:
        i += 1;
        yield "The number " + str(i)


@app.route('/')
def show_entries():

    # print entries # debugging
    return render_template('base.html', the_text='No Tweets Yet')


@app.route('/test', methods=['GET'])
def contact():
    f = open('tweet_pickle','rb')
    tweet_list = cPickle.load(f)
    f.close()
    tweet_list = tweet_list.split()
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
    # name = request.args.get('name', 'Name error')
    # subject = request.args.get('subject', 'Subject Error')
    # email = request.args.get('email', 'Email Error')
    # full_subject = '{} - From: {} @ {}'.format(subject, name, email)
    # msg = Message(
    #     full_subject,
    #     sender=email,
    #     recipients=['tweet.track@gmail.com']
    # )
    # msg.body = request.args.get('message', 'Message error')
    # mail.send(msg)
    # return render_template('message_sent.html', name=name)

    return encoded



if __name__ == '__main__':
    app.run(debug=True)
