from lib.counter import Counter

def test_counter_total():
    counter = Counter()
    counter.add(10)
    result = counter.report()
    assert result == "Counted to 10 so far."

    counter.add(17)
    result = counter.report()
    assert result == "Counted to 27 so far."