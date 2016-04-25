#Name: Vivek Arvind Balaji
#UTA id: 1001108300


#Code References
#http://stackoverflow.com/questions/15518534/simple-http-client-and-server-in-python-but-client-making-atleast-50-request-sim


from httplib import HTTPConnection
import sys

if sys.argv[1:]: 
    server_name = str(sys.argv[1]) #first command line argument - server name
else:
    server_name = "localhost" #if server name is not given explicitly, the default name 'localhost' is assigned

if sys.argv[2:]:
    file_name = str(sys.argv[2]) #second command line argument - file name
else:
    file_name = "index.html" #if file name is not given explicitly, the default name 'index.html' is assigned

if sys.argv[3:]: 
    port_no = int(sys.argv[3]) #third command line argument - port number
else:
    port_no = 8080 #if port number is not given explicitly, default port '8080' is assigned

conn_obj = HTTPConnection(server_name, port_no) #initializing the connection object with the server_name and port number
conn_obj.request("GET", file_name) #issuing a GET request to the server
resp_obj = conn_obj.getresponse() #receiving the response from the server
print resp_obj.status, resp_obj.reason; 
print 'Received data:', resp_obj.read() #print the received data
conn_obj.close(); #close the connection