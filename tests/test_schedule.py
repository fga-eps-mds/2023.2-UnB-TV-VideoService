import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.constants import errorMessages

client = TestClient(app)

class TestSchedule:
  def test_schedule_get_schedule_day(self):
    response = client.get("/api/schedule/")
    data = response.json()
    assert response.status_code == 200
    assert len(list(data.keys())) == 7
    assert all([a == b for a, b in zip(list(data.keys()), ['SEGUNDA', 'TERCA', 'QUARTA', 'QUINTA', 'SEXTA', 'SABADO', 'DOMINGO'])])
  
  def test_schedule_get_schedule_specific_day_invalid(self):
    params = { 'day': 'INVALID' }
    response = client.get("/api/schedule/", params=params)
    data = response.json()
    assert response.status_code == 400
    assert data['detail'] == errorMessages.INVALID_SCHEDULE_DAY

  def test_schedule_get_schedule_specific_day(self):
    params = { 'day': 'segunda' }
    response = client.get("/api/schedule/", params=params)
    data = response.json()
    assert response.status_code == 200
    assert len(data) > 0    