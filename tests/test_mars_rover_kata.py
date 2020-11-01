import pytest

from mars_rover_kata.planet import Planet
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


def test_rover_can_make_complex_movements():
    rover = given_rover_at(initial_position().facing('N'))

    rover.instruct(['f', 'f', 'l', 'f', 'l', 'f', 'r', 'b',
                    'b', 'b', 'b', 'r', 'b', 'f', 'f', 'f',
                    'b', 'r', 'r', 'f', 'f', 'r', 'l', 'b'])

    assert rover.locate() == (initial_position()
                              .move((3, 1))
                              .facing('S')
                              .build())


# def test_crossing_the_latitude_origin_should_behave_as_an_sphere():
#     rover = given_rover_at(origin_position().facing('S'))
#
#     rover.instruct(['f'])
#
#     assert rover.locate() == (origin_position()
#                               .move((10, 1))
#                               .facing('S')
#                               .build())


def given_rover_at(position):
    return Rover(position.build(), Planet())
