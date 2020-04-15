import aiohttp
import asyncio
import datetime
import time
from threading import Thread
#{'HotelID': '14DE8691', 'LockID': 'FD13122E', 'MsgType': 4, 'Action': {'Msg': 'Open Remote Lock Received'}}
#{"LockID":"FD13122E","MsgType":19,"MsgIndex":886,"Action":
#{"GatewayID":"201FD8054D59383454632143","BackLockState":"false","DoorLockState":"false","DoorCloseState":"false","Battery":25,"RSSI":-57}}
##{'HotelID': '14DE8691',"LockID":"FD13122E","MsgType":32,"MsgIndex":255,"Action":{"GatewayID":"111FDA054D57353327501943","Major":5,"Minor":29,"Battery":16,"Stamp":"5CC17FB0","RSSI":-28}}
# mydict = dict()
# mydict['HotelID'] = '14DE8691'
# mydict['LockID'] = 'FD13122E'
# mydict['MsgType'] = 19
# mydict['Action'] = dict()
# mydict['Action']['GatewayID'] = '201FD8054D59383454632143'
# mydict['Action']['BackLockState'] = 'false'
# mydict['Action']['DoorLockState'] = 'false'
# mydict['Action']['DoorCloseState'] = 'false'
# mydict['Action']['Battery'] = 25
# mydict['Action']['RSSI'] = -57
# {"LockID":"5C666669","MsgType":17,"MsgIndex":2517,"Action":{"Pwr_SW_CardNo":"90EFCA5F","State":"On","GatewayID":"201FD5054D59383459351643"}}
mydict = dict()
mydict['HotelID'] = '3C834277'
mydict['LockID'] = '5C35EC9D'
mydict['MsgType'] = 53
mydict['Action'] = dict()
mydict['Action']['Msg'] = 'Pwr_SW Unbinding'
# mydict['Action']['Pwr_SW_Type'] = 'Card' # 90EFCA5F
# mydict['Action']['Pwr_SW_CardNo'] = '90EFCA5F' # 90EFCA5F

#{'HotelID': 'E4B54F48', 'LockID': '5C666669', 'MsgType': 23, 'Action': {'Pwr_SW_State': 'On', 'Pwr_SW_Type': 'Card', 'Pwr_SW_CardNo': '90EFCA5F', 'Type': 1, 'Major': 1, 'Minor': 1}}

#{"LockID":"5C666669","MsgType":53,"MsgIndex":100,"Action":{"Msg":"Pwr_SW Unbinding"}}
headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 '
                            '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

async def fetch(session,url,mydata):
    async with session.post(url, json = mydata, headers = headers) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session,'https://api.weixin.qq.com/tcb/invokecloudfunction?access_token=22_s9sAQFXK94sqsJzZcaBAVHd4wpJGljjS70scE-aWwB754QhJ_xo_YVaOEmguBfHezEaaU_yrdjkhaha-Q5yzX4NZcWwqcopAWhl-WXajLPWm6le3N4TNvKqigIZRKLvDTaP4f9RzEqIKLB8DTSVgAAAGFI&env=demo-b96s0&name=addMessage',mydict)
        print(html)
print(mydict)
start = datetime.datetime.now()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
end = datetime.datetime.now()
during = (end - start).microseconds / 1000
print('Post消耗时间：{}ms'.format(during))

# now = lambda : time.time()
# async def do_some_work(x):
#     #time.sleep(1)
#     await asyncio.sleep(x)
#     print('Waiting: {}'.format(x))
#     return 'Done after {}s'.format(x)

# def callback(future):
#     print('Callback:{}'.format(future.result()))

# start = now()
# coroutine1 = do_some_work(4)
# coroutine2 = do_some_work(2)
# coroutine3 = do_some_work(1)

# tasks = [asyncio.ensure_future(coroutine1),asyncio.ensure_future(coroutine2),asyncio.ensure_future(coroutine3)]
# loop = asyncio.get_event_loop()
# #task = asyncio.ensure_future(coroutine)
# #task = loop.create_task(coroutine)
# #print(tasks)
# loop.run_until_complete(asyncio.wait(tasks))

# for task in tasks:
#     print('Task ret : {}'.format(task.result()))

# print('time : {}'.format(now() - start))