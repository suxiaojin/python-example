from http import client
httpclient=client.HTTPConnection('explorer.whitecoin.info', timeout=5)
httpclient.request('GET', '/tokenswap_stat.json')
response=httpclient.getresponse()
print('status:')
print(response.status)

#############################################################################################################

from http import client
httpclient=client.HTTPConnection('explorer.whitecoin.info', timeout=5)
httpclient.request('GET', '/swap_stat/liquidity/all')
response=httpclient.getresponse()
print('status:')
print(response.status)

##############################################################################################################

from http import client
httpclient=client.HTTPConnection('explorer.whitecoin.info', timeout=5)
httpclient.request('POST', '/api/getDayTrxNum')
response=httpclient.getresponse()
print('status:')
print(response.status)
