#!/usr/bin/env python
import gdax,sys,time
from datetime import datetime
from dateutil import tz

public_client = gdax.PublicClient()
print '%17s%20s%12s%12s' % ("Time(EST)", "BTC-USD", "ETH-USD", "LTC-USD")

def getbtcprice():
        btcreq = public_client.get_product_ticker(product_id='BTC-USD')
        btcprice = btcreq['bid']
        return btcprice

def getethprice():
	ethreq = public_client.get_product_ticker(product_id='ETH-USD')
	ethprice = ethreq['bid']
	return ethprice

def getltcprice():
        ltcreq = public_client.get_product_ticker(product_id='LTC-USD')
        ltcprice = ltcreq['bid']
        return ltcprice

def gettime():
	ethreq = public_client.get_product_ticker(product_id='ETH-USD')
	ethtime = str(ethreq['time'])
        ethtime = ethtime.replace("T", "")
        ethtime = ethtime.split(".")[0]
	from_zone = tz.gettz('UTC')
	to_zone = tz.gettz('America/New_York')
	utc = datetime.utcnow()
	utc = datetime.strptime(ethtime, '%Y-%m-%d%H:%M:%S')
	utc = utc.replace(tzinfo=from_zone)
	est = utc.astimezone(to_zone)
	return est

try:
	while True:
        	print '%-12s%12s%12s%12s' % (gettime(),getbtcprice(),getethprice(),getltcprice())
        	time.sleep(0.5)
		continue
except KeyboardInterrupt:
	pass

