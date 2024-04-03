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
  data = [["OHL1BCUMEASUREMENT1/powMMXU1.TotW.mag.f","MX"],["OHL1BCUMEASUREMENT1/powMMXU1.TotVAr.mag.f","MX"],["OHL1BCUCONTROL1/CSWI1.Pos.stVal","ST"]]

  if (error == iec61850.IED_ERROR_OK):
    daread = data[2][0]
    dafc = eval(str("iec61850.IEC61850_FC_"+str(data[2][1])))
    readobj=iec61850.IedConnection_readObject(con,daread,dafc)
    print(str(daread+" "+str(readobj)))
    val=iec61850.MmsValue_getBitStringAsIntegerBigEndian(readobj[0])
    print(val)
    iec61850.IedConnection_close(con)
  iec61850.IedConnection_destroy(con)
    
  
