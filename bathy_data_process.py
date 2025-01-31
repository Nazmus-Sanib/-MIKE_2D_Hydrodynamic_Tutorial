data = "E:/DU_research/Data/Data/Bathymetry/2022/3969-SP1_2022_River-delta_cleaned_Interpolated10x10_XYZ_.txt"


print("""The default data path is: \n E:/DU_research/Data/Data/Bathymetry/2022/3969-SP1_2022_River-delta_cleaned_Interpolated10x10_XYZ_.txt \n
       Do you want to change the data? Answer YES or NO.\n""")

q1 = input()

if q1 == "YES":
    print("\nPlease paste here the path of the data\n")
    q2 = input()
else:
    pass


import pandas as pd

data = pd.read_csv("E:/DU_research/Data/Data/Bathymetry/2022/3969-SP1_2022_River-delta_cleaned_Interpolated10x10_XYZ_.txt",
                   sep = " ")

cols = [i for i in data.columns]

northing = [round(float(i),1) for i in data[data[cols[2]]<0][cols[0]]]

easting = [round(float(i),1) for i in data[data[cols[2]]<0][cols[1]]]

bathy = [round(float(i),1) for i in data[data[cols[2]]<0][cols[2]]]

index = [i+1 for i in range(len(bathy))]

print("""The default output location is \n E:/DU_research/Data/Data/Bathymetry/2022/ \n
         Do you want to change the default location? Answer YES or NO.\n""")

q3 = input()

output_path = "E:/DU_research/Data/Data/Bathymetry/2022/"

if q3 == "YES":
    print("\nPlease paste here the path\n")
    output_path = input()
else:
    pass
    
      
with open(output_path+"/Water_data.xyz", "w") as f:

    for i in range(len(bathy)):

        tmp = "   {n}    {e}      {b}        {index}\n".format(n = str(northing[i]),
                                       e = str(easting[i]),
                                       b = str(bathy[i]),
                                       index = str(index[i]))
        f.write(tmp)

    f.close()


