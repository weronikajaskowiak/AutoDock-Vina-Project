# Protein-Ligand Docking and Virtual Screening Project

This project focuses on learning protein-ligand docking, conducting structure-based virtual screening (VS), and evaluating the quality of docking tools.

## Methods

### Redocking

1. **Preparation of Receptor and Ligand:**
   - Remove all ligands and water molecules from the receptor.
   - Add hydrogens to the receptor and ligand using PyMol.
   ```bash
   # Commands for preparation using AutoDockFR
   prepare_receptor -r receptor.pdb -o receptor_prepared.pdbqt
   prepare_ligand -l ligand.pdb -o ligand_prepared.pdbqt
   ```

2. **Grid Box Setup:**
   - Determine the center and dimensions (in Ångström) of the grid space around the experimentally bound ligand:
   ```bash
   # Example command to calculate the grid center
   python calculate_center.py
   ```
   - Set grid dimensions (usually 20 Å) based on the ligand size.
   - Save coordinates in `grid_box.txt`.

3. **Docking Simulation:**
   - Run AutoDock Vina with increased exhaustiveness (default 8, increased to 32 for better results):
   ```bash
   vina --receptor receptor_prepared.pdbqt \
        --ligand ligand_prepared.pdbqt \
        --config grid_box.txt \
        --exhaustiveness=32 \
        --out ligand_vina_output.pdbqt
   ```

4. **Assessment of Docking Results:**
   - Split Vina output into individual states and align them with the experimental structure in PyMol.
   - Calculate RMSD values to compare docking results with experimentally bound ligands.

### Virtual Screening

1. **Ligand and Decoy Preparation:**
   - Prepare ligands and decoys using Meeko:
   ```bash
   python mk_prepare_ligand.py -i file.sdf --multimol outdir_output_dir
   ```

2. **Running Virtual Screening:**
   - Use bash scripts for screening:
   ```bash
   bash run_ligands.sh
   bash run_decoys.sh
   ```

---

## Evaluation

### ROC Curve Analysis:
- **Purpose:** Assess the pose-prediction quality of the docking tool.
- **Process:**
  - Plot ROC curves using the `plot_roc.py` script.
  - Calculate the Area Under the Curve (AUC) to measure performance.
  
- **Key Concepts:**
  - **True Positives (TP):** Active compounds (ligands).
  - **False Positives (FP):** Inactive compounds (decoys).
  - **AUC Interpretation:** Represents the probability that the model assigns a higher score to a random positive observation than to a random negative one.

---
