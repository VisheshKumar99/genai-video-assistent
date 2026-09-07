from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
)


def split_transcript(data):
    text = data["text"]

    chunks = splitter.split_text(text)

    return {
        **data,
        "chunks": chunks,
    }