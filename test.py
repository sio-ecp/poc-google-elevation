import poc_GoogleElevation as gElev


# Constants used for test
# Exact location of the "Champs de Mars". Expected elevation i~s 35m.
LAT = 48.856416
LONG = 2.297273


def test():
    elevation = gElev.findElevation(LAT,LONG)
    assert(34 < elevation < 36)
