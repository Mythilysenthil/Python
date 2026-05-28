class Error(Exception):
    "Base class for other exception"
pass

class ValueTooSmallError(Error):
    "Raised when value is too small"
pass

class ValueTooLargeError(Error):
    "Raised when value is too large"
pass

n = 10
while True:
    try:
        num = int(input("Enter the num: "))
        if n>num:
            raise ValueTooSmallError
        elif n<num:
            raise ValueTooLargeError
        break
    except  ValueTooLargeError:
        print("This is value is too small,Try again!")
    except  ValueTooLargeError:
        print("This is value is too large,Try again!")
    print("Run sucessfully")     