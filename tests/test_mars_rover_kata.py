from mars_rover_kata.gps import GPS
from mars_rover_kata.rover import Rover


def test_rover_moves_forward():
    rover = given_rover_at(INITIAL_POSITION)
    rover.instruct(['f'])
    assert (0, 1, 'N') == rover.locate()


def given_rover_at(position):
    return Rover(GPS(position))


INITIAL_POSITION = (0, 0, 'N')
