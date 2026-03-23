dic = {"Alex1": {"phone": "321-654-9870", "email": "alex1@example.com", "address": "123 King St"}, 
       "Alex2": {"phone": "987-654-3210", "email": "alex2@example.com", "address": "321 Queen Rd"}}

conteo = len(dic)
if conteo >= 1:
    for i in dic:
        datos = dic[i]
        print(f"Name: {i}")
        print(f"Phone: {datos['phone']}")
        print(f"Email: {datos['email']}")
        print(f"Address: {datos['address']}")


