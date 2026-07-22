from app.core.security import create_access_token

data = {
    "sub": "bhuvan@example.com"
}

token = create_access_token(data)

print("Generated JWT:")
print(token)