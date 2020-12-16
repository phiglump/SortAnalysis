for ((i=500; i<=10000; i+=500));
do
    python3 randomNums.py $i > ./testR/random_test_$i.txt
done
