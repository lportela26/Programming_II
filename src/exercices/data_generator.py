import pandas as pd
 
data = {

    "City" : ["Punta Cana", "Santo Domingo", "Santiago"],
    "Population" : [50000, 1000000, 500000]
}

df = pd.DataFrame(data)

df.to_csv("data/data_generated.csv")
print("data saved succesfully")