import requests
from typing import Optional
from fastapi import APIRouter
from bs4 import BeautifulSoup
from unidecode import unidecode
from starlette.responses import JSONResponse

from utils import enumeration
from constants import errorMessages

schedule = APIRouter(
  prefix="/schedule"
)

@schedule.get("/")
async def get_schedule_day(day: Optional[str] = None):
  if day:
    day = unidecode(day).upper()
    if not enumeration.ScheduleDaysEnum.has_value(day):
      return JSONResponse(status_code=400, content={ "detail": errorMessages.INVALID_SCHEDULE_DAY })

  try:
    re = requests.get('https://unbtv.unb.br/grade')
    html = re.text

    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.find_all("table")

    schedule_data = {}
    current_day = None

    for table in tables:
      for row in table.find_all("tr"):
        if len(row.find_all("td")) == 1:
          cell = row.find_all("td")[0]
          schedule_day = unidecode(cell.text.replace("-FEIRA", ""))
          
          if day:
            if current_day:
              return schedule_data
            if day == schedule_day:
              current_day = schedule_day
              schedule_data[schedule_day] = []
          else:
            current_day = schedule_day
            schedule_data[schedule_day] = []
        else:
          if current_day:
            day_schedule = [item.text for item in row.find_all("td")[:2]]
            if (day_schedule[0].strip() != "" and day_schedule[1].strip() != ""): 
              schedule_data[current_day].append({ "time": day_schedule[0], "activity": day_schedule[1] })
            
    return schedule_data
  except:
    return JSONResponse(status_code=400, content={ "error": errorMessages.ERROR_RETRIEVING_SCHEDULE })
