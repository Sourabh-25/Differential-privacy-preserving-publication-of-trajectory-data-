import numpy as np
import os

trajectories = {}

# Read the updated database file
with open("output_database_updated.txt", 'r') as input_file:
    for line in input_file:
        parts = line.strip().split(',')
        id = int(parts[0])
        cluster_number = int(parts[2])
        
        # Append cluster_number to trajectories[id]
        if id in trajectories:
            trajectories[id].append(cluster_number)
        else:
            trajectories[id] = [cluster_number]

# Count occurrences of each trajectory
trcnt = {}
tc=[]
for trajectory in trajectories.values():
    trajectory_str = ','.join(map(str, trajectory))
    if trajectory_str in trcnt:
        trcnt[trajectory_str] += 1
    else:
        trcnt[trajectory_str] = 1

# Print trajectories and their counts
i=0
for i in range(150, 200):
    if str(trajectories[i]) in trcnt:
        trcnt[str(trajectories[i])] = 0
i=0
for trajectory, count in trcnt.items():
    i+=1
    # print(f"Trajectory: {trajectory}, Count: {count}")
    tc.append(count)
print(i)


def compute_average(data):
    return np.mean(data)

def laplace_pdf(x, mu, beta):
    return (1 / (2 * beta)) * np.exp(-abs(x - mu) / beta)

def differentially_private_noise_generation(tc, alpha, beta):
    n1 = len(tc)
    N = len(tc)  # Assuming N = n1

    if alpha < 0 or n1 <= 0:
        return None

    nc = [0] * N
    z=0
    z=1
    # for p in range(n1):
    #     for q in range(n1):
    mu = compute_average(tc)
    df = z
    b = df / mu
    beta = 2 * mu

    i = 0
    # print(beta)
    while True:
                ln_i = np.random.laplace(0, b)

                if alpha < ln_i < beta and i < n1:
                    
                    if(i<n1):
                    #  print(ln_i)
                     nc[i] = tc[i] + ln_i
                     i+=1
                    else:
                     break
                if(i>=n1):
                   break

    return nc

nc=differentially_private_noise_generation(tc,0,2)
print(len(tc))
# print(nc)
# Write trcnt dictionary to a file
i=0
with open("trajectory_publication.txt", 'w') as output_file:
    for trajectory, count in trcnt.items():
        output_file.write(f"Trajectory: {trajectory} { i}, Count: {nc[i]}\n")
        i+=1
print("Trajectory counts written to 'trajectory_counts.txt'.")

# Specify the file paths to delete
file_paths = ["output_database.txt", "released_database.txt","output_database_updated.txt"]

# Delete each file
for file_path in file_paths:
    try:
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred while deleting '{file_path}': {e}")
