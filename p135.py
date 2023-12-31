import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import csv
import pandas as pd
from sklearn.cluster import KMeans
import plotly.express as px

rows = []

with open("stars.csv",'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

headers = rows[0]
star_data = rows[1:]

df = pd.read_csv("stars.csv")
mass = df["mass"].tolist()
radius= df["radius"].tolist()

mass.pop(0)
radius.pop(0)

mass_si_unit = []

for data in mass:

    si_unit = float(data)*1.989e+30
    mass_si_unit.append(si_unit)

print(_mass_si_unit)

radius_si_unit = []

for data in radius:
    si_unit = float(data)* 6.957e+8
    radius_si_unit.append(si_unit)

print(radius_si_unit)

star_masses = mass_si_unit
star_radiuses = radius_si_unit
star_names = df["star_names"].tolist()
star_names.pop(0)

star_gravities = []

for index,data in enumerate(star_names):
    gravity = (float(star_masses[index])*5.972e+24) / (float(star_radiuses[index])*float(star_radiuses[index])*6371000*6371000) * 6.674e-11
    star_gravities.append(gravity)

print(star_gravities)

mass_list = df["mass"].tolist()
mass_list.pop(0)

radius_list = df["radius"].tolist()
radius_list.pop(0)

mass_radius_column = star_data.iloc[:, 2:4].values

within_cluster_sum_of_squares = []
for k in range(1, 9):
    k_means = KMeans(n_clusters = k, random_state = 42)
    k_means.fit(mass_radius_column)
    within_cluster_sum_of_squares.append(k_means.inertia_)

plt.figure(figsize = (10, 5))
sns.lineplot(x = range(1, 9), y = within_cluster_sum_of_squares, markers = 'bx-')

plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('Within Cluster Sum of Squares')

k_means = KMeans(n_clusters = 3, init = 'k-means++', random_state = 42)
prediction = k_means.fit_predict(mass_radius_column)

star_distance_list = df["distance"].tolist()
star_distance_list.pop(0)

print(star_distance_list)

star_gravity_list = df["star_gravity"].tolist()
star_gravity_list.pop(0)

print(star_gravity_list)

new_data = []
for data in star_distance_list:
    if data > 100:
        df.remove(data)
    new_data.append(df)

new_data.to_csv("output.csv")

new_data2 = []
for data in star_gravity_list:
    if data > 350 or data < 150:
        df.remove(data)
    new_data2.append(df)
star_names = df["star_names"].tolist()
star_names.pop(0)

star_mass = df["mass"].tolist()
star_mass.pop(0)

star_radius = df["radius"].tolist()
star_radius.pop(0)

star_distance = df["distance"].tolist()
star_distance.pop(0)

star_gravity = df["star_gravity"].tolist()
star_gravity.pop(0)
plt.figure()
sns.barplot(x = star_names,y = star_mass)
plt.title("Star Names VS MASS")
plt.xlabel('Names')
plt.ylabel('MASS')
plt.show()
plt.figure()
sns.barplot(x = star_names,y = star_radius)
plt.title("Star Names VS RADIUS")
plt.xlabel('Names')
plt.ylabel('RADIUS')
plt.show()
plt.figure()
sns.barplot(x = star_names,y = star_distance)
plt.title("Star Names VS DISTANCE")
plt.xlabel('Names')
plt.ylabel('DISTANCE')
plt.show()
plt.figure()
sns.barplot(x = star_names,y = star_gravity)
plt.title("Star Names VS GRAVITY")
plt.xlabel('Names')
plt.ylabel('GRAVITY')
plt.show()

fig1 = px.bar(x = star_names,y = star_mass,title="Names VS MASS")
fig1.show()

fig2 = px.bar(x = star_names,y = star_distance,title="Names VS DISTANCE")
fig2.show()

fig3 = px.bar(x = star_names,y = star_gravity,title="Names VS GRAVITY")
fig3.show()

fig4 = px.bar(x = star_names,y = star_radius,title="Names VS RADIUS")
fig4.show()

new_data2.to_csv("output2.csv")
plt.figure(figsize = (10, 5))
sns.scatterplot(x = mass_radius_column[prediction == 0, 0], y = mass_radius_column[prediction == 0, 1], color = 'orange', label = 'Star Cluster 1')
sns.scatterplot(x = mass_radius_column[prediction == 1, 0], y = mass_radius_column[prediction == 1, 1], color = 'blue', label = 'Star Cluster 2')
sns.scatterplot(x = mass_radius_column[prediction == 2, 0], y = mass_radius_column[prediction == 2, 1], color = 'green', label = 'Star Cluster 3')
sns.scatterplot(x = k_means.cluster_centers_[:, 0], y = k_means.cluster_centers_[:, 1], color = 'red', label = 'Centroids', s = 100, marker = ',')

plt.title('Clusters of Stars')
plt.xlabel('Mass of Stars')
plt.ylabel('Radius of Stars')
plt.legend()
sns.scatterplot(x = mass_list,y = radius_list)
plt.title("STAR MASS AND RADIUS")
plt.xlabel('MASS')
plt.ylabel('RADIUS')
plt.show()
plt.figure()