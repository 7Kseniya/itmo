#!bin/bash

javac -cp ".:../lib/Pokemon.jar(1)" -d classes/ ../src/ru/ifmo/se/*
jar cvmf MANIFEST.MF lab2.jar -C classes/ .
