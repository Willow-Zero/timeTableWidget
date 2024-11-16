from google.transit import gtfs_realtime_pb2
import requests
import gtfs_kit as gk
import pandas as pd
import folium
import datetime
import config as c
import iconDict

if ((len(c.NYC)) > 0):
        import nyc

