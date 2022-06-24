import sports
from pynotifier import Notification
match_info = sports.get_sport("CRICKET")
print(match_info)

Notification(
    title="IPL Live score Updates",
    description=str(match_info),
    duration=60,
).send()
