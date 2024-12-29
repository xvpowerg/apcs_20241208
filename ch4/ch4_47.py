cars = ['honda','BMW','Toyota','audi']
print(cars)
cars.sort()
print(cars)
cars = ['honda','BMW','Toyota','audi']
cars.sort(key=len)
print(cars)
cars = ['honda','BMW','Toyota','audi']
cars.sort(key=lambda v : v.lower())
print(cars)







