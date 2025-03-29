rlist = range(0, 160, 10)

B0 = []
for i, j in zip(rlist, ttD_range):
    b = np.round(HField(i, j), decimals=6)
    B0.append(b)

print("The average field :")
for i in B0:
    print(i)

def calculate_harmonic(r_1, theta):
    a1 = (1 / 180) * np.sum([HField(r_1, i) * np.sin(1 * i * np.pi / 180) for i in theta])
    b1 = (1 / 180) * np.sum([HField(r_1, i) * np.cos(1 * i * np.pi / 180) for i in theta])

    a2 = (1 / 180) * np.sum([HField(r_1, i) * np.sin(2 * i * np.pi / 180) for i in theta])
    b2 = (1 / 180) * np.sum([HField(r_1, i) * np.cos(2 * i * np.pi / 180) for i in theta])

    if b2 != 0.0:
        phase2 = np.arctan2(a2, b2)
        if a2 == 0 and b2 > 0:
            phase2 = 0
        if a2 == 0 and b2 < 0:
            phase2 = np.pi
        if b2 < 0 and a2 > 0:
            phase2 = np.pi + phase2
        if b2 < 0 and a2 < 0:
            phase2 = np.pi + phase2
        if b2 > 0 and a2 < 0:
            phase2 = 2 * np.pi + phase2


    else:
        if a2 > 0:
            phase2 = 0
        elif a2 < 0:
            phase2 = 3 * (np.pi / 2)
        else:
            phase2 = 0  # a2 and b2 are both zero

    if b1 != 0:
        phase1 = np.arctan2(a1, b1)
        if a1 == 0 and b1 > 0:
            phase1 = 0
        if a1 == 0 and b1 < 0:
            phase1 = np.pi
        if b1 < 0 and a1 > 0:
            phase1 = np.pi + phase1
        if b1 < 0 and a1 < 0:
            phase1 = np.pi + phase1
        if b1 > 0 and a1 < 0:
            phase1 = 2 * np.pi + phase1

    if b1 == 0:
        if a1 > 0:
            phase1 = (np.pi/2)
        if a1 < 0:
            phase1 = 3*(np.pi/2)
        if b1 == 0 and a1 == 0:
            phase1 = 0

    # Convert to degrees
    phase1_deg = np.round(np.rad2deg(phase1))
    phase2_deg = np.round(np.rad2deg(phase2))

    # Calculate magnitudes
    mag1 = np.sqrt(a1 ** 2 + b1 ** 2) * 1000
    mag2 = np.sqrt(a2 ** 2 + b2 ** 2) * 1000

    return b1, a1, b2, a2, mag1, mag2, phase1_deg, phase2_deg

b1, a1, b2, a2, mag1, mag2, phase1_deg, phase2_deg = calculate_harmonic(r_1=50, theta=ttD_range)
#print("Theta for 1st harmonic:", phase1_deg)
#print(phase2_deg)

mag1_list = []
mag2_list = []
for i in range(0, 160, 10):
    b1, a1, b2, a2, mag1, mag2, phase1_deg, phase2_deg = calculate_harmonic(i, ttD_range)
    mag1_list.append(mag1)
    mag2_list.append(mag2)

print("The mag values for 1:")
for j in mag1_list:
    print(j)

print("The mag values for 2:")
for j in mag2_list:
    print(j)
