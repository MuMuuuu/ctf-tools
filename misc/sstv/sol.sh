#!/usr/bin/env bash

if [ "$1" == "" ]
then
	echo "./sol.sh [wav file]"
else
	qsstv &
	pactl load-module module-null-sink sink_name=virtual-cable
	pavucontrol &
	paplay -d virtual-cable "$1"
fi
