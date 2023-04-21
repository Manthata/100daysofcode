from fastapi import FastAPI, Response
from pytube import YouTube
import requests
from io import BytesIO
import facebook

app = FastAPI()

@app.get("/download/youtubevideo")
def download_youtube_video(url: str) -> bytes:
    """
    This function is responsible for downloading videos from youtube

    Args:
        url (str): url of the video you want to download

    Returns:
        bytes: mp4 video
    """

    # Initialize the YouTube object
    yt = YouTube(url)

    # Choose the highest resolution stream
    # stream = yt.streams.get_highest_resolution()
    stream = yt.streams.filter(file_extension="mp4").get_by_resolution("360p")
    buffer = BytesIO()
    # Download the video to a BytesIO buffer
    stream.stream_to_buffer(buffer)


    # Get the bytes from the buffer
    video_bytes = buffer.getvalue()

    # Create a FastAPI response object with the video bytes and content type
    response = Response(content=video_bytes, media_type="video/mp4")

    return response


@app.get("/download/facebookvideo")
def download_facebook_video(url: str) -> bytes:
    """
    This function is responsible for downloading videos from Facebook.

    Args:
        url (str): url of the video you want to download

    Returns:
        bytes: mp4 video
    """

    # Parse the video ID from the URL
    video_id = url.split("/")[-1]

    # Initialize the Facebook Graph API with an access token
    access_token = "<your_access_token>"
    graph = facebook.GraphAPI(access_token)

    # Retrieve the video's metadata
    video = graph.get_object(id=video_id, fields="source")

    # Download the video
    video_url = video["source"]
    response = requests.get(video_url)
    video_bytes = BytesIO(response.content).getvalue()

    # Create a FastAPI response object with the video bytes and content type
    response = Response(content=video_bytes, media_type="video/mp4")

    return response