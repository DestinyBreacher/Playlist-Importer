from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json
import pickle
import os
from rando import l
creds=None
apikey='AIzaSyCN2KkWoDo0PG_daCvhMGps3ccimCvE2nA'

if os.path.exists("token.pickle"):
    print("YEEHAW")
    with open("token.pickle", "rb") as token:
        creds = pickle.load(token)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        print("refresh")
        creds.refresh(Request())
    else:
        print("getting")
        
        flow = InstalledAppFlow.from_client_secrets_file("pilla.json",
                                    scopes=['https://www.googleapis.com/auth/youtube.force-ssl']        
        )

        flow.run_local_server(prompt='consent')
        creds = flow.credentials
        with open("token.pickle","wb") as f:
            print("Saving for future")
            pickle.dump(creds,f)

youtube = build("youtube","v3",credentials=creds,developerKey=apikey)
request = youtube.playlists().insert( 
    part="snippet",
    body={'snippet': 
          {'title':"Anime Songs"}})

response=request.execute()
a=response['id']
print(a)
for i in l:
    request2 = youtube.search().list(
        part='snippet',
        maxResults=1,
        type='video',
        order='viewCount',
        q='{} anime full song'.format(i)
    )
    response2=request2.execute()
    print(response2, '\n')
    if len(response2['items']) != 0:
        vidid=response2['items'][0]['id']['videoId']
        request3 = youtube.playlistItems().insert( 
            part='snippet',
            body={
                'snippet':{
                'playlistId':'{}'.format(a),
                "resourceId":{
                    "videoId":'{}'.format(vidid),
                    'kind':"youtube#video"
                    }
                    }
                }
        )
        response3=request3.execute()
    else:
        continue
print("done")