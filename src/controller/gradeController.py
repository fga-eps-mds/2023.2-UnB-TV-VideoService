from fastapi import APIRouter, HTTPException, Response, status, Depends
from database import get_db
from sqlalchemy.orm import Session

import requests
from bs4 import BeautifulSoup

grade = APIRouter(
  prefix="/grade"
)

@grade.get("/{video_id}")
def read_comment(video_id: int, db: Session = Depends(get_db)):
  re = requests.get('https://unbtv.unb.br/grade')
  html = re.text
  soup = BeautifulSoup(html, 'html.parser')
  table = soup.find("table")

  programacao = {}
  dia_atual = None

  for row in table.find_all("tr"):
      if len(row.find_all("td")) == 1:
          cells = row.find_all("td")[0]
          programacao[cells.text] = []
          dia_atual = cells.text
      else:
          detalhe = {"horario": "", "nome": "", "producao": "", "descricao": ""}
          for index, td in enumerate(row.find_all("td")):
            detalhe[list(detalhe.keys())[index]] = td.text.replace('\xa0', '')

          programacao[dia_atual].append(detalhe)
