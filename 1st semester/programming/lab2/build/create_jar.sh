#!bin/bash

javac -cp ".:../lib/Pokemon.jar" -d classes/ ../src/ru/ifmo/se/pokemon/*
cat > MANIFEST.MF
Main-Class: ru.ifmo.se.pokemon.Main
Class-Path: ../lib/Pokemon.jar
jar cvmf MANIFEST.MF lab2.jar -C classes/ .
java -jar lab2.jar
