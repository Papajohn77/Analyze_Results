#!/bin/bash

input_folders=(
    "Results/results_postgis_50k_1"
    "Results/results_postgis_50k_2"
    "Results/results_postgis_50k_3"
    "Results/results_postgis_100k_1"
    "Results/results_postgis_100k_2"
    "Results/results_postgis_100k_3"
    "Results/results_postgis_full_1"
    "Results/results_postgis_full_2"
    "Results/results_postgis_full_3"
    "Results/results_mongodb_50k_1"
    "Results/results_mongodb_50k_2"
    "Results/results_mongodb_50k_3"
    "Results/results_mongodb_100k_1"
    "Results/results_mongodb_100k_2"
    "Results/results_mongodb_100k_3"
    "Results/results_mongodb_full_1"
    "Results/results_mongodb_full_2"
    "Results/results_mongodb_full_3"
)

output_folders=(
    "Plots/vus/plots_postgis_50k_1"
    "Plots/vus/plots_postgis_50k_2"
    "Plots/vus/plots_postgis_50k_3"
    "Plots/vus/plots_postgis_100k_1"
    "Plots/vus/plots_postgis_100k_2"
    "Plots/vus/plots_postgis_100k_3"
    "Plots/vus/plots_postgis_full_1"
    "Plots/vus/plots_postgis_full_2"
    "Plots/vus/plots_postgis_full_3"
    "Plots/vus/plots_mongodb_50k_1"
    "Plots/vus/plots_mongodb_50k_2"
    "Plots/vus/plots_mongodb_50k_3"
    "Plots/vus/plots_mongodb_100k_1"
    "Plots/vus/plots_mongodb_100k_2"
    "Plots/vus/plots_mongodb_100k_3"
    "Plots/vus/plots_mongodb_full_1"
    "Plots/vus/plots_mongodb_full_2"
    "Plots/vus/plots_mongodb_full_3"
)

for folder in "${output_folders[@]}"; do
    mkdir -p "$folder"
done

for i in "${!input_folders[@]}"; do
    input_folder="${input_folders[i]}"
    output_folder="${output_folders[i]}"
    python3 load_testing_results_vus.py "$input_folder" "$output_folder"
done
