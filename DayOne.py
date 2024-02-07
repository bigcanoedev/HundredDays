"""
Day One of the Angela Yu 100 Days of Python Course
"""
#1. Create a greeting for your program.
print("Hello welcome to the band name generator")
#2. Ask the user for the city that they grew up in.
band_name = input("What city did you grow up in?")
#3. Ask the user for the name of a pet.
pet_name = input("what is the name of your pet?")
#4. Combine the name of their city and pet and show them their band name.
band_name = band_name + pet_name
#5. Make sure the input cursor shows on a new line:
print("Your new band name is: \n" + band_name)
# Solution: https://replit.com/@appbrewery/band-name-generator-end