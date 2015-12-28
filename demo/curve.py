# Import system modules
import os
import xapian
import glob

# Set paths
indexPath = 'data/indices'
documentPath = 'data/documents'
# Specify the value slot to store each document's file name
xapian_file_name = 0

# Create the Xapian database
database = xapian.WritableDatabase(indexPath, xapian.DB_CREATE_OR_OPEN)
# Initialize indexer
indexer = xapian.TermGenerator()
# Set word stemmer to English
indexer.set_stemmer(xapian.Stem('english'))
import textract
# For each text file,
for filePath in glob.glob(os.path.join(documentPath, '*')):
    # Load content
    print filePath, filePath[-4:]
    if filePath[-4:]=='.txt':
		content = open(filePath).read()
    else :
		content = textract.process(filePath)
    
    content=''.join([i if ord(i) < 128 else ' ' for i in content])

    # Prepare document
    document = xapian.Document()
    document.set_data(content)
    # Store fileName
    fileName = os.path.basename(filePath)
    document.add_value(xapian_file_name, fileName)
    # Index document
    indexer.set_document(document)
    indexer.index_text(content)
    # Store indexed content in database
    database.add_document(document)

# Save changes
database.flush()
