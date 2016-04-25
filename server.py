#Name: Vivek Arvind Balaji
#UTA id: 1001108300


#Code References
#https://wiki.python.org/moin/BaseHttpServer
#https://docs.python.org/3/library/http.server.html
#http://pymotw.com/2/BaseHTTPServer/index.html#module-BaseHTTPServer


from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import SimpleHTTPServer
import sys
import threading
import os
import time


if sys.argv[1:]:
    port = int(sys.argv[1]) #port number - first command line argument
else:
    port = 8080 #if port number is not given explicitly, default port '8080' is assigned
    
class GetHandler(BaseHTTPRequestHandler): #handler class for handling the incoming http requests
    
    def do_HEAD(self): #overriding the do_HEAD function
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		return
    		
    def do_GET(self): #overriding the do_GET function
		parent_dir = '/Users/VA/Documents/MS/Acads/Summer15/CSE5344ComputerNetworks/Project/server/' #change this directory to the folder where the server file and html code exists
		thread_id = threading.current_thread().getName(); #retrieve the thread id
		try:
			extensions = set(['.html','.htm']) #set of accepted extensions
			extension = os.path.splitext(self.path)[1] #extracting the extension of the given file
			if extension in extensions: #to handle http file requests
				if parent_dir in self.path: #to check if full path is given or not
					file_path = self.path
				else: #if full path is not given, the file name is added to the parent directory
					file_path = parent_dir + self.path
				f = open(file_path) 
				print 'Current thread: %s' % thread_id;
				self.send_response(200); #response of 200 implies that the file is found
				self.send_header('Content-type','text/html') #including the content info in the header
				self.end_headers(); #end of header information
				self.wfile.write(f.read()); #write the contents of the file
				self.wfile.write(thread_id); #write the corresponding thread id
				self.wfile.write('\n');
				return
			else: #this is to handle the empty requests i.e., if the file name is not mentioned.
				file_path = parent_dir + 'default.html' #default page to be displayed
				f = open(file_path)
				print 'Current thread: %s' % thread_id;
				self.end_headers(); 
				self.wfile.write(f.read()); #write the contents of the default page
				self.wfile.write('Default page handled by ');
				self.wfile.write(thread_id); #write the corresponding thread id
				self.wfile.write('\n');
				return
		except IOError: #this is to handle wrong http requests i.e., if a file is absent in the server
			self.wfile.write(thread_id)
			self.wfile.write('\n');
			self.send_error(404, 'File Not Found') #send_error is used to display a 404 error with an optional message to the client
			
			        
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer): #class to handle requests in a separate thread
    """Handle requests in a separate thread."""

if __name__ == '__main__':
	
	server = ThreadedHTTPServer(('localhost', 8080), GetHandler); #initialising the server
	print "Server Starts:",time.asctime() #timestamp at which the server starts
	print 'Server Running, use <Ctrl-C> to stop'
	try:
		server.serve_forever() #this is to keep the server running until an interrupt occurs
	except KeyboardInterrupt:
		server.server_close() #server closes when there is a keyboard interrupt
		print "\nServer Stops:",time.asctime() #timestamp at which the server stops    