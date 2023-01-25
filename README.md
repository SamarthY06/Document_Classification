The Code is developed to solve the problem statement 

1) Based on the input file, the documents must be identified, classified, and divided
into multiple groups. The user can submit a single file (image/pdf/word document)
that contains many documents. Create a library that accepts a user supplied file and
recognises and splits numerous documents existing in the file.
Documents to be classified and split are:
• PAN
• Aadhaar (Aadhaar front, Aadhaar back)
• Bank Statement
• ITR/Form 16
• Customer Photograph (Selfie)
• Utility Bill (Power, Water, Gas, Landline etc)
• Cheque Leaf
• Salary Slip/Certificate
• Driving License
• Voter ID
• Passport
2) Once document is classified and split, create a library which accepts split
document and extracts the data from it.

Steps to run the code:

1) To run this file make sure you upload a pdf containing multiple pages or an image in jpeg format or a word document in data/test/predict
2) Alternate (Train the model using a good set of dataset and store the weights. All the architecture has been done in train.py just make sure you upload the data in data/train in the folders of the class names.)
3) Make sure you configure the path of tesseract and poppler in extractor.py and document_splitter.py respectively.
4) You just have to run the main.py by the command 
python main.py
5) It will output a csv with the column names name,text,label where name is the file name of the test file uploaded , text is the text in that file, label is the class to which it belongs to (PAN,Aadhar.....).

Disclaimer: I have saved some weights but they are not accuracte enough as I didn't had a proper dataset of many images so to predict the class label using the model(train.py) you can train the model as suggested in 2nd point.
For predicting the labels you just need to uncomment the last 3 lines of main.py

