message = """Vishnu\'s World
was a good cartoon in the 1990\'s"""
print(message[0:20].upper())  # Slicing
print(message[21:])
print(message.count('World'))
print(message.find('World'))  # 9th character
new_message = message.replace('World', 'Universe')
print(new_message)

greeting = 'Hello'
name = 'Vishnu'

message = '1. ' + greeting + ' ' + name + ' Welcome'
print(message)
message = '2. {} {} welcome!'.format(greeting, name.upper())  # Cleaner than +
print(message)
message = f'3. {greeting} {name.upper()}, Welcome!'  # Placeholders
print(message)

print(dir(name))  # All attributes and methods which can be accessed by variable
print(help(str.lower))  # Methods accessable to class and their descriptions
