from langchain_core.runnables import RunnableLambda
from helperfunction.helper import extract_video_id
from helperfunction.checkvideo import check_video
from helperfunction.fetchTranscript import fetch_transcript, clean_transcript


def split_transcript(data):
    return


def generate_embeddings(data):
    return


def store_vectors(data):
    return



# pipeline = RunnableLambda(extract_video_id) | RunnableLambda(check_video) | RunnableLambda(fetch_transcript)
pipeline = (
    RunnableLambda(extract_video_id)
    | RunnableLambda(check_video)
    | RunnableLambda(fetch_transcript)
    | RunnableLambda(clean_transcript)
)

def handler(event, context):
    result = pipeline.invoke(event)

    return {
        "statusCode": 200,
        "body": result,
    }

if __name__ == "__main__":
    event = {
        "youtube_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    }

    result = handler(event, None)

    # print("Video ID:", result["body"]["video_id"])
    # print("Already processed:", result["body"]["already_processed"])
    # print("Clean text:")
    # print(result["body"]["text"])