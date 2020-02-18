# -*- coding: utf-8 -*- #
import time
import copy
import random
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
npd=[]
def getlist(tid):
    url='http://liuyan.people.com.cn/threads/queryThreadsList'
    data={
        'fid': 571,
        'lastItem': tid
    }
    headers={
        # 'accept':'application/json, text/javascript, */*; q=0.01',
		# 'Accept - Encoding': 'gzip, deflate',
		# 'Accept-Language': 'zh-CN,zh;q=0.9,en-IN;q=0.8,en',
		# 'Connection': 'no-cache',
		# 'Content-Length': '18',
		# 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		# 'Cookie': 'wdcid=493104400aca737f; aliyungf_tc=AQAAAN34MytoSA0AvhUScHMsjHE8j1v6; 4de1d0bdb25d4625be2481a1b9e1350f=WyIyMTEyODQ5ODQwIl0; ALLYESID4=130B09E3D64BB0BE; _ma_tk=maflfaydrw8po8w31f6ptrs9xazqb46l; _ma_is_new_u=1; _ma_starttm=1581765733872; sso_c=0; sfr=1; wdlast=1581775950; wdses=0c766af561de9998; JSESSIONID=2D1887EC9948998972A1E401FE6D80CF',
		# 'Host': 'liuyan.people.com.cn',
		# 'Origin': 'http://liuyan.people.com.cn',
		'Referer': 'http://liuyan.people.com.cn/threads/list?fid='+str(tid),
		'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
		# 'X-Requested-With': 'XMLHttpRequest'
    }
    try:
        res = requests.post(url,headers=headers,data=data)
        res.encoding='utf-8'#转换编码格式
    except Exception as e:
        print(e)
        data_df=np.array(npd)
        data = pd.DataFrame(data_df)
        writer = pd.ExcelWriter('Save_Excel1.xlsx')
        data.to_excel(writer,'page_1') # float_format 控制精度
        writer.save()
        getlist(tid)
        pass
    if res.status_code!=200:
        exit
    json=res.json()
    print(json)
    ls=json['responseData']
    li=0
    for i in ls:
        ld=[]
        t=0
        tt=i['tid']
        ld.append(tt)
        ld.append(i['forumName'])
        ld.append(i['subject'])
        ld.append(i['traceInfo'])
        ld.append(i['domainName'])
        ld.append(i['typeName'])
        if li==9:
            t=1
        li=li+1
        getcont(tt,ld,t)
    pass
def getcont(tid,ar,t):
    tf=random.uniform(0.1,0.2)
    time.sleep(tf)
    print(tid,t)
    arr=copy.deepcopy(ar)
    global npd
    url='http://liuyan.people.com.cn/threads/content'
    try:
        res=requests.get(url,params={'tid':tid})
        res.encoding='utf-8'#转换编码格式
        soup = BeautifulSoup(res.text,'html.parser')
        tx=soup.find('div',class_='liuyan_box03')
        tim=tx.find('h3',class_='grey2')
        ti="".join(tim.text.split())
        tis=ti[:-15]+'    '+ti[-15:-5]+' '+ti[-5:]
        if ti[-15:-5]<'2019-10-01':
            t=2
        # print(tis)
        arr.append(tis)
        cont=tx.find('p',class_='content')
        # print(cont.text)
        arr.append(cont.text)
        loc=cont.find_next()
        locs="".join(loc.text.split())
        arr.append(locs)
        npd.append(arr)
        if t==1:
            getlist(tid)
        elif t==2:
            print('已完成')
            data_df=np.asarray(npd)
            data = pd.DataFrame(data_df)
            writer = pd.ExcelWriter('Save_Excel1.xlsx')
            data.to_excel(writer,'page_1') # float_format 控制精度
            writer.save()
        pass
    except Exception as e:
        print(e)
        # print(res.bod)
        data_df=np.array(npd)
        data = pd.DataFrame(data_df)
        writer = pd.ExcelWriter('Save_Excel1.xlsx')
        data.to_excel(writer,'page_1') # float_format 控制精度
        writer.save()
        getcont(tid,ar,t)
        pass
def main():
    getlist(0)
    pass
if __name__ == "__main__":
    main()
    pass
