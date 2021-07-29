from speedtest import Speedtest
from datetime import datetime
import pandas as pd
import time

st = Speedtest()
mb = 10**-6
dt = datetime.today()
d = st.download()*mb
u = st.upload()*mb
#print(f"Velocidade de Download: {st.download()*mb} MB em {dt.strftime('%d/%m/%Y %H:%M')}  ") 
#print(f"Velocidade de Upload: {st.upload()*mb} MB em {dt.strftime('%d/%m/%Y %H:%M')}" )
i = 0


while i < 200:
    
    dt = datetime.today()
    d = st.download()*mb
    u = st.upload()*mb  
    df = pd.DataFrame({'data':dt, 'id':i, 'download':d,'upload':u},index=[i])
    i += 1
    time.sleep(1)
    #print(df)


