v1 = field(ran_ge, theta)
n1 = field(ran_ge, (theta + 180))
#print(len(v1))
#print(len(n1))

all_field_vals = np.concatenate((n1, v1))
#for i in all_field_vals:
#    print(i)
tolerance = 1

target_field_value = []
for i in range(120, 140, 1):
    f = field(i, theta)
    target_field_value.append(f)

pos_rad_list = []
neg_rad_list = []
mpoint_list = []

for i in target_field_value:
    # Positive radius
    positive_matching_indices = np.where(np.abs(v1 - i) <= tolerance)[0]
    
    if len(positive_matching_indices) > 0:
        # Sort indices by absolute difference (ascending order of closeness)
        sorted_positive_indices = positive_matching_indices[np.argsort(np.abs(v1[positive_matching_indices] - i))]
        
        # Choose two closest radii (adjust based on your needs)
        positive_matching_radius1 = ran_ge[sorted_positive_indices[0]]
        positive_matching_radius2 = ran_ge[sorted_positive_indices[1]] if len(sorted_positive_indices) > 1 else None
    else:
        positive_matching_radius1 = None
        positive_matching_radius2 = None



    # Negative radius
negative_matching_indices = np.where(np.abs(n1 - i) <= tolerance)[0]

if len(negative_matching_indices) > 0:
    sorted_negative_indices = negative_matching_indices[np.argsort(np.abs(n1[negative_matching_indices] - i))]
    
    # Access positive radii corresponding to negative theta
    negative_matching_radius1 = ran_ge[sorted_negative_indices[0]]
    negative_matching_radius2 = ran_ge[sorted_negative_indices[1]] if len(sorted_negative_indices) > 1 else None
else:
    negative_matching_radius1 = None
    negative_matching_radius2 = None

# Print results (adjust as needed)
print("Target field value:", i)

print("Positive matching radii:")
if positive_matching_radius1 is not None:
    print("  - Radius 1:", positive_matching_radius1)
    print("  - Field value:", field(positive_matching_radius1, theta))
if positive_matching_radius2 is not None:
    print("  - Radius 2:", positive_matching_radius2)
    print("  - Field value:", field(positive_matching_radius2, theta))
else:
    print("  - No matching radii found within tolerance")

print("\nNegative matching radii:")
if negative_matching_radius1 is not None:
    print("  - Radius 1:", negative_matching_radius1)
    print("  - Field value:", field(negative_matching_radius1, theta + 180))
if negative_matching_radius2 is not None:
    print("  - Radius 2:", negative_matching_radius2)
    print("  - Field value:\n", field(negative_matching_radius2, theta + 180))
else:
    print("  - No matching radii found within tolerance")

mpoint = (positive_matching_radius1 - negative_matching_radius1) / 2

print("\nThe midpoint is:", mpoint)

pos_rad_list.append(positive_matching_radius1)
neg_rad_list.append(negative_matching_radius1)
mpoint_list.append(mpoint)

plt.plot(#args: ran_ge, v1)
plt.plot(#args: ran_ge, n1)
#plt.legend()
plt.axhline(i)
plt.xlabel("Radius")
plt.ylabel("Field Value")
plt.title("Comparison of Field Values")
