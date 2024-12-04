

class EdUniOutOfRangeException(Exception):  # class OutOfRangeException extends Exception
    pass

out_of_range_exception = EdUniOutOfRangeException("Something went wrong")

print(out_of_range_exception)

try:
    raise EdUniOutOfRangeException("That number is not in the range of 1 to 10")
except EdUniOutOfRangeException:
    print("Make sure you are within the limits of the game.")
except:
    print("Something unexpected went wrong.")