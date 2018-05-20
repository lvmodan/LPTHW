#!/usr/bin/env python
# coding=utf-8
import web
from gothonweb import map, game
#from gothonweb.game import *

urls = (
    '/game', 'GameEngine',
    '/', 'Index'
)

app = web.application(urls, globals())

if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store, initializer={'room': None})
    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates/', base = 'lay_out')

class Index(object):
    def GET(self):
        session.room = game.START
        web.seeother('/game')
class GameEngine(object):
    def GET(self):
        if session.room:
            return render.show_room(room=session.room)
        else:
            return render.death()

    def POST(self):
        form = web.input(action = None)
        if session.room and form.action:
            session.room = session.room.go(form.action)

        web.seeother('/game')

if __name__ == "__main__":
    app.run()
