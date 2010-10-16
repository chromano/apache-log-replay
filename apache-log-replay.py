#!/usr/bin/env python2.5
from datetime import datetime
import sys
import time
from urllib2 import urlopen

def main(host, filename):
    logfile = open(filename, "r")
    requests = []
    for line in logfile:
        parts = line.split(" ")
        if len(parts) != 24:
            continue
        time_text = parts[3][1:]
        request_time = datetime.strptime(time_text, "%d/%b/%Y:%H:%M:%S")
        path = parts[6]
        requests.append((request_time, path))
    if not requests:
        print "Seems like I don't know how to parse this file!"
        return

    total_delta = requests[-1][0] - requests[0][0]
    print "%d requests to go (time: %s)" % (len(requests), total_delta)
    last_time = requests[0][0]
    for request_time, path in requests:
        time_delta = request_time - last_time
        if time_delta:
            if time_delta.seconds > 10:
                print "(next request in %d seconds)" % time_delta.seconds
            time.sleep(time_delta.seconds)
        last_time = request_time
        url = host + path
        try:
            req_result = "OK"
            urlopen(url)
        except Exception:
            req_result = "FAILED"
        print ("[%s] REQUEST: %s -- %s"
               % (request_time.strftime("%H:%M:%S"), url, req_result))

def usage():
    print "%s <host> <logfile>" % sys.argv[0]

if __name__ == "__main__":
    if not len(sys.argv) == 3:
        usage()
    else:
        main(sys.argv[1], sys.argv[2])

