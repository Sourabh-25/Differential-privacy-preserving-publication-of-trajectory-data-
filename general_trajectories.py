from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# Load the database from the text file
database = []
with open("output_database.txt", 'r') as input_file:
    for line in input_file:
        parts = line.strip().split(',')
        entry = {
            'id': int(parts[0]),
            'date_time': parts[1],
            'longitude': float(parts[2]),
            'latitude': float(parts[3])
        }
        database.append(entry)

# Extract longitude and latitude into a numpy array
locations = np.array([[entry['longitude'], entry['latitude']] for entry in database])

# Define the number of clusters (k)
k = 10

# Apply k-means clustering
kmeans = KMeans(n_clusters=k)
kmeans.fit(locations)

# Get cluster labels and centroids
cluster_labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Plot clusters
plt.figure(figsize=(10, 8))
for i in range(k):
    cluster_points = locations[cluster_labels == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f'Cluster {i+1}')

# Plot centroids
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', color='black', label='Centroids')

# plt.xlabel('Longitude')
# plt.ylabel('Latitude')
# plt.title('K-means Clustering')
# plt.legend()
# plt.grid(True)
# plt.show()
import random
import datetime
import math
def truncate_float(float_number, decimal_places):
    multiplier = 10 ** decimal_places
    return int(float_number * multiplier) / multiplier


# Function to write trajectories to a file
def write_trajectories_to_file(trajectories, filename):
    with open(filename, 'a') as file:
        for trajectory in trajectories:
            for point in trajectory:
                file.write(f"{point['id']},{point['time']},{point['longitude']},{point['latitude']},{point['tc']}\n")

trajectories = []

# Generate 100 trajectories
for i in range(150, 200):
    trajectory_id = i
    trajectory = []
    
    # Randomly select a cluster
    cluster_id = random.randint(0, k - 1)  # k is the number of clusters
    
    # Randomly select a point from the selected cluster
    cluster_points = locations[cluster_labels == cluster_id]
    
    # Ensure that each trajectory has at least 25 points
    while len(trajectory) < random.randint(25,40):
        random_point = random.choice(cluster_points)
        
        # Generate a random time for the point within a day
        random_time = datetime.datetime.now() + datetime.timedelta(seconds=random.randint(0, 86400))
        
        # Append the point with time and trajectory ID
        trajectory.append({
            'id': trajectory_id,
            'time': random_time.strftime('%Y-%m-%d %H:%M:%S'),
            'longitude': truncate_float( random_point[0]+ random.randint(25,50)/random.randint(10,30),5),
            'latitude':  truncate_float(random_point[1]+ random.randint(25,50)/random.randint(10,30),5),
             'tc': 0
        })
    
    trajectories.append(trajectory)

# Write the trajectories to the file
write_trajectories_to_file(trajectories, "released_database.txt")
