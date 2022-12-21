
import sys
import re
import getopt
import os

from os import listdir
from os.path import isfile, join


if len(sys.argv) < 2:
    print('usage: python parse.py -d <dir name> -o <output file > or python parse.py --dir= <dir path> --out <output file >')
    exit(1)

dir_path = os.path.abspath(os.getcwd())
out_path = "output.txt"

argv = sys.argv[1:]

try:
    opts, args = getopt.getopt(argv, "d:o:", 
                               ["dir =",
                                "output ="])
  
except:
    print("Error")

for opt, arg in opts:
    if opt in ['-d', '--dir']:
        dir_path = arg
    elif opt in ['-o', '--output']:
        out_path = arg
        
print(dir_path)
print(out_path)

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
total_files  = 0.0
thrashing = 0

list_gflops = []
list_total_tasks_executed = []
list_total_compute_tasks_executed = []
list_perc_of_compute_tasks = []
list_level0 = []
list_level1 = []
list_level2 = []
list_total_tasks_migrated = []
list_total_affinity_tasks_migrated = []
list_perc_of_affinity_tasks = []
list_total_deals = []
list_successful_deals = []
list_avg_task_migrated_per_deal = []
list_avg_task_migrated_per_successfull_deal = []
list_perc_of_successfull_deals = []
list_total_evictions = []
list_stage_in_initiated = []
list_stage_in_required = []
list_perc_eviction_for_stage_in_required = []
list_tts = []
list_thrashing = []

#print(dir_path)
onlyfiles = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
#print(onlyfiles)

for file in onlyfiles:

    gflops  = 0
    total_tasks_executed = 0
    total_compute_tasks_executed  = 0
    level0_tasks_migrated = 0
    level1_tasks_migrated  = 0
    level2_tasks_migrated = 0
    total_affinity_tasks_executed  = 0
    total_deals = 0
    successful_deals = 0
    total_evictions  = 0
    stage_in_initiated = 0 
    stage_in_required = 0
    tts  = 0
    thrashing = 0
    
    myfile = os.path.abspath(join(dir_path, file))
    print(myfile)
    total_files = total_files + 1

    r = re.compile(r"[^0-9.]")
    with open (myfile, 'rt') as myfile: # Open file for reading text data.
        for myline in myfile:                # For each line, stored as myline,

        
            if(myline.find('Execution time =') != -1):
                ' '.join(myline.split())  #replace multiple by one white space
                list_of_words = myline.split()
                next_word = list_of_words[list_of_words.index('time') + 2]
                next_word = r.sub('', next_word)

                if(float(next_word) > tts):
                    tts = float(next_word) 
                    tts = tts / 1000000000

                #print(list_of_words)

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

                #print(list_of_words)


            if(myline.find('Total Thrashing                        :') != -1):
                ' '.join(myline.split())  #replace multiple by one white space
                list_of_words = myline.split()
                next_word = list_of_words[list_of_words.index('Thrashing') + 2]
                next_word = r.sub('', next_word)               
                if(float(next_word) > thrashing):
                    thrashing = float(next_word)




    myfile.close()   

    total_tasks_migrated = level0_tasks_migrated + level1_tasks_migrated + level2_tasks_migrated

    list_tts.append(tts)

    #print("%s  = %s" % ('GFlops/s', gflops))
    list_gflops.append(gflops)
    #print("%s  = %s" % ('Total tasks executed', total_tasks_executed))
    list_total_tasks_executed.append(total_tasks_executed)
    #print("%s  = %s" % ('Total compute tasks executed', total_compute_tasks_executed))
    list_total_compute_tasks_executed.append(total_compute_tasks_executed)
    #print("%s  = %s" % ('Perc of compute tasks', total_compute_tasks_executed / total_tasks_executed * 100))
    list_perc_of_compute_tasks.append(total_compute_tasks_executed / total_tasks_executed * 100)
    #print("%s  = level0 %s, level1 %s, level2 %s (Total %s)" % ('Tasks migrated', level0_tasks_migrated, level1_tasks_migrated, level2_tasks_migrated, total_tasks_migrated))
    list_level0.append(level0_tasks_migrated)
    list_level1.append(level1_tasks_migrated)
    list_level2.append(level2_tasks_migrated)
    list_total_tasks_migrated.append(total_tasks_migrated)
    #print("%s  = %s" % ('Total tasks with affinity migrated', total_affinity_tasks_executed))
    list_total_affinity_tasks_migrated.append(total_affinity_tasks_executed)

    if(total_tasks_migrated > 0):
        #print("%s  = %s" % ('Perc of affinity tasks', total_affinity_tasks_executed / total_tasks_migrated * 100))
        list_perc_of_affinity_tasks.append(total_affinity_tasks_executed / total_tasks_migrated * 100)
    else:
       #print("%s  = %s" % ('Perc of affinity tasks', 0)) 
       list_perc_of_affinity_tasks.append(0)

    #print("%s  = %s" % ('Total deals', total_deals))
    list_total_deals.append(total_deals)
    #print("%s  = %s" % ('Successful deals', successful_deals))
    list_successful_deals.append(successful_deals)

    if(total_deals > 0):
        #print("%s  = %s" % ('Avg task migrated per deal', total_tasks_migrated / total_deals))
        list_avg_task_migrated_per_deal.append(total_tasks_migrated / total_deals)
    else:
        #print("%s  = %s" % ('Avg task migrated per deal', 0))
        list_avg_task_migrated_per_deal.append(0)
    
    if(successful_deals > 0):
        #print("%s  = %s" % ('Avg task migrated per successfull deal', total_tasks_migrated / successful_deals))
        list_avg_task_migrated_per_successfull_deal.append(total_tasks_migrated / successful_deals)
    else:
        #print("%s  = %s" % ('Avg task migrated per successfull deal', 0))
        list_avg_task_migrated_per_successfull_deal.append(0)

    if(total_deals > 0):
        #print("%s  = %s" % ('perc of successfull deals', successful_deals / total_deals * 100) )
        list_perc_of_successfull_deals.append(successful_deals / total_deals * 100)
    else:
        #print("%s  = %s" % ('perc of successfull deals', 0) )
        list_perc_of_successfull_deals.append(0)
     
    #print("%s  = %s" % ('Total evictions', total_evictions) )
    list_total_evictions.append(total_evictions)
    #print("%s  = %s" % ('Total stage in initiated', stage_in_initiated) )
    list_stage_in_initiated.append(stage_in_initiated)
    #print("%s  = %s" % ('Total stage in required', stage_in_required) )
    list_stage_in_required.append(stage_in_required)

    if(stage_in_required > 0):
        #print("%s  = %s" % ('Perc eviction for stage in required', total_evictions / stage_in_required * 100) )
        list_perc_eviction_for_stage_in_required.append(total_evictions / stage_in_required * 100)
    else:
        #print("%s  = %s" % ('Perc eviction for stage in required', 0) )
        list_perc_eviction_for_stage_in_required.append(0)

    if(thrashing > 0):
        list_thrashing.append(thrashing)
    else:
        list_thrashing.append(0)

if(out_path == ""):

    #print(list_gflops)
    print("%s  : %s" % ('Total files', total_files ) )
    print("%s  : Min %s Max %s Avg %s" % ('Time to solution', min(list_tts), max(list_tts), sum(list_tts)/len(list_tts) ) )
    print("%s  : Min %s Max %s Avg %s" % ('GFlops', min(list_gflops), max(list_gflops), sum(list_gflops)/len(list_gflops) ) )
    print("%s  : Min %s Max %s Avg %s" % ('Total tasks', min(list_total_tasks_executed), max(list_total_tasks_executed), sum(list_total_tasks_executed)/len(list_total_tasks_executed) ) )
    print("%s  : Min %s Max %s Avg %s" % ('Compute tasks', min(list_total_compute_tasks_executed), max(list_total_compute_tasks_executed), sum(list_total_compute_tasks_executed)/len(list_total_compute_tasks_executed) ) )
    print("%s  : Min %s Max %s Avg %s" % ('Perc. compute tasks', min(list_perc_of_compute_tasks), max(list_perc_of_compute_tasks), sum(list_perc_of_compute_tasks)/len(list_perc_of_compute_tasks) ) )
    print("%s  : Min %s Max %s Avg %s" % ('Level0 tasks migrated', min(list_level0), max(list_level0), sum(list_level0)/len(list_level0) ) )
    print("%s  : Min %s Max %s Avg %s" % ('Level1 tasks migrated', min(list_level1), max(list_level1), sum(list_level1)/len(list_level1) ) )
    print("%s  : Min %s Max %s Avg %s" % ('Level2 tasks migrated', min(list_level2), max(list_level2), sum(list_level2)/len(list_level2) ) )
    print("%s  : Min %s Max %s Avg %s" % ('Total tasks migrated', min(list_total_tasks_migrated), max(list_total_tasks_migrated), sum(list_total_tasks_migrated)/len(list_total_tasks_migrated) ) )
    print("%s  : Min %s Max %s Avg %s" % ('Affinity tasks migrated', min(list_total_affinity_tasks_migrated), max(list_total_affinity_tasks_migrated), sum(list_total_affinity_tasks_migrated)/len(list_total_affinity_tasks_migrated) ) )
    print("%s  : Min %s Max %s Avg %s" % ('Perc. affinity tasks migrated', min(list_perc_of_affinity_tasks), max(list_perc_of_affinity_tasks), sum(list_perc_of_affinity_tasks)/len(list_perc_of_affinity_tasks) ) )
    print("%s  : Min %s Max %s Avg %s" % ('Deals', min(list_total_deals), max(list_total_deals), sum(list_total_deals)/len(list_total_deals) ) )
    print("%s  : Min %s Max %s Avg %s" % ('Successful deals', min(list_successful_deals), max(list_successful_deals), sum(list_successful_deals)/len(list_successful_deals) ) )
    print("%s  : Min %s Max %s Avg %s" % ('Avg. task migrated per deal', min(list_avg_task_migrated_per_deal), max(list_avg_task_migrated_per_deal), sum(list_avg_task_migrated_per_deal)/len(list_avg_task_migrated_per_deal) ) )
    print("%s  : Min %s Max %s Avg %s" % ('Avg. task migrated per success deal', min(list_avg_task_migrated_per_successfull_deal), max(list_avg_task_migrated_per_successfull_deal), sum(list_avg_task_migrated_per_successfull_deal)/len(list_avg_task_migrated_per_successfull_deal) ) )
    print("%s  : Min %s Max %s Avg %s" % ('Perc. success deal', min(list_perc_of_successfull_deals), max(list_perc_of_successfull_deals), sum(list_perc_of_successfull_deals)/len(list_perc_of_successfull_deals) ) )
    print("%s  : Min %s Max %s Avg %s" % ('Evictions', min(list_total_evictions), max(list_total_evictions), sum(list_total_evictions)/len(list_total_evictions) ) )
    print("%s  : Min %s Max %s Avg %s" % ('Stagein initiated', min(list_stage_in_initiated), max(list_stage_in_initiated), sum(list_stage_in_initiated)/len(list_stage_in_initiated) ) )
    print("%s  : Min %s Max %s Avg %s" % ('Stagein required', min(list_stage_in_required), max(list_stage_in_required), sum(list_stage_in_required)/len(list_stage_in_required) ) )
    print("%s  : Min %s Max %s Avg %s" % ('Perc. eviction per req. stagein', min(list_perc_eviction_for_stage_in_required), max(list_perc_eviction_for_stage_in_required), sum(list_perc_eviction_for_stage_in_required)/len(list_perc_eviction_for_stage_in_required) ) )
    print("%s  : Min %s Max %s Avg %s" % ('Thrashing', min(list_thrashing), max(list_thrashing), sum(list_thrashing)/len(list_thrashing) ) )
else:

    outputFile = open(out_path, 'w')

    out_string = 'Total files :' +  str(total_files) + '\n'
    outputFile.write(out_string)

    out_string = 'Time to solution :' + ' Min ' +  str(min(list_tts)) + ' Max ' + str(max(list_tts)) + ' Avg ' + str(sum(list_tts)/len(list_tts)) + '\n'
    outputFile.write(out_string)

    #print(list_gflops)
    out_string = 'GFlops :' + ' Min ' +  str(min(list_gflops)) + ' Max ' + str(max(list_gflops)) + ' Avg ' + str(sum(list_gflops)/len(list_gflops)) + '\n'
    outputFile.write(out_string)

    out_string = 'Total tasks :' + ' Min ' + str(min(list_total_tasks_executed)) + ' Max ' + str(max(list_total_tasks_executed)) + ' Avg ' + str( sum(list_total_tasks_executed)/len(list_total_tasks_executed) ) + '\n'
    outputFile.write(out_string)

    out_string = 'Compute tasks :' + ' Min ' + str(min(list_total_compute_tasks_executed)) + ' Max ' + str(max(list_total_compute_tasks_executed)) + ' Avg ' + str(sum(list_total_compute_tasks_executed)/len(list_total_compute_tasks_executed) ) + '\n'
    outputFile.write(out_string)

    out_string = 'Perc. compute tasks :' + ' Min ' + str(min(list_perc_of_compute_tasks)) + ' Max ' + str(max(list_perc_of_compute_tasks)) + ' Avg ' + str(sum(list_perc_of_compute_tasks)/len(list_perc_of_compute_tasks) ) + '\n'
    outputFile.write(out_string)

    out_string = 'Level0 tasks migrated :' + ' Min ' + str(min(list_level0)) + ' Max ' + str(max(list_level0)) + ' Avg ' + str(sum(list_level0)/len(list_level0) ) + '\n'
    outputFile.write(out_string)

    out_string = 'Level1 tasks migrated :' + ' Min ' + str(min(list_level1)) + ' Max ' + str(max(list_level1)) + ' Avg ' + str(sum(list_level1)/len(list_level1) ) + '\n'
    outputFile.write(out_string)

    out_string = 'Level2 tasks migrated :' + ' Min ' + str(min(list_level2)) + ' Max ' + str(max(list_level2)) + ' Avg ' + str(sum(list_level2)/len(list_level2) ) + '\n'
    outputFile.write(out_string)

    out_string = 'Total tasks migrated :' + ' Min ' + str(min(list_total_tasks_migrated)) + ' Max ' + str(max(list_total_tasks_migrated)) + ' Avg ' + str(sum(list_total_tasks_migrated)/len(list_total_tasks_migrated) ) + '\n'
    outputFile.write(out_string)

    out_string = 'Affinity tasks migrated :' + ' Min ' + str(min(list_total_affinity_tasks_migrated)) + ' Max ' + str(max(list_total_affinity_tasks_migrated)) + ' Avg ' + str(sum(list_total_affinity_tasks_migrated)/len(list_total_affinity_tasks_migrated) ) + '\n'
    outputFile.write(out_string)

    out_string = 'Perc. affinity tasks migrated :' + ' Min ' + str(min(list_perc_of_affinity_tasks)) + ' Max ' + str(max(list_perc_of_affinity_tasks)) + ' Avg ' + str(sum(list_perc_of_affinity_tasks)/len(list_perc_of_affinity_tasks) ) + '\n'
    outputFile.write(out_string)

    out_string = 'Deals :' + ' Min ' + str(min(list_total_deals)) + ' Max ' + str(max(list_total_deals)) + ' Avg ' + str(sum(list_total_deals)/len(list_total_deals) ) + '\n'
    outputFile.write(out_string)

    out_string = 'Successful deals :' + ' Min ' + str(min(list_successful_deals)) + ' Max ' + str(max(list_successful_deals)) + ' Avg ' + str(sum(list_successful_deals)/len(list_successful_deals) ) + '\n'
    outputFile.write(out_string)

    out_string = 'Avg. task migrated per deal' + ' Min ' + str(min(list_avg_task_migrated_per_deal)) + ' Max ' + str(max(list_avg_task_migrated_per_deal)) + ' Avg ' + str(sum(list_avg_task_migrated_per_deal)/len(list_avg_task_migrated_per_deal) ) + '\n'
    outputFile.write(out_string)

    out_string = 'Avg. task migrated per success deal' + ' Min ' + str(min(list_avg_task_migrated_per_successfull_deal)) + ' Max ' + str(max(list_avg_task_migrated_per_successfull_deal)) + ' Avg ' + str(sum(list_avg_task_migrated_per_successfull_deal)/len(list_avg_task_migrated_per_successfull_deal) ) + '\n'
    outputFile.write(out_string)

    out_string = 'Perc. success deal' + ' Min ' + str(min(list_perc_of_successfull_deals)) + ' Max ' + str(max(list_perc_of_successfull_deals)) + ' Avg ' + str(sum(list_perc_of_successfull_deals)/len(list_perc_of_successfull_deals) ) + '\n'
    outputFile.write(out_string)

    out_string = 'Evictions' + ' Min ' + str(min(list_total_evictions)) + ' Max ' + str(max(list_total_evictions)) + ' Avg ' + str(sum(list_total_evictions)/len(list_total_evictions) ) + '\n'
    outputFile.write(out_string)

    out_string = 'Stagein initiated' + ' Min ' + str(min(list_stage_in_initiated)) + ' Max ' + str(max(list_stage_in_initiated)) + ' Avg ' + str(sum(list_stage_in_initiated)/len(list_stage_in_initiated) ) + '\n'
    outputFile.write(out_string)

    out_string = 'Stagein required' + ' Min ' + str(min(list_stage_in_required)) + ' Max ' + str(max(list_stage_in_required)) + ' Avg ' + str(sum(list_stage_in_required)/len(list_stage_in_required) ) + '\n'
    outputFile.write(out_string)

    out_string = 'Perc. eviction per req. stagein' + ' Min ' + str(min(list_perc_eviction_for_stage_in_required)) + ' Max ' + str(max(list_perc_eviction_for_stage_in_required)) + ' Avg ' + str(sum(list_perc_eviction_for_stage_in_required)/len(list_perc_eviction_for_stage_in_required) ) + '\n'
    outputFile.write(out_string)
    
    out_string = 'Thrashing' + ' Min ' + str(min(list_thrashing)) + ' Max ' + str(max(list_thrashing)) + ' Avg ' + str(sum(list_thrashing)/len(list_thrashing) ) + '\n'
    outputFile.write(out_string)

    outputFile.close()



    
