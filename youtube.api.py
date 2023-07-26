
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Replace 'YOUR_API_KEY' with your actual API key obtained from the Google Developers Console.
API_KEY = 'AIzaSyBFj4C2xF_qOnTzHdDnbZSmrqWaWSy9xpA'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def search_videos(query, max_results=10):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)

    try:
        search_response = youtube.search().list(
            q=query,
            type='video',
            part='id,snippet',
            maxResults=max_results
        ).execute()

        for search_result in search_response.get('items', []):
            video_id = search_result['id']['videoId']
            title = search_result['snippet']['title']
            print(f"Title: {title}, Video ID: {video_id}")

    except HttpError as e:
        print(f"An HTTP error occurred: {e}")

# Usage example:
search_videos('c++ Tutorial')


def get_video_details(video_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)

    try:
        video_response = youtube.videos().list(
            part='snippet,statistics',
            id=video_id
        ).execute()

        if video_response['items']:
            video = video_response['items'][0]
            title = video['snippet']['title']
            views = video['statistics']['viewCount']
            likes = video['statistics']['likeCount']
            dislikes = video['statistics']['dislikeCount']
            print(f"Title: {title}, Views: {views}, Likes: {likes}, Dislikes: {dislikes}")

        else:
            print("Video not found.")

    except HttpError as e:
        print(f"An HTTP error occurred: {e}")

