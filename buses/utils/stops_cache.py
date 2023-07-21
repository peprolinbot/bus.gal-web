from django.conf import settings

from ..templatetags.buses_extras import form_stop_string

from whoosh.fields import Schema, STORED, NUMERIC, TEXT
from whoosh.index import create_in, open_dir
from whoosh.qparser import QueryParser

import os.path

from busGal_api.transport.stops import get_all_stops


class StopsCache():
    schema = Schema(id=STORED, group_type=NUMERIC(stored=True, sortable=True), name=TEXT(
        stored=True))  # group_type is NUMERIC instead of SORTED because it needs to be sortable

    def __init__(self, cache_dir=settings.STOPS_CACHE_DIR):
        self.cache_dir = cache_dir

        if not os.path.exists(self.cache_dir):
            os.mkdir(self.cache_dir)
            self.update_index()
        else:
            self.ix = open_dir(self.cache_dir)

    def update_index(self):
        self.ix = create_in(self.cache_dir, self.schema)

        stops = get_all_stops()

        writer = self.ix.writer()
        for stop in stops:
            writer.add_document(id=form_stop_string(
                stop), group_type=stop.group_type, name=stop.name)
        writer.commit()

    def autocomplete_search(self, text):
        with self.ix.searcher() as searcher:
            name_query = QueryParser("name", stops_cache.ix.schema).parse(text)
            results = searcher.search(name_query, sortedby="group_type")

            group_type_icons = ["🏢", "🎖️", "📍", "📌"]  # Imagine it's one-indexed
            return [{"id": r["id"], "text": f"{group_type_icons[r['group_type']-1]} {r['name']}"}
                    for r in results]


stops_cache = StopsCache()
