PROCESSED_VIDEOS = set()


def check_video(data):
    video_id = data["video_id"]

    if video_id in PROCESSED_VIDEOS:
        return {
            **data,
            "already_processed": True,
        }

    PROCESSED_VIDEOS.add(video_id)

    return {
        **data,
        "already_processed": False,
    }