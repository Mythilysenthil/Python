#Fun definition with Arbitrary Arguments

def employee(*names): # *denotes variable length arguments
    for emp in names:
        print("Hello ",emp, ", Have a nice day!" )

#Fun call with arbitrary arguments        
employee("Mythily", "Naveen", "Gopi")        