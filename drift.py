import numpy as np

def calculate_drift(real, synthetic):
    drift_scores = {}

    for col in real.columns:
        if real[col].dtype != 'object':  # only numeric columns
            real_mean = np.mean(real[col])
            syn_mean = np.mean(synthetic[col])

            drift = abs(real_mean - syn_mean)
            drift_scores[col] = drift

    return drift_scores