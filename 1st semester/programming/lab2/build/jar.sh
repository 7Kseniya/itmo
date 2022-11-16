#!bin/bash

javac -cp ".:../lib/Pokemon.jar" -d classes/ ../src/ru/ifmo/se/pokemon/*
jar cvmf MANIFEST.MF lab2.jar -C classes/ .

#компиляция
java -jar lab2.jar
