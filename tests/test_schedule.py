import pytest
from fastapi.testclient import TestClient
from datetime import datetime

from src.main import app
from src.constants import errorMessages
from src.utils import enumeration

client = TestClient(app)

class TestSchedule:
  def test_schedule_get_schedule_day(self):
    response = client.get("/api/schedule/")
    data = response.json()
    week_dt_str = [i.value for i in enumeration.ScheduleDaysEnum][datetime.now().weekday()]
    assert response.status_code == 200
    assert week_dt_str in data.keys()
  
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