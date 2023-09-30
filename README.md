# H2O-model
These are a couple of Python programs written to determine the total non-bonding energy of two water molecules. This resultant energy is the sum of all the electrostatic contributions and the Lennard-Jones potential between the two oxygen atoms.

Go to the **'Ordinary Configuration'** folder to find the script in which you can calculate the total energy at different separations when all hydrogen atoms are pointing to the left.

In the folder named **'Inverted Configuration'**, you will find a script that performs the same calculations but in a configuration where the pair of hydrogen atoms from one molecule is pointing in the opposite direction compared to the hydrogen atoms of the other molecule. There are two ways to arrange this configuration: with hydrogens facing inward toward the center of mass and with hydrogens facing outward from it.

# How to use it

There is a piece of code in each of the two scripts mentioned above:

<div style="
  background-color: #f7f7f7;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 20px;
  margin-bottom: 20px;
  font-family: 'Courier New', monospace;
  white-space: pre-wrap;
  overflow-x: auto;
">
  <pre>
    <code>
      # Ruta del archivo CSV
      archivo_csv = "C:/Users/USUARIO/Downloads/chemcraft/molecules csv/H4O2({}).csv".format(distance_in_amstrongs)
    </code>
  </pre>
</div>

You need to change this path to specify where the coordinates files are located. The coordinates files set the distance beetween the two molecules. For example, in this repository, inside **Ordinary Configuration** there is a folder named as **Coordinates Files**, as you see, you can find 5 files, in which every file, contains the coordinates of the two molecules in the ordinary configuration with a separation of the number of amstrongs that is indicated in the name of file, this means, H4O2(3.6) for 3.6 amstrongs, H4O2 for 4 amstrongs and so on. 

The same idea for **Inverted Configuration**, but for this case, some of the files are for the inverted config in which the hydrogens looks outwards and some are for the case looking inwards, you can differentiate these files easily, because inside code is specified the set of distances associated to the configuration of interest:

<div style="background-color:#f5f5f5; padding:10px; border-radius:5px; border:1px solid #ddd;">
  <pre>
    <code>
      distances_outwards = [7,6,5,4,3,2,1,0.8,0.6,0.58,0.56,0.54,0.52] #List of distances between Oxigen atoms of the two water molecules in a inverted position, hydrogens are looking outwards to the center of mass.
      energies_outwards = [] #List with total energies, hydrogens looking outwards to the center of mass.
    </code>
    <code>
      distances_inwards = [7.01,6.01,5.01,4.01,3.01,2.01,1.8] #List of distances between Oxigen atoms of the two water molecules in a inverted position, hydrogens looking inwards to the center of mass.
      energies_inwards = [] #List of total energies, hydrogens looking inwards to the center of mass.
    </code>
  </pre>
</div>

Therefore, you just can identify in every name in file, and recognize which one is for inwards or outwards, because the distances to test each case are unique.
