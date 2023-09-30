import matplotlib.pyplot as plt

def tot_energy(distance_in_amstrongs):
    import re
    import math
    import numpy as np

    # Ruta del archivo CSV
    archivo_csv = "C:/Users/USUARIO/Downloads/chemcraft/molecules csv/original-pos/H4O2({}).csv".format(distance_in_amstrongs)

    # Listas para almacenar las columnas
    atom_index = []
    coordinates = []

    # Leer el archivo CSV
    with open(archivo_csv, 'r') as csv_file:
        for line in csv_file:
            # Usar expresión regular para dividir la línea en columnas por cualquier cantidad de espacios
            columns = re.split(r'\s+', line.strip())

            if len(columns) == 4:
                atom_index.append(columns[0])
                coordinates.append(list(map(float, columns[1:])))

    # Definir el tamaño de la matriz
    num_atoms = len(coordinates)
    matrix_rij = np.zeros((num_atoms, num_atoms))

    # Llenar la matriz con valores
    for i in range(num_atoms):
        for j in range(num_atoms):
            rij = math.sqrt(sum((ci - cj) ** 2 for ci, cj in zip(coordinates[i], coordinates[j])))
            matrix_rij[i, j] = rij

    qi = qj = 0 #We define the variables that we're gonna use to store the value of the charges of each atom.

    electrostatic_energy_matrix_rij = np.zeros((num_atoms, num_atoms))
    Lennard_Jones_potential_energy_matrix_rij = np.zeros((num_atoms, num_atoms))
    # Calculate non-bonding energies and distances
    E_total_electrostatic = 0

    #To calculate the sum of all the atomic contributions of electrostatic energy, we use the following for cycle...
    for i in [0,1,2]:
        for j in [3,4,5]:
            rij = matrix_rij[i, j]
            if atom_index[i] == '1':
                qi = 0.417
            elif atom_index[i] == '8':
                qi = -0.417 * 2
            if atom_index[j] == '1':
                qj = 0.417
            elif atom_index[j] == '8':
                qj = -0.417 * 2

            Eij = ((qi * qj) / rij) * 332
            electrostatic_energy_matrix_rij[i, j] = Eij
            E_total_electrostatic += Eij

    # To calculate the sum of all the atomic contributions of Lennard-Jones potential energy, we use the following...
    rOO = matrix_rij[1, 4]
    EOO = ((0.582 / rOO ** 12) - (595.0 / rOO ** 6))
    E_Lennard_Jones = EOO

    E_total = E_total_electrostatic + E_Lennard_Jones
    return E_total


distances_original = [7,6,5,4,3.6] #List of distances between Oxigen atoms, of the two water molecules (all hydogens pointing to the left).
energies_original = [] #List with total energies of the two molecules at original position.

#Append the results of total energy for the inverted molecules
for distance in distances_original:
    energies_original.append(tot_energy(distance))

#Both graphs superposed:

# Create a figure
plt.figure(figsize=(10, 6))

# Set the y-axis limits to a maximum of 10
plt.ylim(-4, 0)

# Plot the inverted molecules data
plt.plot(distances_original, energies_original, label='Molecules with the whole hydrogen´s looking to left', marker='o')

# Add labels and title
plt.xlabel('Distance in amstrongs')
plt.ylabel('Total energy [electro + Lennard-Jones]')
plt.title('Energy vs Distance for Molecules at the Original Position (all hydrogen´s pointing to the left')

# Add a legend
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
