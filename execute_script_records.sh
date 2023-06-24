#!/bin/bash

input_folders_50k=(
    "Results/results_postgis_50k_1"
    "Results/results_postgis_50k_2"
    "Results/results_postgis_50k_3"
    "Results/results_mongodb_50k_1"
    "Results/results_mongodb_50k_2"
    "Results/results_mongodb_50k_3"
)

input_folders_100k=(
    "Results/results_postgis_100k_1"
    "Results/results_postgis_100k_2"
    "Results/results_postgis_100k_3"
    "Results/results_mongodb_100k_1"
    "Results/results_mongodb_100k_2"
    "Results/results_mongodb_100k_3"
)

input_folders_full=(
    "Results/results_postgis_full_1"
    "Results/results_postgis_full_2"
    "Results/results_postgis_full_3"
    "Results/results_mongodb_full_1"
    "Results/results_mongodb_full_2"
    "Results/results_mongodb_full_3"
)

output_folders_25vu=(
    "Plots/records/plots_postgis_25vus_1"
    "Plots/records/plots_postgis_25vus_2"
    "Plots/records/plots_postgis_25vus_3"
    "Plots/records/plots_mongodb_25vus_1"
    "Plots/records/plots_mongodb_25vus_2"
    "Plots/records/plots_mongodb_25vus_3"
)

output_folders_50vu=(
    "Plots/records/plots_postgis_50vus_1"
    "Plots/records/plots_postgis_50vus_2"
    "Plots/records/plots_postgis_50vus_3"
    "Plots/records/plots_mongodb_50vus_1"
    "Plots/records/plots_mongodb_50vus_2"
    "Plots/records/plots_mongodb_50vus_3"
)

output_folders_100vu=(
    "Plots/records/plots_postgis_100vus_1"
    "Plots/records/plots_postgis_100vus_2"
    "Plots/records/plots_postgis_100vus_3"
    "Plots/records/plots_mongodb_100vus_1"
    "Plots/records/plots_mongodb_100vus_2"
    "Plots/records/plots_mongodb_100vus_3"
)

output_folders_200vu=(
    "Plots/records/plots_postgis_200vus_1"
    "Plots/records/plots_postgis_200vus_2"
    "Plots/records/plots_postgis_200vus_3"
    "Plots/records/plots_mongodb_200vus_1"
    "Plots/records/plots_mongodb_200vus_2"
    "Plots/records/plots_mongodb_200vus_3"
)

for folder in "${output_folders_25vu[@]}"; do
    mkdir -p "$folder"
done

for folder in "${output_folders_50vu[@]}"; do
    mkdir -p "$folder"
done

for folder in "${output_folders_100vu[@]}"; do
    mkdir -p "$folder"
done

for folder in "${output_folders_200vu[@]}"; do
    mkdir -p "$folder"
done

for i in "${!input_folders_50k[@]}"; do
    input_folder_50k="${input_folders_50k[i]}"
    input_folder_100k="${input_folders_100k[i]}"
    input_folder_full="${input_folders_full[i]}"
    output_folder_25vu="${output_folders_25vu[i]}"
    output_folder_50vu="${output_folders_50vu[i]}"
    output_folder_100vu="${output_folders_100vu[i]}"
    output_folder_200vu="${output_folders_200vu[i]}"

    python3 load_testing_results_records.py "$input_folder_50k" "$input_folder_100k" "$input_folder_full" "$output_folder_50vu" "$output_folder_25vu" 50 25
    python3 load_testing_results_records.py "$input_folder_50k" "$input_folder_100k" "$input_folder_full" "$output_folder_100vu" "$output_folder_50vu" 100 50
    python3 load_testing_results_records.py "$input_folder_50k" "$input_folder_100k" "$input_folder_full" "$output_folder_200vu" "$output_folder_100vu" 200 100
done
