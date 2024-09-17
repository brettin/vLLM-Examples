#!/usr/bin/perl

while(<>){
  print "$1\n" if /(Avg prompt throughput: \d+\.*\d* tokens\/s, Avg generation throughput: \d+\.*\d* tokens\/s, Running: \d+ reqs)/;
}
