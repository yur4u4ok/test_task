from app.errors import NotVaccinatedError, \
                        OutdatedVaccineError, \
                        NotWearingMaskError
import datetime


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, vstr: dict) -> str:
        if "vaccine" not in vstr.keys() or vstr["vaccine"] == None:
            raise NotVaccinatedError("not vaccinated")
        elif vstr["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("outdated")
        elif not vstr["wearing_a_mask"]:
            raise NotWearingMaskError("not wearing mask")
        else:
            return "Welcome to " + self.name
