import matplotlib.pyplot as plt
# Definizione dei dati come dizionario di liste
import pandas as pd



data = {
    "Name": [
        "Plague of Athens", "Antonine Plague", "Plague of Cyprian", "Plague of Justinian", "Plague of Amida",
        "Roman Plague of 590", "Plague of Sheroe", "British Isles", "Plague of Basra", "Japanese smallpox",
        "Black Death", "Sweating sickness", "Mexico Smallpox", "Cocoliztli Epidemic", "1563 London plague",
        "Cocoliztli epidemic", "1592-93 London plague", "Plague of Malta", "Plague in Spain", "New England",
        "Italian plague", "G. Plague of Sevilla", "Plague of Naples", "Netherlands", "G. Plague of London",
        "Plague in France", "Malta plague epidemic", "G. Plague of Vienna", "G. N. War plague",
        "Smallpox in Iceland", "G. Plague of Marseille", "G. Plague of 1738", "Russian plague", "Persian Plague",
        "Ottoman Plague", "Caragea's plague", "Malta plague epidemic", "1st cholera pand.", "2nd cholera pand.",
        "Canada Typhus", "Third cholerapandemic", "Copenhagen Cholera", "Third plague pandemic",
        "B. Columbiam Smallpox", "Fourth cholera pandemic", "Fiji Measles outbreak", "Yellow Fever",
        "Fifth cholera pandemic", "Smallpox in Montreal", "Russian flu", "Sixth cholera pandemic", "China plague",
        "Encephalitis lethargica", "American polio epidemic", "Spanish flu", "HIV/AIDS pandemic",
        "Poliomyelitis in USA", "Asian flu", "Hong Kong flu", "London flu", "Smallpox epidemic of India",
        "Zimbabwe cholera", "Swine Flu", "Haiti cholera outbreak", "Measles in D.R. Congo",
        "Ebola in West Africa", "Indian swine flu outbreak", "Yemen cholera outbreak", "Kivu Ebola",
        "COVID-19 Pandemic", "Measles in D.R. Congo", "Dengue fever"
    ],
    "Start": [
        -429, 165, 250, 541, 562, 590, 627, 664, 688, 735, 1331, 1485, 1520, 1545, 1562, 1576, 1592, 1592, 1596, 1616,
        1629, 1647, 1656, 1663, 1665, 1668, 1675, 1679, 1700, 1707, 1720, 1738, 1770, 1772, 1812, 1813, 1813, 1816, 1829,
        1847, 1852, 1853, 1855, 1862, 1863, 1875, 1880, 1881, 1885, 1889, 1899, 1910, 1915, 1916, 1918, 1920, 1920, 1946,
        1957, 1968, 1972, 1974, 2008, 2009, 2010, 2011, 2013,  2016, 2018, 2019, 2019, 2019
    ],
    "End": [
        -426, 180, 266, 542, 562, 590, 628, 689, 689, 737, 1353, 1551, 1520, 1548, 1564, 1580, 1593, 1593, 1602, 1620,
        1631, 1652, 1658, 1664, 1666, 1668, 1676, 1679, 1721, 1709, 1722, 1738, 1772, 1772, 1819, 1813, 1814, 1826, 1851,
        1848, 1860, 1853, 1960, 1863, 1875, 1875, 1900, 1896,1923, 1885, 1890, 1969, 1973,1974, 1912, 2020, 2020, 2020, 1946, 1958,
        1969, 1973, 1974, 2009, 2009, 2020, 1018, 2016, 2015, 2020, 2020, 2020
    ],
    "Lower": [
        75, 5000, 1000, 25000000, 30, 10, 100, 150, 200, 2000, 75000, 10, 5000, 5000, 20, 2000, 20, 3, 600, 7, 280, 150,
        1250, 24, 100, 40, 11, 76, 176, 18, 100, 50, 50, 2000, 300, 60, 5, 100, 100, 20, 1000, 5, 15000, 3, 600, 40, 100,
        800, 40, 9, 3, 1000, 2, 40, 1500, 6, 17000, 25000, 2, 2000, 1000, 1, 15, 4, 152, 10, 5, 11, 2, 117, 5, 2
    ],
    "Avg(k)": [
        88, 7500, 1000, 62500000, 30, 20, 100, 175, 200, 2000, 137500, 10, 6500, 10000, 20, 2250, 20, 3, 650, 7, 280, 150,
        1250, 24, 100, 40, 11, 76, 192, 18, 100, 50, 50, 2000, 300, 60, 5, 100, 100, 20, 1000, 5, 15000, 3, 600, 40, 100,
        800, 40, 9, 3, 1000, 2, 40, 1500, 6, 17000, 25000, 2, 2000, 1000, 1, 15, 4, 152, 10, 5, 11, 2, 117, 5, 2
    ],
    "Upper": [
        100, 10000, 1000, 100000000, 30, 30, 100, 200, 200, 2000, 200000, 10, 8000, 15000, 20, 2500, 20, 3, 700, 7, 280, 150,
        1250, 24, 100, 40, 11, 76, 208, 18, 100, 50, 50, 2000, 300, 60, 5, 100, 100, 20, 1000, 5, 22000, 3, 600, 40, 100,
        800, 42, 9, 3, 1000, 3, 40, 1500, 7, 100000, 35000, 2, 2000, 1000, 2, 29, 5, 575, 7, 5, 12, 2, 150, 5, 2
    ],
    "Resc Avg": [
        13376, 283355, 37227, 2246000, 1078, 719, 3594, 6290, 7189, 67690, 2678283, 166, 107684, 165668, 277, 31045, 275, 41,
        8969, 97, 3863, 2070, 15840, 306, 1267, 507, 143, 963, 2427, 228, 1267, 470, 470, 15444, 2317, 463, 35, 772, 772,
        154, 6053, 29, 111986, 18, 3632, 242, 757, 42, 14, 4620, 3696, 185, 6930, 30, 193789, 61768, 5, 5186, 2102, 2, 29,
        6788, 409, 11, 5, 7176, 2, 12, 2, 50, 5, 2
    ],
    "Avg Pop": [
        50, 202, 205, 213, 213, 213, 213, 213, 213, 226, 392, 461, 461, 461, 554, 554, 554, 554, 554, 554, 554, 554, 603,
        603, 603, 603, 603, 603, 603, 603, 603, 814, 814, 814, 990, 990, 990, 990, 900, 900, 900, 1263, 1263, 1263,
        1263, 1263, 1263, 1263, 1654, 1654, 1654, 1654, 1654, 1654, 1654,
        2307, 3712, 2948, 2948, 3637, 3866, 4016, 6788, 6788, 7253, 7176, 7253, 7643, 7643,7643,7643,7643
    ]
}
'''
# Stampare la lunghezza della lista 'Name'
print("Lunghezza della lista 'Name':", len(data["Name"]))

# Verificare la lunghezza delle altre liste rispetto alla lista 'Name'
for key, value in data.items():
    if key != "Name":
        print(f"Lunghezza della lista '{key}':", len(value))

'''
# Creazione del DataFrame
df = pd.DataFrame(data)

# Creiamo il grafico a dispersione
plt.figure(figsize=(12, 8))
plt.scatter(df['Avg Pop'], df['Lower'], color='blue', label='Stima Inferiore (Lower)')
plt.scatter(df['Avg Pop'], df['Avg(k)'], color='green', label='Stima Media (Avg(k))')
plt.scatter(df['Avg Pop'], df['Upper'], color='red', label='Stima Superiore (Upper)')
plt.xlabel('Popolazione Media Coinvolta (in milioni)')
plt.ylabel('Stime del Numero di Vittime (in migliaia)')
plt.title('Confronto delle Stime del Numero di Vittime per Epidemia')
plt.legend()
plt.grid(True)

# Mostra il grafico
plt.show()
