import os,sys
import iec61850
import time

if __name__=="__main__":
  hostname = "192.168.253.226";
  tcpPort = 102
  if len(sys.argv)>1:
    hostname = sys.argv[1]
  if len(sys.argv)>2:
    port = sys.argv[2]
  con = iec61850.IedConnection_create()
  error = iec61850.IedConnection_connect(con,hostname,tcpPort)
  dataRCB =
  if (error == iec61850.IED_ERROR_OK):
    iec61850.IedConnection_close(con)
  iec61850.IedConnection_destroy(con)
