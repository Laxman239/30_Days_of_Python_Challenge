from pydantic import BaseModel, EmailStr, field_validator

class user_profile(BaseModel):
    name: str
    email: EmailStr
    age: int

    @field_validator('age', mode = 'before')
    @classmethod
    def validate_age(cls, value):
        if not (18 <= value <= 100):
            raise ValueError (f"Age must be in range of (18 - 100): {value}")
        return value
    
user_profile = user_profile(name = 'Laxman',
                            email = 'laxman123@gmail.com',
                            age = 23)

print(f'Name: {user_profile.name}')
print(f'Email: {user_profile.email}')
print(f'age: {user_profile.age}')

user_profile = user_profile(name = 'Laxman',
                            email = 'laxmangmail.com',
                            age = 123)

print(f'Name: {user_profile.name}')
print(f'Email: {user_profile.email}')
print(f'age: {user_profile.age}')
