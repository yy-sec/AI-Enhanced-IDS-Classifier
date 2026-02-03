# AI-Enhanced-IDS-Classifier

## Project Overview
This project implements a flow-based Network Intrusion Detection System (NIDS) designed from a Blue Team / SOC perspective. The system analyzes network traffic flows extracted from PCAP data and applies machine learning techniques to distinguish between benign and malicious activity.
Currently, the system is optimized for Binary Classification, Future iterations will expand into Multi-class Classification to identify specific attack vectors.

## Dataset

This project uses the CIC-IDS2017 flow-based intrusion detection dataset.

Due to size constraints, the dataset is not included in this repository.
Instructions to download and prepare the data are provided in the `data/` directory.

## 📊 Performance Results (Binary Classification)

The model was evaluated on a test set of 565,576 samples from the CIC-IDS2017 dataset, yielding the following results:
| Metric | Score |
| --- | --- |
| **Accuracy** | **99.89%** |
| **Precision** | **99.53%** |
| **Recall** | **99.89%** |
| **F1-Score** | **99.71%** |







