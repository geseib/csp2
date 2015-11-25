import cspserver
import requests
import json
import argparse

default_server='10.90.16.41'
default_user='admin'
default_password='admin'



parser = argparse.ArgumentParser(description='CSP worker tool.')
parser.add_argument('service', type=str,nargs='?',help='name of the service')
parser.add_argument('--status', action='store_true',help='list attributes')
parser.add_argument('--list','-l', action='store_true',help='list services')
parser.add_argument('--down', action='store_true',help='down services')
parser.add_argument('--up', action='store_true',help='up services')
parser.add_argument('--delete', action='store_true',help='up services')
parser.add_argument('--count', type=int,nargs='?',default=0,help='used for a series of services')
parser.add_argument('--image', type=str,nargs=1,help='name of the image')
parser.add_argument('--debug', action='store_true',help='turn debugging on')

###override server default paramaters: IP,username, password
parser.add_argument('--server','-S', type=str,nargs=1,help='IP of the server',default=default_server)
parser.add_argument('--user', '-U', type=str,nargs=1,help='username for the CSP',default=default_user)
parser.add_argument('--password','-P', type=str,nargs=1,help='password for the CSP',default=default_password)

args=parser.parse_args()



def get_services():
    """Using the cspsever.csp object poll for a list of service on the CSP server"""
    print "get services happens here"


#START OF APP
print"=========================="
print"|     ACTCSP - 2015       |"
print"=========================="
print"\n"

my_server=cspserver.csp(args.server,args.user,args.password)
print my_server.ip
print my_server.user
#get a list of current services on CSP and store in variable plist
get_services()
if args.debug:
    print "Verbose Debuging on"

