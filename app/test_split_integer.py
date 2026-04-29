import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (4, 5)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int,
    number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert (
        sum(result) == value
    ), f"Sum of {result} should be equal to {value}"


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (4, 5)
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int,
    number_of_parts: int
) -> None:
    if value % number_of_parts == 0:
        result = split_integer(value, number_of_parts)
        assert (
            max(result) == min(result)
        ), f"{result} should consist of {number_of_parts} equal parts"


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (4, 5)
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
    value: int,
    number_of_parts: int
) -> None:
    if number_of_parts == 1:
        result = split_integer(value, number_of_parts)
        assert (
            len(result) == 1 and result[0] == value
        ), (f"{result} should consist of "
            f"{number_of_parts} part equal to {value}")


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (4, 5)
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
    value: int,
    number_of_parts: int
) -> None:
    if value % number_of_parts != 0:
        result = split_integer(value, number_of_parts)
        assert (
            sorted(result) == result
        ), f"{result} should be sorted"


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (4, 5)
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
    value: int,
    number_of_parts: int
) -> None:
    if value < number_of_parts :
        result = split_integer(value, number_of_parts)
        assert (
            result.count(0) == number_of_parts - value
        ), f"{result} should be have {number_of_parts - value} added"
