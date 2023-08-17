import pandas

data = pandas.read_csv("https://pythonhow.com/media/data/sampledata.txt")

concatenated = pandas.concat([data,data * 2])

concatenated.to_csv("Practice-100-Python-Questions\Section-3\csv_data_generated_74.csv",index=None)

