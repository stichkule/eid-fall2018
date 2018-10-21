import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import csv

'''
This is a simple Websocket Echo server that uses the Tornado websocket handler.
This program connects to a client application, and serves data to it according to the message request.
The data passed over is contained in the temp_rh_data.csv file (that is populated by temp_rh_app.py).
''' 
 
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        '''indicates new connection'''
        print('new connection')
      
    def on_message(self, message):
        '''function to handle incoming message request, and provide response data accordingly'''
        with open('temp_rh_data.csv', 'r') as csvfile: #open and read data file
            reader = csv.reader(csvfile)
            for row in reader:
                data = row
                
        print('message received:  %s' % message)
        # send data to client application in accordance with received request
        if message == "CurrTemp":
            response = "1,"+data[1]+","+data[0]+","+data[13]
        elif message == "CurrHum":
            response = "2,"+data[3]+","+data[0]+","+data[13]
        elif message == "AvgTemp":
            response = "3,"+data[2]+","+data[0]+","+data[13]
        elif message == "AvgHum":
            response = "4,"+data[4]+","+data[0]+","+data[13]
        elif message == "HighTemp":
            response = "5,"+data[8]+","+data[7]+","+data[13]
        elif message == "LowTemp":
            response = "6,"+data[6]+","+data[5]+","+data[13]
        elif message == "HighHum":
            response = "7,"+data[10]+","+data[9]+","+data[13]
        elif message == "LowHum":
            response = "8,"+data[12]+","+data[11]+","+data[13]
        else:
            response = message[::-1]
        print('sending back message: %s' % response)
        self.write_message(response)
 
    def on_close(self):
        '''indicates connection closed'''
        print('connection closed')
 
    def check_origin(self, origin):
        return True
 
application = tornado.web.Application([
    (r'/ws', WSHandler),
])
 
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application) #start http server
    http_server.listen(8888) #listen for incoming connections
    myIP = socket.gethostbyname(socket.gethostname()) #get IP address of server
    print('*** Websocket Server Started at %s***' % myIP)
    tornado.ioloop.IOLoop.instance().start() #start tornado IOloop instance for continuous listening of incoming requests
