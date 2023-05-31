
import math

units = ["B", "KB", "MB", "BG", "TB"]

units_to_use = {
    "B": 1, 
    "KB": 1024, 
    "MB": 1024 **2, 
    "BG": 1024 **3, 
    "TB":1024 **4,
}


def func1 ():
    1024


size = float(input("Enter the size: "))
unit_from = input("Enter the unit to convert from (B, KB, MB, BG, TB): ")
unit_to = input("Enter the unit to convert to (B, KB, MB, BG, TB): ")

if unit_from not in units or unit_to not in units:
    raise ValueError("Invalid units")

if unit_from == "B" and unit_to == "B":
    print(size)
elif unit_from == "KB" and unit_to == "KB":
    print(size)
elif unit_from == "MB" and unit_to == "MB":
    print(size)
elif unit_from == "BG" and unit_to == "BG":
    print(size)
elif unit_from == "TB" and unit_to == "TB":
    print(size)
elif unit_from == "B" and unit_to == "KB":
    KB = size / func1
    print(f"Converted size: {KB} KB")
elif unit_from == "KB" and unit_to == "B":
    B = size * 1024
    print(f"Converted size: {B} B")
elif unit_from == "B" and unit_to == "MB":
    MB = size / 1024 * 1024
    print(f"Converted size: {MB} MB")
elif unit_from == "MB" and unit_to == "B":
    B = size * 1024 * 1024
    print(f"Converted size: {B} B")
elif unit_from == "B" and unit_to == "BG":
    BG = size / 1024 * 1024 * 1024
    print(f"Converted size: {BG} BG")
elif unit_from == "BG" and unit_to == "B":
    B = size * 1024 * 1024 * 1024
    print(f"Converted size: {B} B")
elif unit_from == "B" and unit_to == "TB":
    TB = size / 1024 * 1024 * 1024 * 1024
    print(f"Converted size: {TB} TB")
elif unit_from == "TB" and unit_to == "B":
    B = size * 1024 * 1024 * 1024 * 1024
    print(f"Converted size: {B} B")
elif unit_from == "KB" and unit_to == "MB":
    MB = size / 1024 
    print(f"Converted size: {MB} MB")
elif unit_from == "MB" and unit_to == "KB":
    KB = size * 1024 
    print(f"Converted size: {KB} KB")
elif unit_from == "KB" and unit_to == "BG":
    BG = size / 1024 * 1024
    print(f"Converted size: {BG} BG")
elif unit_from == "BG" and unit_to == "KB":
    KB = size * 1024 * 1024
    print(f"Converted size: {KB} KB")
elif unit_from == "KB" and unit_to == "TB":
    TB = size / 1024 * 1024 * 1024
    print(f"Converted size: {TB} TB")
elif unit_from == "TB" and unit_to == "KB":
    KB = size * 1024 * 1024 * 1024
    print(f"Converted size: {KB} KB")
elif unit_from == "MB" and unit_to == "BG":
    BG = size / 1024 * 1024
    print(f"Converted size: {BG} BG")
elif unit_from == "BG" and unit_to == "MB":
    MB = size * 1024 * 1024
    print(f"Converted size: {MB} MB")
elif unit_from == "MB" and unit_to == "TB":
    TB = size / 1024
    print(f"Converted size: {TB} TB")
elif unit_from == "TB" and unit_to == "MB":
    MB = size * 1024
    print(f"Converted size: {MB} MB")
elif unit_from == "BG" and unit_to == "TB":
    TB = size / 1024 * 1024
    print(f"Converted size: {TB} TB")
elif unit_from == "TB" and unit_to == "BG":
    BG = size * 1024 * 1024
    print(f"Converted size: {BG} BG")
# else:
#     print("Error Input the correct")