from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd

# Create your views here.
def index(request):
    #data = pd.read_csv("static/gdscmitadt.csv")
    data = pd.read_csv("https://github.com/thehackerpanda/thehackerpanda.github.io/blob/gccp/assets/gdscmitadt.csv?raw=true")
    data['Total'] = data['# of Courses Completed'] + data['# of Skill Badges Completed']
    data.drop(data.columns[[1,2,3,4,5]], axis=1, inplace=True)
    df = data.sort_values(by=['Total'], ascending=False)

    return HttpResponse(df.to_html(index=False))