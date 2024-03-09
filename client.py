import pysolr

# Step 1: Connect to Solr
# Assuming Solr is running on the default port (8983) and "mycollection" is the name of your collection
solr_url = 'http://localhost:8983/solr/mycollection'
solr = pysolr.Solr(solr_url, timeout=10)

# Step 2: Add Documents to Solr
# Each document is a dictionary where the keys are schema fields and the values are the data for those fields
documents = [
    {"id": "1", "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": "2", "title": "Moby Dick", "author": "Herman Melville"},
    {"id": "3", "title": "War and Peace", "author": "Leo Tolstoy"},
]

# Add the documents to Solr
solr.add(documents)

# Commit changes to make sure documents are searchable
solr.commit()

# Step 3: Search Documents
# Perform a search query that searches for any document with the word "great" in the title
results = solr.search('title:Great')

print("Searched for 'title:Great', found {} documents.".format(len(results)))
for result in results:
    print("Title: {}, Author: {}".format(result['title'], result['author']))
