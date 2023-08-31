from django.conf import settings

from ..templatetags.buses_extras import form_stop_string

from whoosh.analysis import CharsetFilter, StemmingAnalyzer
from whoosh.support.charset import accent_map
from whoosh.fields import Schema, STORED, NUMERIC, TEXT
from whoosh.index import create_in, open_dir
from whoosh.qparser import QueryParser
from whoosh import writing

import os.path

from busGal_api.transport.stops import get_all_stops


class StopsCache():
    name_analyzer = StemmingAnalyzer() | CharsetFilter(accent_map)
    schema = Schema(id=STORED, group_type=NUMERIC(stored=True, sortable=True), name=TEXT(
        stored=True, analyzer=name_analyzer))  # group_type is NUMERIC instead of SORTED because it needs to be sortable

    def __init__(self, cache_dir=settings.STOPS_CACHE_DIR):
        self.cache_dir = cache_dir

        if not os.path.exists(self.cache_dir):
            os.mkdir(self.cache_dir)
            self.ix = create_in(self.cache_dir, self.schema)
            self.update_index()
        else:
            self.ix = open_dir(self.cache_dir)

    def update_index(self):
        stops = get_all_stops()

        with self.ix.writer() as writer:
            for stop in stops:
                writer.add_document(id=form_stop_string(
                    stop), group_type=stop.group_type, name=stop.name)

            # Clears all existing documents, only the ones added in this writer are left
            writer.mergetype = writing.CLEAR

    def autocomplete_search(self, text):
        name_query = QueryParser("name", stops_cache.ix.schema).parse(text)
        with self.ix.searcher() as searcher:
            results = searcher.search(name_query, sortedby="group_type")

            # Search for the corrected query
            corrected = searcher.correct_query(name_query, text)
            if corrected.query != name_query:
                results_corrected = searcher.search(corrected.query, sortedby="group_type")
                results.upgrade_and_extend(results_corrected)

            # Imagine it's one-indexed
            group_type_icons = ["🏢", "🎖️", "📍", "📌"]
            return [{"id": r["id"], "text": f"{group_type_icons[r['group_type']-1]} {r['name']}"}
                    for r in results]


stops_cache = StopsCache()
