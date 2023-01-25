import os
import numpy as np
import tensorflow as tf,keras
from document_splitter import DocumentSplitter
from keras.preprocessing.image import ImageDataGenerator
from classification import Classification
import pandas as pd

def func(value):
	return ''.join(value.splitlines())

# Define the directory paths for the training and test sets
test_dir = 'data/test_split/'

directory = 'data/test/predict/'
# Splitting and Extraction
document_splitter = DocumentSplitter()
for file in os.listdir(directory):
    if file.endswith('.pdf'):
        documents = document_splitter.pdf_splitter(directory+file)
    elif file.endswith('.jpeg') is not None:
        documents = document_splitter.image_splitter(directory+file)
    elif file.endswith('.docx') is not None:
        documents = document_splitter.docx_splitter(directory+file)

name = []
text = []
label = []
for df in documents:
    name.append(df["path"])
    text.append(df["text"])
res = []
for sub in text:
    res.append(sub.replace("\n", ""))

for i in res:
    #modified_text = func(i)
    print(str(i))
    if "Permanent Account Number Card" in str(i):
        Label = "PAN Card"
    elif "DRIVING LICENCE" in str(i):
        Label = "Driving Licence"
    elif "ELECTION COMMISSION OF INDIAN" in str(i):
        Label = "Voter ID"
    elif "BANK STATEMENT" in str(i):
        Label = "Bank Statement"
    elif "INCOME TAX" in str(i):
        Label = "ITR"
    elif "Unique Indentification Authority" in str(i):
        Label = "Aadhar"
    elif "SALARY" in str(i):
        Label = "Salary Slip"
    elif "RUPEES" in str(i):
        Label = "Cheque Leaf"
    elif "BILL" in str(i):
        Label = "Utility Bill"
    elif "PASSPORT" in str(i):
        Label = "Passport"
    else:
        Label = "Customer Photo"
    label.append(Label)
data = {
        "Label":label,
        "File_name": name,
        "Text": text
    }

# Create a dataframe
df = pd.DataFrame(data)

# Save the DataFrame to a csv file
df.to_csv('output.csv', index=False)

# Trained the model but due to less data available the model became biase

# Classify = Classification()
# Label = Classify.classify(test_dir)
# print(Label)
    


