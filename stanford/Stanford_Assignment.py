MARS_MULTIPLE = 0.378
earth_weight_str = input("Enter a weight on Earth: ")
earth_weight = float(earth_weight_str)
mars_weight = earth_weight * MARS_MULTIPLE
print("The equivalent weight on Mars: " + str(mars_weight))

