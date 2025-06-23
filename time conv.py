def to_seconds(hours,minutes,seconds):
    return hours*60*60 + minutes*60 + seconds

print("WELCOME TO THIS TIME CONVERTER ")

content = "y"
while (content.lower ()== "y"):
    hours = int(input("Enter hours: "))
    minutes = int(input("Enter minutes: "))
    seconds = int(input("Enter seconds: "))

    print("THAT'S {} seconds".format(to_seconds(hours,minutes,seconds)))
    print()
    content = input("Do you want to do another conversion? [y to continue]")

print("good bye")