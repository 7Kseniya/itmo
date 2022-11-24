#!bin/bash

javac -cp "src:lib/Pokemon.jar" -d classes/ ../src/ru/ifmo/se/*
cp -R lib/ build/
cat > MANIFEST.mf
echo "Main-Class: ru.ifmo.se.pokemon.Main
Class-Path: ../lib/Pokemon.jar
" > MANIFEST.MF
jar cvmf MANIFEST.MF lab2.jar -C classes/ .
java -jar lab2.jar
