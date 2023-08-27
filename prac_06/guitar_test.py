from guitar import Guitar

def test_guitar_methods():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 1200.00)

    # Test get_age() method
    assert gibson.get_age() == 101
    assert another_guitar.get_age() == 10

    # Test is_vintage() method
    assert gibson.is_vintage() == True
    assert another_guitar.is_vintage() == False

    print("Tests passed.")

if __name__ == "__main__":
    test_guitar_methods()