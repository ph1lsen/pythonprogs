# Guest List Python Crash Course Chapter 3, Exercise 3-4 to 3-7

dinner_guests = ["Bill Gates", "John Lennon", "Terry Pratchett"]

print(f"{dinner_guests[0].title()}, du bist eingeladen zu meiner Party!")
print(f"{dinner_guests[1].title()}, du bist eingeladen zu meiner Party!")
print(f"{dinner_guests[2].title()}, du bist eingeladen zu meiner Party!")

declined = dinner_guests.pop(0)

print(f"{declined.title()} schafft es leider nicht zur party.")

print(f"{dinner_guests[0].title()}, {declined.title()} schafft es leider nicht zur Party, bitte bring einen Gast mit.")
print(f"{dinner_guests[1].title()}, {declined.title()} schafft es leider nicht zur Party, bitte bring einen Gast mit.")

dinner_guests.insert(0, 'Patrick Rothfuss')
dinner_guests.insert(1, 'J.R.R. Tolkien')
dinner_guests.append("Stephen King")

print(f"{dinner_guests}")