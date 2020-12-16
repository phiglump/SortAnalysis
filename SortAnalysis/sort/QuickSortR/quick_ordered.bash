for ((i=500; i<=10000; i+=500));
do
    python3 ordered.py $i > ./testO/ordered_test_$i.txt
done
