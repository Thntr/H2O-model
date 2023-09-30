import matplotlib.pyplot as plt

def tot_energy(distance_in_amstrongs):
    import re
    import math
    import numpy as np

    # Ruta del archivo CSV
    archivo_csv = "C:/Users/USUARIO/Downloads/chemcraft/molecules csv/H4O2({}).csv".format(distance_in_amstrongs)

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



    # To calculate the sum of all the atomic contributions of Lennard-Jones potential energy, we use the following for cycle...
    E_total_Lennard_Jones = 0
    for i in [0, 1, 2]:
        for j in [3, 4, 5]:
            if atom_index[i] == '8' and atom_index[j] == '8':
                rij = matrix_rij[i, j]
                Eij = ((0.582 / rij ** 12) - (595.0 / rij ** 6))
                Lennard_Jones_potential_energy_matrix_rij[i, j] = Eij
                E_total_Lennard_Jones = Eij

    # To calculate the sum of all the atomic contributions of Lennard-Jones potential energy, we use the following...
    rOO = matrix_rij[1, 4]
    EOO = ((0.582 / rOO ** 12) - (595.0 / rOO ** 6))
    E_Lennard_Jones = EOO

    E_total = E_total_electrostatic + E_Lennard_Jones

    return E_total


distances_outwards = [7,6,5,4,3,2,1,0.8,0.6,0.58,0.56,0.54,0.52] #List of distances between Oxigen atoms of the two water molecules in a inverted position, hydrogens are looking outwards to the center of mass.
energies_outwards = [] #List with total energies, hydrogens looking outwards to the center of mass.

distances_inwards = [7.01,6.01,5.01,4.01,3.01,2.01,1.8] #List of distances between Oxigen atoms of the two water molecules in a inverted position, hydrogens looking inwards to the center of mass.
energies_inwards = [] #List of total energies, hydrogens looking inwards to the center of mass.

#Append the results of total energy for the inverted molecules (H's outwards)
for distance in distances_outwards:
    energies_outwards.append(tot_energy(distance))

#Append the results of total energy for the water molecules (H's inwards)
for distance in distances_inwards:
    energies_inwards.append(tot_energy(distance))

#Both graphs superposed:

# Create a figure
plt.figure(figsize=(10, 6))

# Set the y-axis limits to a maximum of 10
plt.ylim(0, 30)

# Plot the inverted molecules data, outwards arrange
plt.plot(distances_outwards, energies_outwards, label='Molecules Inverted (Hs looking outwards)', marker='o')

# Plot the inverted molecules data, inwards arrange
plt.plot(distances_inwards, energies_inwards, label='Molecules Inverted (Hs looking inwards)', marker='s')

# Add labels and title
plt.xlabel('Distance in amstrongs')
plt.ylabel('Total energy [electro + Lennard-Jones]')
plt.title('Energy vs Distance for Inverted Inwards and Inverted Outwards')

# Add a legend
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
