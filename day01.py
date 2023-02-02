import pathlib

# can use (/) instead of (\) python can interpret this
path = pathlib.Path("C:/Users/pavel/Documents/dev/py_basic/adc/day01_input.txt")

#  turn the string into a raw string by (r). Python ignore any escape sequences
# path = pathlib.Path(r"C:\Users\pavel\Documents\dev\py_basic\adc\helloinput.txt")

print(path.stem)    # helloinput
print(path.suffix) # .txt
print(path.exists())


suma = 0
stara = 0

with path.open(mode="r", encoding="utf-8") as file:
    for line in file.readlines():
        
        if line == "\n":
            print("- - - - - - - - - -")
            # print(suma)
            if stara > suma:
                print(stara)
                print("Nie zmieniam sumy")
                suma = stara
            else:
                print(suma)
                print("Zmieniam sumę")
                stara = suma
            suma = 0
        else:
            suma = int(line) + suma
    
    
