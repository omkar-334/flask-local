
import pandas as pd
import time
from google.cloud import storage
from io import BytesIO

start=time.time()
client = storage.Client()
bucket = client.get_bucket('fees_bucket')
blob = bucket.blob('feescopy1.xlsx')
content = blob.download_as_string()
file = BytesIO(content)

cols=[1,2,3,7,13,11]
out=pd.read_excel(
        io=file,
        sheet_name='Student Master',
        converters={'Cell':str,'Adm':str},
        usecols=cols)
print(out.head())
print(time.time()-start)