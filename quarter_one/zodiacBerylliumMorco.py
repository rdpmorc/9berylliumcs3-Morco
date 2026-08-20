# FUNCTIONS AND LISTS :
signList = ['Rat (鼠 / Shǔ)','Ox (牛 / Niú)','Tiger (虎 / Hǔ)',
            'Rabbit (兔 / Tù)','Dragon (龙 / Lóng)','Snake (蛇 / Shé)',
            'Horse (马 / Mǎ)','Goat (羊 / Yáng)','Monkey (猴 / Hóu)',
            'Rooster (鸡 / Jī)','Dog (狗 / Gǒu)','Pig (猪 / Zhū)']

def getYear():
    x = int(input("Enter your birth year: "))
    return x

def getZodiac(x, y):
    year = (x - 1900) % 12
    zodiac = y[year]
    return zodiac

# MAIN PROGRAM :
x = getYear()
if x >= 1900:
    animal = getZodiac(x, signList)
    print("Your Chinese Zodiac Sign is: " + animal)
else:
    print("Invalid Year, it should not be earlier than 1900.")
