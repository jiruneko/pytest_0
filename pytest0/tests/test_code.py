from unittest import result
from src import code

def get_json_data_mock(id):
  return {'name': 'サプー'}

def test_get_user_names(monkeypatch):
  monkeypatch.setattr(
    code, 'get_json_data', get_json_data_mock
  )
  result = code.get_user_names[()]
