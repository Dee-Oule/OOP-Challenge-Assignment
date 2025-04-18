from pet import Pet

# Create a pet instance
my_pet = Pet("Buddy")

# Show initial status
my_pet.get_status()

# Interact with pet
my_pet.eat()
my_pet.sleep()
my_pet.play()

# Show updated status
my_pet.get_status()

# Bonus: train and show tricks
my_pet.train("Sit")
my_pet.train("Roll over")
my_pet.show_tricks()
