import http.server
from http.server import BaseHTTPRequestHandler,HTTPServer
class RequestHandler(BaseHTTPRequestHandler):

    '''监听　http　请求　返回／page'''
    #page to send back
    Page = '''\
<html>
<body>
<p>hello ,world </p>
</body>
</html>
'''
    #监听一个ＧＥＴ请求
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type","text/html")
        self.send_header("Content-Length",str(len(self.Page)))
        self.end_headers()
        self.wfile.write(self.Page)





if __name__=='__main__':
    serverAddress = ('',8080)
    server = HTTPServer(serverAddress,RequestHandler)
    server.serve_forever()

