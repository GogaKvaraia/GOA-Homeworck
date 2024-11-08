#1 რა არის ობიექტი

#ობიექტი Python-ში არის მონაცემთა სტრუქტურა, რომელიც ინახავს მონაცემებს და ფუნქციებს, რომლებიც ამ მონაცემებზე მუშაობენ. ყოველ ობიექტს აქვს მახასიათებლები და მეთოდები





#2 Dictionary Python'ში 

#Dictionary Python-ში არის უნიკალური გასაღებების (keys) და ღირებულებების (values) ნაკრები, რომელიც საშუალებას გვაძლევს სწრაფად მოვიძიოთ და შეცვალოთ მონაცემები


#3

mouse = {
    "brand": "Logitech",
    "type": "Wireless",
    "dpi": 16000,
    "color": "Black",
    "buttons": 7
}


print("Mouse Keys:", mouse.keys())
print("Mouse Values:", mouse.values())
print("Mouse Items:", mouse.items())






computer = {
    "brand": "Apple",
    "processor": "M1",
    "ram": "16GB",
    "storage": "512GB SSD",
    "os": "macOS"
}


print("Computer Keys:", computer.keys())
print("Computer Values:", computer.values())
print("Computer Items:", computer.items())







keyboard = {
    "brand": "Razer",
    "type": "Mechanical",
    "backlight": "RGB",
    "key_switch": "Green",
    "warranty": "2 years"
}



print("Keyboard Keys:", keyboard.keys())
print("Keyboard Values:", keyboard.values())
print("Keyboard Items:", keyboard.items())
