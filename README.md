# Script to replay HTTP requests from an Apache access logfile

Features

- Takes the time between requests into account
- Replaying can be sped up by a given factor
- Optionally send all requests to a selected (proxy) server

## Installation

Requires Python >= 2.6

Simply download the file and execute it...

## Usage

    Usage: apache-log-replay.py [options] logfile
    
    Options:
      -h, --help            show this help message and exit
      -p PROXY, --proxy=PROXY
                            send requests to server PROXY
      -s SPEEDUP, --speedup=SPEEDUP
                            make time run faster by factor SPEEDUP