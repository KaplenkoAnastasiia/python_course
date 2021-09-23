def create_user(name:str, user_name:str,  age:int = 42, **extra):
  return {
    "name": name,
    "surname": user_name,
    "age": age,
    "extra": extra
  }

print(create_user("John", "Doe")) 
print(create_user("Bill", "Gates", age=65))
print(create_user("Marie", "Curie", age=66, occupation="physicist",
            won_nobel=True))