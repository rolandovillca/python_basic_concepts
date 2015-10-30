# Function that calculates fahrenheit formula
def fahrenheit(temperature):
    return ((float(9)/5) * temperature + 32)

# Function that calculates celcius formula
def celcius(temperature):
    return (float(5)/9) * (temperature - 32)

# The array with values as random temperatures
temperature = (36.5, 37, 37.5,39)

# Apply map function using fahrenheit function
F = map(fahrenheit, temperature)

# Apply map function using fahrenheit function
C = map(celcius, F)

# Display results
print F
print C
