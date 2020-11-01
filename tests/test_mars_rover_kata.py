from mars_rover_kata.gps import GPS
from mars_rover_kata.rover import Rover
from tests.position_builder import initial_position


def test_rover_moves_forward():
    rover = given_rover_at(initial_position().facing_north())

    rover.instruct(['f'])

    assert rover.locate() == (initial_position()
                              .facing_north()
                              .move_north(1)
                              .build())


def test_rover_moves_backwards():
    rover = given_rover_at(initial_position().facing_north())

    rover.instruct(['b'])

    assert rover.locate() == (initial_position()
                              .facing_north()
                              .move_south(1)
                              .build())


def given_rover_at(position):
    return Rover(GPS(position.build()))

