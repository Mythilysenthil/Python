try:
    fh = open("text.txt","w")
    try:
        fh.write("This file is opened")
    finally:
        print("going to close the file")
        fh.close
except FileNotFoundError:
    print("file not exist")
else:
    print("I will run when no exception error")
finally:
    print("Run successfully")

# for invalid path to find exception work flow
try:
    fh = open("invalidpath//text.txt","w")
    try:
        fh.write("This file is opened")
    finally:
        print("going to close the file")
        fh.close
except FileNotFoundError:
    print("file not exist")
else:
    print("I will run when no exception error")
finally:
    print("Run successfully")                                            