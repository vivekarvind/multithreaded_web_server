Building a Simple Web Client and a Multithreaded Web Server

Steps for execution:
1. Extract the zip file. It contains six files viz., server.py, client.py, index.html, index.htm, default.html and Readme.txt
2. server.py and client.py are the files containing the source codes.
3. Open two python terminals windows, and change the working directory to the extracted folder using the command 'cd <file_path>'.
4. In the first terminal window, run the server code using the command 'python server.py <port_no>'. If the command line argument <port_no> is not given, the default port 8080 will be assigned. Now the server will start and it will keep running.
5. In the second terminal window, run the client code using the command 'python client.py <server_name> <file_name> <port_no>'. If the command line argument <server_name> is not given, the default name 'localhost' is assigned. If the command line argument <file_name> is not given, the default name 'index.html' is assigned. If the command line argument <port_no> is not given, the default port 8080 will be assigned. 
6. You can see the output in both the terminal windows.
7. To give an http request from the browser, open any web browser and type 'http://localhost:8080/<file_name>'. If <file_name> is not specified, the server will redirect you to a default page. 
8. You can also test the code by entering the full path of the file provided the file is in the same directory as the folder. This can be done by 'http://localhost:8080/<full_path>'. 


Code References:
1. https://wiki.python.org/moin/BaseHttpServer
2. https://docs.python.org/3/library/http.server.html
3. http://pymotw.com/2/BaseHTTPServer/index.html#module-BaseHTTPServer
4.http://stackoverflow.com/questions/15518534/simple-http-client-and-server-in-python-but-client-making-atleast-50-request-sim


Software Required:
1. Python 2.7.9

