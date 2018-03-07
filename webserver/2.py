import http.server
from http.server import BaseHTTPRequestHandler,HTTPServer
class RequestHandler(BaseHTTPRequestHandler):

    '''监听　http　请求　返回／page'''
    #page to send back
    Page = '''\
<html>
<body>
<tr>  <td>Header</td>  <td>Value</td>               </tr>
<tr>  <td>Date and time</td>  <td>{date_time}</td>  </tr>
<tr>  <td>Client host</td>  <td>{client_host}</td>  </tr>
<tr>  <td>client port</td>  <td>{client_port}</th>  </tr>
<tr>  <td>commond</td>  <td>{commond}</td>          </tr>
<tr>  <td>Path</td>  <td>{path}</td>                </tr>
</body>
</html>
'''
    #监听一个ＧＥＴ请求
    def do_GET(self):
        page =self.creat_page()
        self.send_page(page)
    def creat_page(self):
        values = {
                'date_time'     :self.date_time_string(),
                'client_host'   :self.client_address[0],
                'client_port'   :self.client_address[1],
                'commond'       :self.command,
                'path'          :self.path
                }
        page = self.Page.format(**values)
        return page

    def send_page(self,page):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.send_header("Content-Length",str(len(page)))
        self.end_headers()
        self.wfile.write(page)







if __name__=='__main__':
    serverAddress = ('',8080)
    server = HTTPServer(serverAddress,RequestHandler)
    server.serve_forever()

