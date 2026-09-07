from youtube_transcript_api import YouTubeTranscriptApi


def fetch_transcript(data):
    video_id = data["video_id"]

    transcript = YouTubeTranscriptApi().fetch(video_id)

    return {
        **data,
        "transcript": transcript,
    }

def clean_transcript(data):
    transcript = data["transcript"]
    # print('transcript', transcript.snippets)
    text = " ".join(
        snippet.text
        for snippet in transcript.snippets
    )

    return {
        **data,
        "text": text,
    }