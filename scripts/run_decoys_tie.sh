#!/bin/bash

# Create the output directory for Vina docking results if it doesn't exist
mkdir -p vina_outputs_decoys_tie
mkdir -p vina_console_output_decoys_tie

# Define the receptor and config file
RECEPTOR="2oo8_receptor_prepared.pdbqt"
CONFIG="grid_box_tie.txt"
EXHAUSTIVENESS=32

# Loop through each ligand file in the output_ligands directory
for LIGAND in output_decoys_tie/*.pdbqt; do
  # Check if there are no matching files
  if [ ! -e "$LIGAND" ]; then
    echo "No ligand files found in the output_ligands directory."
    break
  fi
  
  # Extract the base name of the ligand file (without extension)
  BASENAME=$(basename "$LIGAND" .pdbqt)
  
  # Define the output file name in the vina_outputs directory
  OUTPUT="vina_outputs_decoys_tie/${BASENAME}_vina_output.pdbqt"
  
  # Run the vina command
  vina --receptor "$RECEPTOR" --ligand "$LIGAND" --config "$CONFIG" --exhaustiveness="$EXHAUSTIVENESS" --out "$OUTPUT" > vina_console_output_decoys_tie/${BASENAME}_energy.txt
  
  # Check if vina command was successful
  if [ $? -eq 0 ]; then
    echo "Vina docking for $LIGAND completed successfully."
  else
    echo "Vina docking for $LIGAND failed."
  fi
done
