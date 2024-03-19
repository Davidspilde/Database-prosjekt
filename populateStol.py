rader = [29, 57, 85, 113, 141, 169, 197, 225, 253, 281, 309, 337, 365, 393, 421, 449, 477]
currentRad = 1

for i in rangenot(1, 505):
    if i in rader:
        currentRad += 1
    print(f"INSERT INTO Stol VALUES ({i},{i},{currentRad},NULL,2);")

for i in range(505, 525):
    print(f"INSERT INTO Stol VALUES ({i},{i},19,'Galleri',1);")


# Gamle Scene

# Parkett

RadSizeParkett = [18, 16, 17, 18, 18, 17, 18, 17, 17, 14]

chairCount = 525

for i in range(1, 11):
    for j in range(1, RadSizeParkett[i]):
        print(f"INSERT INTO Stol VALUES ({chairCount},{j},{i},'Parkett',2);")
        chairCount += 1

# Balkong
RadSizeBalkong = [28, 27, 22, 17]
for i in range(1, 5):
    for j in range(1, RadSizeBalkong[i]):
        print(f"INSER INTO Stol VALUES ({chairCount},{j},{i},'Balkon',2);")