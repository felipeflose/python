


from speedtest import Speedtest
from datetime import datetime
import pandas as pd
import os



st = Speedtest()
mb = 10**-6
dt = datetime.today()
d = st.download()*mb
u = st.upload()*mb
i = 0
df = pd.DataFrame({'data':dt, 'id':i, 'download':d,'upload':u},index=[0])


while i < 1440:

    os.system('clear')
    dt = datetime.today()
    d = st.download()*mb
    u = st.upload()*mb  
    dfn = ([dt,len(df),d,u])
    df.loc[len(df)] =  dfn 
    print(df.sort_values(by=['id'], ascending = False))
    i += 1