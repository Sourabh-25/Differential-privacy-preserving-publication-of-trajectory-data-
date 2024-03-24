import numpy as np

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
# Define the array to store the last entries
tc = []

# Read each line from the file and extract the last entry
with open("released_database.txt", 'r') as file:
    for line in file:
        parts = line.strip().split(',')
        # print(parts)
        if parts[-1].strip():  # Check if the last entry is not empty
            last_entry = int(parts[-1])
            if(last_entry==0):
               tc.append(0.0)
            else:
            #  print(last_entry)  # Extract the last entry and convert it to an integer
              tc.append(last_entry)  # Append it to the tc array

# Print the tc array
print(len(tc))
# print("Last entries stored in tc array:")
# print (tc)


alpha = 0
beta = 1.1
nc = differentially_private_noise_generation(tc, alpha, beta)
# print(len(result))
# print(result)
def truncate_float(float_number, decimal_places):
    multiplier = 10 ** decimal_places
    return int(float_number * multiplier) / multiplier

def append_to_each_line(filename):
    i=0
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
           
            line = line.strip() +" "+ str(truncate_float(nc[i],3))+"\n"
            i+=1
            file.write(line)

# Call the function to append ", 1" to each line in the file
filename="released_database.txt"
with open(filename, 'r') as file:
 lines = file.readlines()

 with open(filename, 'w') as file:
        for line in lines:
            entries = line.split(",")
        # Remove the last entry
            entries = entries[:-1]
        # Join the remaining entries with commas and write to the output file
            file.write(",".join(entries) + "\n")
append_to_each_line("released_database.txt")

