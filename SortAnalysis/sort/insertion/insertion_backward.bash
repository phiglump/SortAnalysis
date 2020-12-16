for ((i=500; i<=10000; i+=500));
do
    python3 backward.py $i > ./testB/backward_test_$i.txt
done
