import os
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()

api_key = os.getenv("PINECONE_API_KEY")
index_name = "atlas-enterprise-ai-index"

if not api_key:
    raise ValueError("PINECONE_API_KEY is missing")

pc = Pinecone(api_key=api_key)

# List all indexes accessible with this API key
indexes = pc.list_indexes()

print("\nAvailable Pinecone indexes:")
for index in indexes:
    print(index)

# Verify the required index
if index_name in indexes.names():
    print("\nIndex FOUND!")

    index_info = pc.describe_index(index_name)
    print("Index details:", index_info)

    index = pc.Index(index_name)

    # Check actual vector count
    stats = index.describe_index_stats()
    print("\nVector statistics:")
    print(stats)

else:
    print("\nIndex NOT FOUND using this API key!")
