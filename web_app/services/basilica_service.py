from basilica import Connection
import os
from dotenv import load_dotenv

load_dotenv()
BASILICA_API_KEY = os.getenv("BASILICA_API_KEY", default="OOPS")
connection = Connection(BASILICA_API_KEY)

if __name__ == "__main__":
    pass

    #embeddings = list(connection.embed_sentences(sentences))
    # print(embeddings)
    # sentences = [
    #     "This is a sentence!",
    #     "This is a similar sentence!",
    #     "I don't think this sentence is very similar at all...",
    # ]
