import datetime
from app.cafe import Cafe
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list, cafe : Cafe):
    count_mask = 0
   
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotVaccinatedError:
            return "All friends should be vaccinated"
        except OutdatedVaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            count_mask+=1

    if count_mask > 0:
        masks_to_buy = sum(1 for friend in friends
                           if not friend.get("wearing_a_mask"))
        return f"Friends should buy {masks_to_buy} masks"
    
    return f"Friends can go to {cafe.name}"
    
        
        


# Example usage
friends =  [
                {
                    "name": "Alisa",
                    "vaccine": {
                        "name": "Pfizer",
                        "expiration_date": datetime.date.today()
                        + datetime.timedelta(days=5),
                    },
                    "wearing_a_mask": False,
                },
                {
                    "name": "Bob",
                    "vaccine": {
                        "name": "Moderna",
                        "expiration_date": datetime.date.today()
                        + datetime.timedelta(days=15),
                    },
                    "wearing_a_mask": False,
                },
                {
                    "name": "Harry",
                    "vaccine": {
                        "name": "Moderna",
                        "expiration_date": datetime.date.today()
                        - datetime.timedelta(days=10),
                    },
                    "wearing_a_mask": False,
                },
            ]
print(go_to_cafe(friends, Cafe("KFC")))  # "Friends can go to KFC"
