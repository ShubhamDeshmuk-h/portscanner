import sys
import socket
from datetime import datetime
import threading



def scan_port(target,port):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #this is ipv4 for the system which uses somethings

        #we are putting time out

        s.settimeout(1)
        #setup a result to variable

        result = s.connect_ex((target,port))  #this is error indicator which will check for the indicator if any port is open
        #if port is 0 then we get some output and it result is not equal to zero then we get some kind of output lets goo

        if result == 0 :
            print(f"Port {port} is open")
        
    except socket.error as e:
        print(f"Socket error on port {port}:{e}")

        #we allways need to handle error in all the way  it's a good practice before any porgram always make sure to put handle error

    except Exception as e:
        print(f"Unexcepted error on port {port}:{e}")



#this is main function which is target and all


def main():
    if len(sys.argv) == 2:
        target = sys.argv[1]
    #what is meaning of this when we run somehting like python.exe scanner.py then
    # we get our script over there so IP address 
    # script = python.exe scanner.py 192.168.1.1
    else:
        print("Invalide number of arguments.")
        print("usage: python.exe scanner.py <target>")
        sys.exit(1)

    
    #resolve target to hostname to target ip address so what can we do for it


    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"Error: Unable to resolve hostname {target}")
        sys.exit(1)

    #now adding pretty banner which will look good over terminal for the use

    print("-"*50)
    print(f"Scanning target {target_ip}")
    print(f"Time started: {datetime.now()}")
    print("-"*50)

    try:
        #we are going to use multithreading to scan port using concurrently all port scanning

        # this will save time as we are going for fast us
        threats = []
        for port in range(1,65535):
            #here we have used our scan port function for the use of the scanning
            thread = threading.Thread(target=scan_port,args=(target_ip,port))
            threats.append(thread)
            thread.start()

        
        #wait to for all the threats to complete how to do it 
        for thread in threats:
            thread.join()
            #main thread is paused for the scanning until it is done
    except KeyboardInterrupt:
        print("\nExiting program")
        sys.exit(0)
    except socket.error as e:
        print(f"Socket error:{e}")

    print("\nScan completed")

if __name__ == "__main__":
    main()
#this does hey we are not running this script directly if we are trying to import this one that program
#so this should work on the other program too so we need to add above two line so we can get the required things


