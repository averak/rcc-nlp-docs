#!/usr/bin/env bash

mkdir -p data
cd data

a_year=("2015" "2016" "2017" "2018" "2019")
for year in ${a_year[@]}; do
  git clone "https://gitlab.com/ritscc/soukai/${year}/soukai-${year}-1"
  git clone "https://gitlab.com/ritscc/soukai/${year}/soukai-${year}-2"
done

cd -
