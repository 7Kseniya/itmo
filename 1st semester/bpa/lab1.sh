#!/bin/bash

#1
mkdir lab0
cd lab0
mkdir -p ekans8/{claydol,grumpig,torterra}
touch armaldo3
echo "satk=7 sdef=8 spd=5" > armaldo3
touch bayleef6 pikachu1
echo -e "Ходы Body \nSlam Counter Cover Defence Curl Double-Edge Dynamicpuch Focus Punch \nHelping Hand Iron Tail Knock Off Magnet Rise Mega Kick Mega Punch Mud-Slap Rollout Seismic Toss Shock Wave Signal Beam Sleep Talk Shore \nSwift Thunderpunch Uproar" > pikachu1

mkdir -p gallade2/scythe
touch gallade2/{purloin,shinx}
echo -e "Способности Scratch Growl Assist \nSad-Attack Fury Swipes Pursuit Torment Fake Out Hone Claws Assurance \nSlash Captivate Night Slash Satch Nasty Plot Sucker \nPunch" > purloin
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
chmod u=rw,go=x gallade2/purloin
chmod 736 gallade2/scythe
chmod 006 gallade2/shinx
chmod 307 nidorino3
chmod u=wx,go=x nidorino3/shellder
chmod 046 nidorino3/leafeon
chmod 404 nidorino3/azurill
chmod 571 nidorino3/omanyte
chmod a=r pikachu1

ls -lR

echo "________________________________________________________"

#3
ln -s ../armaldo3 gallade2/purloinarmaldo
cat nidorino3/leafeon nidorino3/azurill > bayleef6_63
ln pikachu1 gallade2/purloinpikachu
cat bayleef6 > nidorino3/azurillbayleef
cp -r gallade2/ ekans8/torterra
ln -s ekans8 Copy_31
cp pikachu1 nidorino3/omanyte

ls -lR

echo "________________________________________________________"

#4
wc -m pikachu1>>pikachu1 2>/tmp/myerrors
ls -lR ./lab0/* 2>/dev/null | grep ^- | grep \ a| tail -3 | sort -r -k5
cat -n ekans8 2>/tmp/myerrors| grep Mu
ls -ltR ./lab0/* 2>/dev/null | grep ^- | grep \g | head -3 
ls -lR ./lab0/* | grep ^- | grep n$ | head -4 | sort -r -k2
ls -ulFR ./lab0/* 2>/dev/null | grep ^- | grep \ a | sort -r -k6

echo "________________________________________________________"

#5
rm -f bayleef6
rm -f gallade2/shinx
rm -f gallade2/purloinarmal*
rm -f gallade2/purloinpikac*
rm -rf gallade2
rm -rf ekans8/torterra

ls -lR
