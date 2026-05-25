# Keyword Arguments
def message(name, msg):
    print("Hello ", name, ",", msg)
message(name="Mythily", msg="Have a nice day!")   # Normal Keyword Arguments
message(msg="Have a nice day!", name="Mythily")   # position order changed
message( msg="Have a nice day!", name="Mythily")  # 1 positional and 1 keyword argument