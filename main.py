def afunction():
    # Test for ci
    return True


if __name__ == "__main__":
    test = afunction()
    if test:
        print("Test passed")
    else:
        print("Test failed")
