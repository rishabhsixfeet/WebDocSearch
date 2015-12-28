import logging

from pylons import request, response, session, tmpl_context as c, url,config
from pylons.controllers.util import abort, redirect,forward
from paste.fileapp import FileApp

from demo.lib.base import BaseController, render
import xapian
import os
# Import custom modules


class SearchController(BaseController):

    def index(self):
        return render('/search/index.mako')

    def query(self):
        # Load queryString
        queryString = request.GET.get('q', '').strip()
        # If queryString exists,
        if queryString:
            # Connect to database
            try:
                database = xapian.Database(config['path_indices'])
            except xapian.DatabaseOpeningError:
                return 'Cannot open database at ' + config['path_indices']
            # Parse query string
            queryParser = xapian.QueryParser()
            queryParser.set_stemmer(xapian.Stem('english'))
            queryParser.set_database(database)
            queryParser.set_stemming_strategy(xapian.QueryParser.STEM_SOME)
            query = queryParser.parse_query(queryString)
            # Set offset and limit for pagination
            offset, limit = 0, database.get_doccount()
            # Start query session
            enquire = xapian.Enquire(database)
            enquire.set_query(query)
            # Display matches
            c.matches = enquire.get_mset(offset, limit)
            c.queryString = queryString
            # Render
            return render('/search/payload.mako')
    def download(self, fileName):
        # Clean fileName for security
        fileName = os.path.basename(fileName)
        # Build filePath
        filePath = os.path.join(config['path_documents'], fileName)
        # If the filePath is a file,
        if os.path.exists(filePath) and os.path.isfile(filePath):
            return forward(FileApp(filePath))
