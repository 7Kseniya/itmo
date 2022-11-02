#!bin/bash

javac -cp ".:../lib/Pokemon.jar(1)" -d classes/ ../src/ru/ifmo/se/pokemon/*
jar cvmf MANIFEST.MF lab2.jar -C classes/ .
