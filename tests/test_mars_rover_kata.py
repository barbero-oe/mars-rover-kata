import pytest

from mars_rover_kata.gps import GPS
from mars_rover_kata.rover import Rover
from tests.position_builder import initial_position


@pytest.mark.parametrize("cardinal_point,movement",
                         [('N', (1, 0))])
def test_rover_moves_forward(cardinal_point, movement):
    rover = given_rover_at(initial_position().facing(cardinal_point))

    rover.instruct(['f'])

    assert rover.locate() == (initial_position()
                              .facing(cardinal_point)
                              .move(movement)
                              .build())


@pytest.mark.parametrize("cardinal_point,movement",
                         [('N', (-1, 0))])
def test_rover_moves_backwards(cardinal_point, movement):
    rover = given_rover_at(initial_position().facing(cardinal_point))

    rover.instruct(['b'])

    assert rover.locate() == (initial_position()
                              .facing(cardinal_point)
                              .move(movement)
                              .build())


def given_rover_at(position):
    return Rover(GPS(position.build()))
