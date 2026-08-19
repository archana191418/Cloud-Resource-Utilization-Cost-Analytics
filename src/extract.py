import os 
import shutil 
import kagglehub

# Download latest version
path = kagglehub.dataset_download("freshersstaff/multi-cloud-resource-dataset")

#creating file folder if does not exist 
destination="data/raw"
os.makedirs(destination,exist_ok=True)
#copy all files from cache to it's destination
for file in os.listdir(path):
    source=os.path.join(path,file)
    shutil.copy(source,destination)
print("dataset is downloaded successfully")
print("source:",source)
print("destination:",destination )