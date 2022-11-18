#!/bin/bash

#1
mkdir lab0
cd lab0
mkdir -p ekans8/{claydol,grumpig,torterra}
touch armaldo3
echo "satk=7 sdef=8 spd=5" > armaldo3
touch bayleef6 pikachu1
echo -e "Ходы Body \nSlam Counter Cover Defence Curl Double-Edge Dynamicpuch Focus Punch \nHelping Hand Iron Tail Knock Off Magnet Rise Mega Kick Mega Punch Mud-Slap Rollout Seismic Toss Shock Wave Signal Beam Sleep Talk Shore \nSwift Thunderpunch Uproar" > pikachu1

mkdir -p ekans8/{claydol,grumpig,torterra}
mkdir -p gallade2/scythe
touch gallade2/{purrloin,shinx}
echo -e "Способности Scratch Growl Assist \nSad-Attack Fury Swipes Pursuit Torment Fake Out Hone Claws Assurance \nSlash Captivate Night Slash Satch Nasty Plot Sucker \nPunch" > purrloin
echo "Развитые способности Guts" > shinx


mkdir -p nidorino3/{shellder,omanyte}
touch nidorino3/{leafeon,azurill}
echo -e "Способноти \nSand-Attack Razor Leaf Quick Attack Grasswhistle Magical Leaf Giga \nDrain Swords Dance Synthesis Suny Day Last Resort Leaaf \nBlade" > leafeon
echo "weigth=4.4 height=8.0 def=4"c > azurill

ls -lR

echo "________________________________________________________"

#2

chmod 666 armaldo3
chmod 444 bayleef6
chmod 577 ekans8
chmod a=rwx  ekans8/claydol
chmod 307 ekans8/grumpig
chmod 355 ekans8/torterra
chmod 661 gallade2
chmod u=rw go=x gallade2/purrloin
chmod 736 gallade2/scythe
chmod 006 gallade2/shinx
chmod 307 nidorino3
chmod u=wx go=x nidorino3/shellder
chmod 046 nidorino3/leafeon
chmod 404 nidorino3/azurill
chmod 571 nidorino3/omanyte
chmod a=r pikachu1

ls -lR

echo "________________________________________________________"

#3

chmod -R 744 gallade2
ln -s ../armaldo3 gallade2/purrloinarmaldo

chmod 744 nidorino3/leafeon
chmod 744 nidorino3/azurill
cat nidorino3/leafeon nidorino3/azurill > bayleef6_63
ln pikachu1 gallade2/purrloinpikachu
cp bayleef6 nidorino3/azurillbayleef
chmod 046 nidorino3/leafeon
chmod 404 nidorino3/azurill

chmod 744 ekans8/torterra
cp -r gallade2/ ekans8/torterra
chmod 355 ekans8/torterra
chmod 736 gallade2/scythe
chmod 006 gallade2/shinx

chmod u+wx pikachu1
chmod u+w nidorino3/omanyte
ln -s ekans8 Copy_31
cp pikachu1 nidorino3/omanyte
chmod 571 nidorino3/omanyte
chmod a=r pikachu1 

ls -lR

echo "________________________________________________________"

#4
chmod 744 pikachu1
wc -m >>pikachu1 2>/tmp/myerrors
chmod a=r pikachu1
ls -lFR ./lab0/* 2>/dev/null | grep ^a | grep -v[@/] | tail -3 |  sort -rs 
cat -n ekans8 2>/tmp/myerrors| grep Mu |
ls -lFR ./lab0/* 2>/dev/null | grep g$ | grep -v[@/] | head -3 |  sort -k6
ls -lR ./lab0/* | grep n$ | grep -v[@/] | head -4 |  sort -r -k2
ls -ulFR ./lab0/* ./lab0/*/* ./lab0/*/*/* 2>/dev/null |  grep ^a | grep -v[@/] | sort -r -k6

echo "________________________________________________________"

#5
chmod 777 ./lab0/*
chmod 777 ./lab0/**/*

rm -f bayleef6
rm -f gallade2/shinx
rm -f gallade2/purrloinarmal*
rm -f gallade2/purrloinpikac*
rm -rf gallade2
rm -rf ekans8/torterra
