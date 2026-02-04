# AI-Enhanced-IDS-Classifier

## Project Overview
This project implements a flow-based Network Intrusion Detection System (NIDS) designed from a Blue Team / SOC perspective. The system analyzes network traffic flows extracted from PCAP data and applies machine learning techniques to distinguish between benign and malicious activity.
Currently, the system is optimized for Binary Classification, Future iterations will expand into Multi-class Classification to identify specific attack vectors.

## Objectives
•	Analyze network flow data derived from PCAP files

•	Clean and preprocess real-world cybersecurity datasets

•	Handle class imbalance common in intrusion detection datasets

•	Train and evaluate a machine learning model for attack detection


## Dataset

This project uses the CIC-IDS2017 flow-based intrusion detection dataset.

Due to size constraints, the dataset is not included in this repository.
Instructions to download and prepare the data are provided in the `data/` directory.

## Workflow
### 1.	Data Exploration
o	Analyze distributions and class imbalance
o	Identify missing and invalid values
### 2.	Data Cleaning & Preprocessing
o	Remove NaN and empty values
o	Drop unnecessary index columns
o	Scale numerical features
### 3.	Label Engineering
o	Convert multi-class labels into binary labels
### 4.	Model Training
o	Train a binary classification ML model
o	Save trained model and preprocessing objects
### 5.	Evaluation
o	Confusion matrix
o	Performance metrics









