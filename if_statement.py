
is_male = True
is_tall = False
if is_male and is_tall:
    print("You are male or tall or both")
elif is_male and not(is_tall):
        print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are neither not male not tall or both")
