import threading
 
# Creating threads
# IP list is from the file with all of the IP Addresses
def create_threads(iplist, function):
 
    threads = []
 
    for ip in iplist:
        th = threading.Thread(target = function, args = (ip,))   #args is a tuple with a single element
        th.start()
        threads.append(th)
        
    for th in threads:
        th.join()