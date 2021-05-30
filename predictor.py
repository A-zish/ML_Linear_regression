# importing os module
import os


#Print yellow colour
os.system("tput setaf 3")

print(" \t\t\t\t\n\n #######This will predict your Height According TO Father's Height#######")

#print red colur
os.system("tput setaf 2")


print("\n\n\n\n ------>The Datab used to train machine is  based on a famous experiment by Karl Pearson around 1903. The number of cases is 1078. Random noise was added to the original data to produce heights to the nearest 0.1 inch.<------ ")

os.system("tput setaf 5")
print( "\n\n\n\n \t\t\tPLEASE ENTER MATHEMATICAL VALUE" )


os.system("tput setaf 7")

def predictor():
  import joblib
  model = joblib.load("height_predictor.pk")
  try:
    height = float(input("\n\nFather height: "))
    result = model.predict([[height]])
    print("son height: ",result,"inch")
  except:
    print("!!!!!!!please input a integer value")
predictor()
