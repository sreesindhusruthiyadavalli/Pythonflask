from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurant.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()



class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        restaurants = session.query(Restaurant).all()
        try:
            if self.path.endswith("/restaurants"):
                restaurants = session.query(Restaurant).all()
                output = ""
                output += "<a href = '/restaurants/new'>Make a new restaurant name</a></br></br>"
                self.send_response(200)
                self.send_header('Content-type',	'text/html')
                self.end_headers()
                
                output += "<html><body>"
                for restaurant in restaurants:
                    
                    output += restaurant.name
                    output += "</br>"
                    output += "<a href = '#''> Edit </a> </br> <a href = '#''> Delete </a>"
                    output += "</br></br></br>"
                output += "</body></html>"
                self.wfile.write(output)
                return

            if self.path.endswith("/restaurants/new"):
                
                self.send_response(200)
                self.send_header('Content-type',    'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Make a new restaurant</h1>"
                
                output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/new'> "
                output += "<input name='newRestaurantName' type='text' placeholder = 'New Restaurant name'>"
                output += "<input type='submit' value='Create'>"
                output += "</form></body></html>"
                self.wfile.write(output)
                return
                
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            if self.path.endswith("/restaurants/new"):
                
                
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')

                #Create new restaurant class
                newRestaurant = Restaurant(name=messagecontent[0])
                session.add(newRestaurant)
                session.commit()   

                self.send_response(301)
                self.send_header('Content-type', 'text/html') 
                self.send_header('Location', '/restaurants')
                self.end_headers()
               
                #print output
        except:
            pass        
     

   

def main():
    try:
        server = HTTPServer(('', 8080), MyHandler)
        print 'Web server running...open localhost:8080/restaurants in your browser'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()