import pytest

from mars_rover_kata.gps import GPS
from mars_rover_kata.rover import Rover
from tests.position_builder import initial_position


@pytest.mark.parametrize('cardinal_point,movement',
                         [('N', (0, 1)), ('S', (0, -1)), ('E', (1, 0)), ('W', (-1, 0))])
def test_rover_moves_forward(cardinal_point, movement):
    rover = given_rover_at(initial_position().facing(cardinal_point))

    rover.instruct(['f'])

    assert rover.locate() == (initial_position()
                              .facing(cardinal_point)
                              .move(movement)
                              .build())


@pytest.mark.parametrize('cardinal_point,movement',
                         [('N', (0, -1)), ('S', (0, 1)), ('E', (-1, 0)), ('W', (1, 0))])
def test_rover_moves_backwards(cardinal_point, movement):
    rover = given_rover_at(initial_position().facing(cardinal_point))

    rover.instruct(['b'])

    assert rover.locate() == (initial_position()
                              .facing(cardinal_point)
                              .move(movement)
                              .build())


@pytest.mark.parametrize('cardinal_point,turn,facing',
                         [('N', 'l', 'W'), ('S', 'l', 'E'), ('E', 'l', 'N'), ('W', 'l', 'S'),
                          ('N', 'r', 'E'), ('S', 'r', 'W'), ('E', 'r', 'S'), ('W', 'r', 'N')])
def test_rover_should_be_able_to_turn(cardinal_point, turn, facing):
    rover = given_rover_at(initial_position().facing(cardinal_point))

    rover.instruct([turn])

    assert rover.locate() == (initial_position()
                              .facing(facing)
                              .build())


def given_rover_at(position):
    return Rover(GPS(position.build()))
