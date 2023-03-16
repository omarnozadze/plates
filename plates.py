def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    
    if s[0].isdigit() or s[1].isdigit():
        return False

    if s.isalnum() == False:
        return False 
       
    if len(s) < 2 or len(s) > 6 :
        return False

    for i in s:
        if s.find("0") == i:
            if s.find("0")<=i:
                return False
    return i                     
main()