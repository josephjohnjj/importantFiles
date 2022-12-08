#!/bin/bash

helpFunction()
{
   echo ""
   echo "Usage: $0 -a parameterA -b parameterB -c parameterC"
   echo -e "\t-a Description of what is parameterA"
   echo -e "\t-b Description of what is parameterB"
}

while getopts "d:r:" opt
do
   case "$opt" in
      d ) DEVICES="$OPTARG" ;;
      r ) RUNS="$OPTARG" ;;
      ? ) helpFunction ;; # Print helpFunction in case parameter is non-existent
   esac
done

# Print helpFunction in case parameters are empty
if [ -z "$DEVICES" ] || [ -z "$RUNS" ] 
then
   echo "Some or all of the parameters are empty";
   helpFunction
fi

# Begin script in case all parameters are correct
echo "Total devices: $DEVICES"
echo "Total runs per device: $RUNS"

for device in $(seq 1 $DEVICES)
do

        for run in $(seq 1 $RUNS)
        do
                filename="irrGEMM_$(date +%F)_device-$device"
                file_part2="_runs-$run.txt"
                filename+=$file_part2

                mpirun -np 1 ~/irr-gemm-gpu-over-parsec/build/src/testing_dgemm_irr_sparse -P 1 -Q 1 -M 20000 -N 800000 -K 20000 -m 100 -n 100 -k 100 -- --mca device_cuda_enabled $device --mca device_cuda_delegate_task_completion 0 &> $filename
                echo $filename
        done
done


