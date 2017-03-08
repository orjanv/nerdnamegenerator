from flup.server.fcgi import WSGIServer
from nerdnamegenerator import app

if __name__ == '__main__':
  WSGIServer(app, bindAddress = '/tmp/nerdnamegenerator-fcgi.sock').run()
