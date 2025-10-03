import sqlite3
import pytest
from api.actors import ActorsHandler
from api.response import ActorsResponse

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
class FakeCursor:
    def __init__(self, rows):
        self._rows = rows

    def execute(self, query):
        return None

    def fetchall(self):
        return self._rows


class FakeConn:
    def __init__(self, rows):
        self._cursor = FakeCursor(rows)

    def cursor(self):
        return self._cursor


class DummyHandler:
    def __init__(self):
        self.written = None

    def write(self, obj):
        self.written = obj


def test_actors_handler_get_monkeypatched(monkeypatch):
    rows = [(1, 'Actor One', 1970), (2, 'Actor Two', 1980)]

    def fake_connect(db_path):
        assert db_path == 'movies.db'
        return FakeConn(rows)

    monkeypatch.setattr(sqlite3, 'connect', fake_connect)

    handler = DummyHandler()
    ActorsHandler.get(handler)

    assert handler.written is not None
    assert 'objects' in handler.written
    assert isinstance(handler.written['objects'], list)
    assert len(handler.written['objects']) == 2
    
    actor1 = handler.written['objects'][0]
    assert isinstance(actor1, dict)
    assert actor1['id'] == 1
    assert actor1['name'] == 'Actor One'
    assert actor1['birth_year'] == 1970

    actor2 = handler.written['objects'][1]
    assert isinstance(actor2, dict)
    assert actor2['id'] == 2
    assert actor2['name'] == 'Actor Two'
    assert actor2['birth_year'] == 1980

