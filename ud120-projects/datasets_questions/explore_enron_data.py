#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print(len(enron_data))
count = 0
mailcount = 0
nanPaymentCount = 0
total = len(enron_data)
poiCount = 0
poiNanCount = 0
import math
for data in enron_data:
    # print len(data)
    # print(enron_data[data])
    # print(len(enron_data[data]))
    # if (enron_data[data]["poi"]==1):
    #     count = count + 1
    if (math.isnan(float(enron_data[data]["salary"]))):
        count = count + 1
    if (enron_data[data]["email_address"] != enron_data[data]["email_address"]):
            mailcount = mailcount + 1
    #print(enron_data[data]["email_address"])
    if (math.isnan(float(enron_data[data]["total_payments"]))):
        nanPaymentCount = nanPaymentCount + 1
    if (math.isnan(float(enron_data[data]["poi"]))):
        poiNanCount = poiNanCount + 1
    elif (enron_data[data]["poi"]==1):
        poiCount = poiCount + 1
print(count)
print(mailcount)
print(nanPaymentCount)
print((nanPaymentCount*100)/total)
print(poiCount, poiNanCount, (poiCount*100)/(poiNanCount + poiCount))
# print(enron_data["PRENTICE JAMES"]["total_stock_value"])
# print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])
# print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

# print(enron_data["SKILLING JEFFREY K"]["total_payments"])
# print(enron_data["LAY KENNETH L"]["total_payments"])
# print(enron_data["FASTOW ANDREW S"]["total_payments"])

#from feature_format import feature_format as ff
#received = ff.featureFormat(enron_data,["total_payments"])

#print(len(received))