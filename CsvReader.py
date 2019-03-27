#import the pandas library and aliasing as pd
import re
import csv
import pandas as pd
import  urllib
#result1=1
import csv
from person_pojo import Person

Wire_shark_info = pd.read_csv("dns_check.csv") #csv read
select_relevnt_col = Wire_shark_info[["Source","Info"]] # choose relevent colmn
#print(select_relevnt_col)
df = pd.DataFrame(Wire_shark_info, columns = ['Info']) # Using panda for using dns
df_source = pd.DataFrame(Wire_shark_info, columns = ['Source'])
#df_cat=df[df['Info'].filter(regex=r'[www.google-analytics.com]')]
All_Result = {} #define tupel for dns query
Match_array_for_dns={} #after filtring
i=1 # counter
k=1 # counter
match_arr = []
for index, row in df.iterrows():  #iter for csv
    info_d=row['Info'] #info raw for manpultion
    #print(info_d)
    #print(Wire_shark_info[["Source","Info"]]) #check
    All_Result[i] = re.search('www.(.*).com', info_d) # search in rows for dns
    str_result = str(All_Result[i]) # casting for exttract dns
    #print(str_result)
    if (All_Result[i] is not 'None'): #check dns
     match = re.findall(r"'(.*)'",str_result) #find match
     #print(match) #print match
    #print(All_Result[i])
    Match_array_for_dns[k] = match
    match_arr.append(match)
    i=i+1
    k=k+1

#print(match_arr)


Index_Var_array = 0
list_of_person = []

csvData =  [['Source', 'Dns_query']]

with open('person.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)
    list_of_string_for_source = []

    for index, row in df_source.iterrows():
        Source_data = row['Source']
        list_of_string_for_source.append(Source_data)

    rows = zip(list_of_string_for_source , match_arr)
    # -------------- adi edit here --------------
    id =0

    for row in rows:
        
        find=0
        # print(row)
        writer.writerow(row)
        tmp= Person(id,row[0],row[1])
        # print(row)

        for l in list_of_person:
            if l.get_mac() == tmp.get_mac():
                l.add_to_dns(row[1] )
                find=1

        if find == 0:
            list_of_person.append(tmp)
            id=id+1

        #if not found any - create person


        #--------------done edit here--------------

    for l in list_of_person:
        print(l.id,l.mac , l.dns)

    # print(list_of_string_for_source)
    csvFile.close()

