from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

# Load variables from the .env file
load_dotenv()

# Read credentials
URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")

# Create a connection to the database
driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD),
   
)

# Test the connection
with driver.session() as session:
    result = session.run("RETURN 'Connected Successfully!' AS message")
    print(result.single()["message"])

# Close the connection
driver.close()