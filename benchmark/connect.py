from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

# Load selected environment file
ENV_FILE = os.getenv("ENV_FILE", ".env")
load_dotenv(ENV_FILE)

# Read credentials
URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")

# Print what we're connecting to (don't print the password)
print("ENV_FILE:", ENV_FILE)
print("URI:", URI)
print("USERNAME:", USERNAME)

# Create connection
driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

# Test connection
with driver.session() as session:
    result = session.run("RETURN 'Connected Successfully!' AS message")
    print(result.single()["message"])

driver.close()