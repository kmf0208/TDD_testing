from lib.gratitudes import Gratitudes


def test_add_single_item():
    gratitude = Gratitudes()
    gratitude.add("family")
    assert gratitude.gratitudes == ["family"]


def test_add_multiple_items():
    gratitude = Gratitudes()
    gratitude.add("family")
    gratitude.add("friends")
    gratitude.add("health")
    assert gratitude.gratitudes == ["family", "friends", "health"]

def test_format_multiple_items():
    gratitude = Gratitudes()
    gratitude.add("sunshine")
    gratitude.add("food")
    gratitude.add("love")
    result = gratitude.format()
    assert result == "Be grateful for: sunshine, food, love"