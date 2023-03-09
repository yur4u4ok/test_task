from app.cafe import Cafe

from app.errors import (
    NotWearingMaskError,
    NotVaccinatedError,
    OutdatedVaccineError
)

def go_to_cafe(friends, cafe) -> str:
    
    total = 0

    for i in range(len(friends)):
        try:
            cafe.visit_cafe(friends[i])
        except (NotVaccinatedError, OutdatedVaccineError):
            return 'All friends should be vaccinated'
        except NotWearingMaskError:
            total += 1

    if not total:
        return f'Friends can go to {cafe.name}'
    return f'Friends should buy {total} masks'
