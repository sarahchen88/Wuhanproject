import folium
import pandas as pd
from folium.plugins import HeatMapWithTime

current_coordinate=(31.829405,117.266164)
masterdata=pd.read_csv('locdetail_2.csv') #need to update file name
max_records=1000
Map=folium.Map(location=current_coordinate,
               tiles='http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=7&x={x}&y={y}&z={z}',
               attr='default',
               zoom_start=12)

masterdata['latitude'] = masterdata['latitude'].astype(float)
masterdata['longitude'] = masterdata['longitude'].astype(float)
masterdata=masterdata.dropna(subset=['latitude','longitude','Weight','Date'])

heatdata = [[[row['latitude'],row['longitude'],row['Weight']] for index, row in masterdata.iterrows()]]

time_index=[
    (masterdata['Date']).values.tolist() for
    k in range(len(heatdata))]
HeatMapWithTime(heatdata,index=time_index,min_opacity=0.5, max_opacity=0.8, use_local_extrema=True).add_to(Map)

#Map.fit_bounds(Map.get_bounds())

#Save the map to an HTML file
Map.save('Wuhan_draft_v2.html')
Map