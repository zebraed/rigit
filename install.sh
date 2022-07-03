#!/bin/bash
which inkscape >/dev/null 2>&1
if [ ! $? -eq 0 ]; then
	echo "git is not installed. continue with setup..."
	
else
	echo "git is already installed. Ready to start RiGit!"
fi
