

from speedtest import Speedtest
import matplotlib.pyplot as fig
from datetime import datetime
import pandas as pd
import os
import time


def cont():
        dt = datetime.today()
        dtf = '23:59'
        ag = int(dt.strftime('%H:%M').replace(":",""))
        fi = int(dtf.replace(":",""))
        r = fi - ag

        return r
st = Speedtest()
mb = 10**-6
dt = datetime.today()
d = st.download()*mb
u = st.upload()*mb
i = 0
c = 300
p_d = d / c 

df = pd.DataFrame({'data':dt, 'id':i, 'download':d,'upload':u, '%':"{:.2%}".format(p_d)},index=[0])

i = 0

while i < cont():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    dt = datetime.today()
    d = st.download()*mb
    u = st.upload()*mb  
    p_d = d / c 
    dfn = ([dt,len(df),d,u,"{:.2%}".format(p_d)])
    df.loc[len(df)] =  dfn 
    print(df.sort_values(by=['id'], ascending = False))
    time.sleep(30)
    

for i in range(cont()):
        ax = fig.subsplot(111)   
        fig.pause(1)
        ax.plot(x=['id'],y=['download'])
i = cont() -1

