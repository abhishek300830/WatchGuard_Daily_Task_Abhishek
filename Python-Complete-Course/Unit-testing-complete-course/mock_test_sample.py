from unittest import mock
from mock_sample import guess_number


@mock.patch("mock_sample.roll_dice")
def test_guess_number(mock_roll_dice):
    mock_roll_dice.return_value = 3
    assert guess_number(3) == "YOU WON"
    mock_roll_dice.assert_called()


