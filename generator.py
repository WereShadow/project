import pandas as pd
from sdv.single_table import CTGANSynthesizer
from sdv.metadata import SingleTableMetadata

def generate_synthetic_data(data):
    # Create metadata
    metadata = SingleTableMetadata()
    metadata.detect_from_dataframe(data)

    # Create model with metadata
    model = CTGANSynthesizer(metadata)

    # Train model
    model.fit(data)

    # Generate synthetic data
    synthetic_data = model.sample(len(data))

    return synthetic_data