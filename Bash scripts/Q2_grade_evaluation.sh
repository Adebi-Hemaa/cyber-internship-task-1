#!/bin/bash

# Prompt user for numeric grade
echo "Enter a numeric grade (0-100): "
read grade

# Check if input is a valid number between 0 and 100
if [[ ! $grade =~ ^[0-9]+$ || $grade -lt 0 || $grade -gt 100 ]]; then
    echo "Error: Please enter a valid number between 0 and 100."
    exit 1
fi

# Determine letter grade
if [ $grade -ge 90 ]; then
    echo "Letter grade: A"
elif [ $grade -ge 80 ]; then
    echo "Letter grade: B"
elif [ $grade -ge 70 ]; then
    echo "Letter grade: C"
elif [ $grade -ge 60 ]; then
    echo "Letter grade: D"
else
    echo "Letter grade: F"
fi
