def create_user(name, user_name,  age = 42, **keywords):
  extra = {}
  for kw in keywords:
    extra[kw] = keywords[kw]
  return print({
    "name": name,
    "surname": user_name,
    "age": age,
    "extra": extra
  })

create_user("John", "Doe") 
create_user("Bill", "Gates", age=65)
create_user("Marie", "Curie", age=66, occupation="physicist",
            won_nobel=True)