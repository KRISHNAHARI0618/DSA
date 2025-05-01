#!/bin/bash

date=$(date +%d-%m-%Y)
dates=$(date +%F)

echo "$dates"

validate(){
    # Validate will take input as first argument while calling 
    if [ $1 -ne 0 ]
    then
        echo "$3 Installation Is Failure"
    else
        echo "$3 Installation Is Success"
    fi

    if [ $2 -eq 1 ]
    then
        echo "The New Installation is There"
    else
        echo "The Error Installation is There"
    fi
}
rm -rf "$date".txt

apt install git -y &>> "$date".txt

validate $? 1 "Git"