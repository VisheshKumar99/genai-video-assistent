from urllib.parse import urlparse, parse_qs

def extract_video_id(data: dict) -> dict:
    url = data["youtube_url"]

    parsed = urlparse(url)

    if parsed.hostname in ("youtube.com", "www.youtube.com"):
        video_id = parse_qs(parsed.query).get("v", [None])[0]

    elif parsed.hostname == "youtu.be":
        video_id = parsed.path.lstrip("/")

    else:
        raise ValueError("Invalid YouTube URL")

    if not video_id:
        raise ValueError("Could not extract YouTube video ID")

    return {
        **data,
        "video_id": video_id,
    }

