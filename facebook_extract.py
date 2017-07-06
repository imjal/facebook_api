import requests
import random
import json
import pandas as pd
import iso8601
import matplotlib.pyplot as plt
import numpy
from datetime import datetime


def req_facebook(req, access_token):
    api_endpoint = "https://graph.facebook.com/v2.9/"
    url = api_endpoint + req + "&access_token="+access_token
    r = requests.get(url)
    return r;

def clean_data(results):
    a = results.json()
    dict_time_likes = {}
    for j in range(5):
        print(a['friends']['data'][j]['name'])
        for i in range(25):
            try:
                num_of_likes = a['friends']['data'][j]['photos']['data'][i]['likes']['summary']['total_count']

                time_created = iso8601.parse_date(a['friends']['data'][j]['photos']['data'][i]['created_time'])
                dict_time_likes.update({time_created: num_of_likes})
            except KeyError:
                break;
            except IndexError:
                print("number of photos: ", i)
                break;
    return dict_time_likes


