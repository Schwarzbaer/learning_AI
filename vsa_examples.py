from vsa import *


T = new_vec()
H = new_vec()
E = new_vec()
THE = bundle(T, H, E)

print(f"T is E  : {similarity(T, E): 1.3f}")
print(f"E is H  : {similarity(E, H): 1.3f}")
print(f"T is H  : {similarity(T, H): 1.3f}")
print(f"T in THE: {similarity(T, THE): 1.3f}")
print(f"H in THE: {similarity(H, THE): 1.3f}")
print(f"E in THE: {similarity(E, THE): 1.3f}")


name = new_vec()
currency = new_vec()

usa = new_vec()
us_dollar = new_vec()
mexico = new_vec()
peso = new_vec()

country_usa = bundle(bind(name, usa), bind(currency, us_dollar))
country_mexico = bundle(bind(name, mexico), bind(currency, peso))
analogous_countries = bind(country_usa, country_mexico)

# What is the Dollar of Mexico?
the_dollar_of_mexico = bind(us_dollar, analogous_countries)
print("What is the dollar of Mexico? bind(us_dollar, analogous_countries)")
print(f"Country name: {similarity(the_dollar_of_mexico, name)}")
print(f"Currency    : {similarity(the_dollar_of_mexico, currency)}")
print(f"USA         : {similarity(the_dollar_of_mexico, usa)}")
print(f"US Dollar   : {similarity(the_dollar_of_mexico, us_dollar)}")
print(f"Mexico      : {similarity(the_dollar_of_mexico, mexico)}")
print(f"Peso        : {similarity(the_dollar_of_mexico, peso)}")
# The Peso is the what of Mexico?
peso_is_a_what = bind(peso, country_mexico)
print("What kind of thing is Mexico's Peso? bind(peso, country_mexico)")
print(f"Country name: {similarity(peso_is_a_what, name)}")
print(f"Currency    : {similarity(peso_is_a_what, currency)}")
print(f"USA         : {similarity(peso_is_a_what, usa)}")
print(f"US Dollar   : {similarity(peso_is_a_what, us_dollar)}")
print(f"Mexico      : {similarity(peso_is_a_what, mexico)}")
print(f"Peso        : {similarity(peso_is_a_what, peso)}")
