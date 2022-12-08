#!/usr/bin/env python
# coding: utf-8

# In[102]:


import sys
import re
import getopt


# In[106]:


if len(sys.argv) < 2:
    print('usage: python parse.py -f <file name> or python parse.py --file= <file name> ')
    exit(1)

argv = sys.argv[1:]
file_name = ""
  
try:
    opts, args = getopt.getopt(argv, "f:", ["file=",])
except:
    print("Error")
  
for opt, arg in opts:
    if opt in ['-f', '--file']:
        file_name = arg


# In[107]:
gflops = 0.0
total_tasks_executed = 0.0
total_compute_tasks_executed = 0.0
level0_tasks_migrated = 0.0
level1_tasks_migrated = 0.0
level2_tasks_migrated = 0.0
total_tasks_migrated = 0.0
total_affinity_tasks_executed = 0.0
total_deals  = 0.0
successful_deals = 0.0
total_evictions  = 0.0
stage_in_initiated = 0.0
stage_in_required = 0.0


# In[108]:



r = re.compile(r"[^0-9.]")
with open (file_name, 'rt') as myfile: # Open file for reading text data.
    for myline in myfile:                # For each line, stored as myline,

        if(myline.find('gflops/s=') != -1):
            ' '.join(myline.split())  #replace multiple by one white space
            list_of_words = myline.split() 
            next_word = list_of_words[list_of_words.index('gflops/s=') + 1]
            next_word = r.sub('', next_word)
            
            if(float(next_word) > gflops):
                gflops = float(next_word)
        
            #print(list_of_words)
   
        if(myline.find('Total tasks executed                   :') != -1):
            ' '.join(myline.split())  #replace multiple by one white space
            list_of_words = myline.split()
            next_word = list_of_words[list_of_words.index('executed') + 2]
            next_word = r.sub('', next_word)

            if(float(next_word) > total_tasks_executed):
                total_tasks_executed = float(next_word)

            #print(list_of_words)

        if(myline.find('Total compute tasks executed           :') != -1):
            ' '.join(myline.split())  #replace multiple by one white space
            list_of_words = myline.split()
            next_word = list_of_words[list_of_words.index('executed') + 2]
            next_word = r.sub('', next_word)

            if(float(next_word) > total_compute_tasks_executed):
                total_compute_tasks_executed = float(next_word) 

            #print(list_of_words)

        if(myline.find('Tasks migrated                         :') != -1):
            ' '.join(myline.split())  #replace multiple by one white space
            list_of_words = myline.split()

            next_word = list_of_words[list_of_words.index('level0') + 1]
            next_word = r.sub('', next_word)
            if(float(next_word) > level0_tasks_migrated):
                level0_tasks_migrated = float(next_word) 

            next_word = list_of_words[list_of_words.index('level1') + 1]
            next_word = r.sub('', next_word)
            if(float(next_word) > level1_tasks_migrated):
                level1_tasks_migrated = float(next_word) 

            next_word = list_of_words[list_of_words.index('level2') + 1]
            next_word = r.sub('', next_word)
            if(float(next_word) > level2_tasks_migrated):
                level2_tasks_migrated = float(next_word) 

            #print(list_of_words)

        if(myline.find('Tasks with affinity migrated           :') != -1):
            ' '.join(myline.split())  #replace multiple by one white space
            list_of_words = myline.split()
            next_word = list_of_words[list_of_words.index('migrated') + 2]
            next_word = r.sub('', next_word)

            if(float(next_word) > total_affinity_tasks_executed):
                total_affinity_tasks_executed = float(next_word) 

            #print(list_of_words)

        if(myline.find('Total deals                            :') != -1):
            ' '.join(myline.split())  #replace multiple by one white space
            list_of_words = myline.split()
            next_word = list_of_words[list_of_words.index('deals') + 2]
            next_word = r.sub('', next_word)

            if(float(next_word) > total_deals):
                total_deals = float(next_word) 

            #print(list_of_words)

        if(myline.find('Successful deals                       :') != -1):
            ' '.join(myline.split())  #replace multiple by one white space
            list_of_words = myline.split()
            next_word = list_of_words[list_of_words.index('deals') + 2]
            next_word = r.sub('', next_word)

            if(float(next_word) > successful_deals):
                successful_deals = float(next_word) 

            #print(list_of_words)

        if(myline.find('Total evictions                        :') != -1):
            ' '.join(myline.split())  #replace multiple by one white space
            list_of_words = myline.split()
            next_word = list_of_words[list_of_words.index('evictions') + 2]
            next_word = r.sub('', next_word)

            if(float(next_word) > total_evictions):
                total_evictions = float(next_word) 

            #print(list_of_words)

        if(myline.find('Total stage in initiated               :') != -1):
            ' '.join(myline.split())  #replace multiple by one white space
            list_of_words = myline.split()
            next_word = list_of_words[list_of_words.index('initiated') + 2]
            next_word = r.sub('', next_word)

            if(float(next_word) > stage_in_initiated):
                stage_in_initiated = float(next_word) 

            #print(list_of_words)
        
        if(myline.find('Total stage in required                :') != -1):
            ' '.join(myline.split())  #replace multiple by one white space
            list_of_words = myline.split()
            next_word = list_of_words[list_of_words.index('required') + 2]
            next_word = r.sub('', next_word)

            if(float(next_word) > stage_in_required):
                stage_in_required = float(next_word) 

            print(list_of_words)

            
    
     
myfile.close()           
            
print("%s = %s" % ('GFlops/s', gflops))
print("%s = %s" % ('Total tasks executed', total_tasks_executed))
print("%s = %s" % ('Total compute tasks executed', total_compute_tasks_executed))
print("%s = %s" % ('Perc of compute tasks', total_compute_tasks_executed / total_tasks_executed * 100))
total_tasks_migrated = level0_tasks_migrated + level1_tasks_migrated + level2_tasks_migrated
print("%s = level0 %s, level1 %s, level2 %s (Total %s)" % ('Tasks migrated', level0_tasks_migrated, level1_tasks_migrated, level2_tasks_migrated, total_tasks_migrated))
print("%s = %s" % ('Total tasks with affinity migrated', total_affinity_tasks_executed))
print("%s = %s" % ('Perc of affinity tasks', total_affinity_tasks_executed / total_tasks_migrated * 100))
print("%s = %s" % ('Total deals', total_deals))
print("%s = %s" % ('Successful deals', successful_deals))
print("%s = %s" % ('Avg task migrated per deal', total_tasks_migrated / total_deals))
print("%s = %s" % ('Avg task migrated per successfull deal', total_tasks_migrated / successful_deals))
print("%s = %s" % ('Avg task migrated per successfull deal', successful_deals / total_deals * 100) )
print("%s = %s" % ('Total evictions', total_evictions) )
print("%s = %s" % ('Total stage in initiated', stage_in_initiated) )
print("%s = %s" % ('Total stage in required', stage_in_required) )
print("%s = %s" % ('Perc eviction for stage in required', total_evictions / stage_in_required * 100) )


