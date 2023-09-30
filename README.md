# H2O-model
These are a couple of Python programs written to determine the total non-bonding energy of two water molecules. This resultant energy is the sum of all the electrostatic contributions and the Lennard-Jones potential between the two oxygen atoms.

Go to the **'Ordinary Configuration'** folder to find the script in which you can calculate the total energy at different separations when all hydrogen atoms are pointing to the left.

In the folder named **'Inverted Configuration'**, you will find a script that performs the same calculations but in a configuration where the pair of hydrogen atoms from one molecule is pointing in the opposite direction compared to the hydrogen atoms of the other molecule. There are two ways to arrange this configuration: with hydrogens facing inward toward the center of mass and with hydrogens facing outward from it.

# How to use it

There is a piece of code in each of the two scripts mentioned above:

<div style="background-color:#f5f5f5; padding:10px; border-radius:5px; border:1px solid #ddd;">
  <pre>
    <code>
      # Ruta del archivo CSV
      archivo_csv = "C:/Users/USUARIO/Downloads/chemcraft/molecules csv/H4O2({}).csv".format(distance_in_amstrongs)
    </code>
  </pre>
</div>

You need to change this path to specify where the coordinates files are located. The coordinates files set the distance beetween the two molecules. For example, in this repository, inside **Ordinary Configuration** there is a folder named as **Coordinates Files**, as you see, you can find 5 files, in which every file, contains the coordinates of the two molecules in the ordinary configuration with a separation of the **number of amstrongs that is indicated in the name of file**, this means, **H4O2(3.6) for 3.6 amstrongs, H4O2(4) for 4 amstrongs and so on**. 

The same idea for **Inverted Configuration**, but for this case, some of the files are for the inverted config in which the **hydrogens looks outwards and some are for the case looking inwards**, you can differentiate these files easily, **because inside code is specified the set of distances associated to the configuration of interest**:

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

# Modelo H2O

Estos son un par de programas escritos en Python diseñados para determinar la energía total no enlazante de dos moléculas de agua. Esta energía resultante es la suma de todas las contribuciones electrostáticas y el potencial de Lennard-Jones entre los dos átomos de oxígeno.

Ve al directorio **'Configuración Ordinaria'** para encontrar el script en el que puedes calcular la energía total a diferentes separaciones cuando todos los átomos de hidrógeno apuntan hacia la izquierda.

En el directorio llamado **'Configuración Invertida'**, encontrarás un script que realiza los mismos cálculos, pero en una configuración en la que el par de átomos de hidrógeno de una molécula apunta en dirección opuesta con respecto a los átomos de hidrógeno de la otra molécula. Hay dos formas de configurar esta disposición: con los hidrógenos orientados hacia el centro de masa y con los hidrógenos orientados hacia afuera desde él.

# Como utilizarlo

En cada uno de los dos scripts mencionados anteriormente, encontrarás un fragmento de código:

<div style="background-color:#f5f5f5; padding:10px; border-radius:5px; border:1px solid #ddd;">
  <pre>
    <code>
      # Ruta del archivo CSV
      archivo_csv = "C:/Users/USUARIO/Downloads/chemcraft/molecules csv/H4O2({}).csv".format(distance_in_amstrongs)
    </code>
  </pre>
</div>

Debes cambiar esta ruta para especificar dónde se encuentran los archivos de coordenadas. Los archivos de coordenadas establecen la distancia entre las dos moléculas. Por ejemplo, en este repositorio, dentro de **Configuración Ordinaria**, encontrarás una carpeta llamada **Archivos de Coordenadas**. Como puedes ver, hay 5 archivos, y en cada uno de ellos se encuentran las coordenadas de las dos moléculas en la configuración ordinaria, con una separación de **la cantidad de ángstroms que se indica en el nombre del archivo**, esto significa que **H4O2(3.6) es para 3.6 ángstroms, H4O2(4) para 4 ángstroms, y así sucesivamente**.

La misma idea aplica para la Configuración Invertida, pero en este caso, algunos de los archivos son para la configuración invertida en la que los hidrógenos miran hacia afuera y otros para cuando miran hacia adentro. Puedes diferenciar fácilmente estos archivos porque dentro del código se especifica el conjunto de distancias asociado a la configuración de interés:

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

Por lo tanto, puedes identificar cada nombre de archivo y reconocer cuál es para la configuración hacia adentro o hacia afuera, ya que las distancias para probar cada caso son únicas.
