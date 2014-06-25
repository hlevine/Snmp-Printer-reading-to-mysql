import datetime
import urllib2
import MySQLdb
from pysnmp.entity.rfc3413.oneliner import cmdgen

#site name
site = 'office'
myip = urllib2.urlopen("http://myip.dnsdynamic.org/").read()
#ip range of printers
iprange = ["10.0.0.250","10.0.0.251","10.0.0.251","10.0.0.251"]
i=0
for item in iprange:
	cmdGen = cmdgen.CommandGenerator()
	errorIndication, errorStatus, errorIndex, values = cmdGen.getCmd(cmdgen.CommunityData('public'),cmdgen.UdpTransportTarget((iprange[i], 161)),'iso.3.6.1.2.1.43.5.1.1.17.1','iso.3.6.1.2.1.25.3.2.1.3.1','.1.3.6.1.4.1.11.2.3.9.4.2.1.4.1.2.7.0','iso.3.6.1.2.1.43.10.2.1.4.1.1','.1.3.6.1.2.1.43.11.1.1.9.1.1','.1.3.6.1.2.1.43.11.1.1.8.1.1','.1.3.6.1.2.1.43.11.1.1.9.1.2','.1.3.6.1.2.1.43.11.1.1.8.1.2','.1.3.6.1.2.1.43.11.1.1.9.1.3','.1.3.6.1.2.1.43.11.1.1.8.1.3','.1.3.6.1.2.1.43.11.1.1.9.1.4','.1.3.6.1.2.1.43.11.1.1.8.1.4','.1.3.6.1.2.1.43.11.1.1.9.1.5','.1.3.6.1.2.1.43.11.1.1.8.1.5','.1.3.6.1.2.1.43.11.1.1.9.1.6','.1.3.6.1.2.1.43.11.1.1.8.1.6')
	if errorIndication==None:
		model = values[1][1]
		serial = values[0][1]
		tc = values[3][1]
		colc = values[2][1]
		bl = values[4][1]
		blt = values[5][1]
		cl = values[6][1]
		clt = values[7][1]
		ml = values[8][1]
		mlt = values[9][1]
		yl = values[10][1]
		ylt = values[11][1]
		trans = values[12][1]
		transt = values[13][1]
		fuser = values[14][1]
		fusert = values[15][1]
		date = datetime.datetime.now()
		db = MySQLdb.connect(host="your_db_host",user="youruser",passwd="yourpass",db="your_db_name")
		cur = db.cursor()
		cur.execute("""INSERT INTO reading (model,serial,target_ip,total_count,colour_count,loc,collector_date,site_ip,bl,blt,cl,clt,ml,mlt,yl,ylt,trans,transt,fuser,fusert) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """,(model,serial,iprange[i],tc,colc,site,date,myip,bl,blt,cl,clt,ml,mlt,yl,ylt,trans,transt,fuser,fusert))
		i=i+1
	else:
		model = 'NO PRINTER'
		serial = 'NO PRINTER'
		tc = 'NO PRINTER'
		colc = 'NO PRINTER'
		date = datetime.datetime.now()
		db = MySQLdb.connect(host="your_db_host",user="youruser",passwd="yourpass",db="your_db_name")
		cur = db.cursor()
		cur.execute("""INSERT INTO reading (model,serial,target_ip,total_count,colour_count,loc,collector_date,site_ip) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) """,(model,serial,iprange[i],tc,colc,site,date,myip))
		i=i+1
