#!/usr/bin/env python
# coding: utf-8

# In[2]:


car_make = {
  "Abarth": "Abarth",
  "Alfa Romeo":  "Alfa Romeo",
  "Aston Martin": "Aston Martin",
  "Audi": "Audi",
  "Bentley": "Bentley",
  "BMW": "BMW",
  "Bugatti": "Bugatti",
  "Cadillac": "Cadillac",
  "Chevrolet": "Chevrolet",
  "Chevy": "Chevy",
  "Chrysler": "Chrysler",
  "Citroën": "Citroën",
  "Dacia": "Dacia",
  "Daewoo": "Daewoo",
  "Daihatsu": "Daihatsu",
  "Dodge": "Dodge",
  "Ferrari": "Ferrari",
  "Fiat": "Fiat",
  "Fisker": "Fisker",
  "Ford": "Ford",
  "Honda": "Honda",
  "Hummer": "Hummer",
  "Hyundai": "Hyundai",
  "Infiniti": "Infiniti",
  "Jaguar": "Jaguar",
  "Jeep": "Jeep",
  "Kia": "Kia",
  "Lamborghini": "Lamborghini",
  "Lancia":  "Lancia",
  "Land Rover": "Land Rover",
  "Lexus":"Lexus",
  "Lotus":"Lotus",
  "Maserati": "Maserati",
  "Maybach": "Maybach",
  "Mazda": "Mazda",
  "McLaren": "McLaren",
  "Mercedes-Benz": "Mercedes-Benz",
  "Mini": "Mini",
  "Mitsubishi": "Mitsubishi",
  "Morgan": "Morgan",
  "Nissan": "Nissan",
  "Peugeot": "Peugeot",
  "Porsche": "Porsche",
  "Renault": "Renault",
  "Rolls-Royce": "Rolls-Royce",
  "Rover": "Rover",
  "Saab": "Saab",
  "Seat": "Seat",
  "Skoda": "Skoda",
  "Smart": "Smart",
  "Subaru":  "Subaru",
  "Suzuki": "Suzuki",
  "Tesla": "Tesla",
  "Toyota": "Toyota",
  "Volkswagen": "Volkswagen",
  "Volvo":  "Volvo"
    
}

def search(values, searchFor):
    for k in values:
        for v in values[k]:
            if searchFor in v:
                return k
    return None

#Checking if string exists in dictionary value
print (search(car_make, 'Chevy')) #prints make

x = car.get("model")



# In[ ]:




