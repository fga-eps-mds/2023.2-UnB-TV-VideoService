from enum import Enum

class ScheduleDaysEnum(Enum):
  SEGUNDA = "SEGUNDA"
  TERCA = "TERCA"
  QUARTA = "QUARTA"
  QUINTA = "QUINTA"
  SEXTA = "SEXTA"
  SABADO = "SABADO"
  DOMINGO = "DOMINGO"

  @classmethod
  def has_value(cls, value):
    return value in cls._value2member_map_