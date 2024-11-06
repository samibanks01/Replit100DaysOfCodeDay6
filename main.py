print("SECURE LOGIN")
username = input("Username > ")
password = input("Password> ")

if username == "Samuel" and password == "Verybadman":
 print("""
  Welcome User Sam!
  It's a Wonderful Day and great to be here!
  Tighten your seat belt and get ready for the day!
 """)
elif username == "suzanne" and password == "Sleeknerdychick":
  print("""
    Welcome User Suzy!
    It's a Wonderful Day and great to be here!
    Grab a cup of coffee and get ready for the day!
   """)
elif username == "mobydick" and password == "Sneakydick":
  print("""
    Welcome User Moby!
    It's a Wonderful Day and great to be here!
    Hop in and lets chase the chickens!
   """)
else:
 print("Sorry, Not today!")
