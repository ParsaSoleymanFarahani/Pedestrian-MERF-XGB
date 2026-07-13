import numpy as np
import pandas as pd
import os

def generate_synthetic_data(output_path):
    np.random.seed(42)
    n_samples = 199

    # 1. Generate clustering levels
    cities = ['detroit', 'ann-arbor', 'flint', 'novi', 'stockbridge']
    city_weights = [116/199, 58/199, 15/199, 9/199, 1/199]
    location = np.random.choice(cities, size=n_samples, p=city_weights)

    years = [2019, 2020, 2021, 2022]
    year_weights = [55/199, 66/199, 62/199, 16/199]
    year = np.random.choice(years, size=n_samples, p=year_weights)

    # 2. Generate predictors based on their actual ranges
    strava_madt = np.random.exponential(scale=10.0, size=n_samples)
    strava_madt = np.clip(strava_madt, 0.0, 48.89)

    bik_den = np.random.exponential(scale=10.0, size=n_samples)
    # add some zeros to mimic zero inflation
    bik_den[np.random.rand(n_samples) > 0.6] = 0.0
    bik_den = np.clip(bik_den, 0.0, 71.32)

    slope = np.random.gamma(shape=1.5, scale=0.4, size=n_samples)
    slope = np.clip(slope, 0.0, 3.34)

    distcolleg = np.random.uniform(150.0, 118762.2, size=n_samples)

    bik_pct = np.random.exponential(scale=1.0, size=n_samples)
    bik_pct = np.clip(bik_pct, 0.0, 7.36)

    ret_area = np.random.uniform(0.0, 1104941.0, size=n_samples)
    # add some zeros to mimic zero inflation
    ret_area[np.random.rand(n_samples) > 0.8] = 0.0

    afam = np.random.uniform(0.0, 56.50, size=n_samples)

    prec = np.random.uniform(0.05, 0.18, size=n_samples)

    hh_den = np.random.exponential(scale=500.0, size=n_samples) + 54.77
    hh_den = np.clip(hh_den, 54.77, 3830.06)

    hum = np.random.uniform(54.47, 75.31, size=n_samples)

    med_age = np.random.normal(loc=40.07, scale=7.93, size=n_samples)
    med_age = np.clip(med_age, 21.51, 52.16)

    # 3. Define random effects
    city_effects = {
        'detroit': 40.0,
        'ann-arbor': 120.0,
        'flint': -50.0,
        'novi': -10.0,
        'stockbridge': -80.0
    }
    year_effects = {
        2019: 15.0,
        2020: -30.0,
        2021: 25.0,
        2022: -10.0
    }

    # 4. Generate target variable (pedestrian count) using features + random effects + noise
    # We build a realistic relationship: Strava_MADT is the main predictor
    ped_count = (
        80.0 
        + 18.5 * strava_madt 
        + 1.5 * bik_den 
        + 8.0 * bik_pct 
        + 0.04 * hh_den
        - 1.2 * afam
        + np.array([city_effects[c] for c in location])
        + np.array([year_effects[y] for y in year])
        + np.random.normal(loc=0.0, scale=35.0, size=n_samples)
    )
    # Pedestrian count must be positive
    ped_count = np.clip(ped_count, 5.09, 1319.76)

    # 5. Create DataFrame
    df = pd.DataFrame({
        'location': location,
        'Year': year,
        'Strava_MADT': strava_madt,
        'bik_den': bik_den,
        'slope': slope,
        'distcolleg': distcolleg,
        'bik_pct': bik_pct,
        'ret_area': ret_area,
        'afam': afam,
        'prec': prec,
        'hh_den': hh_den,
        'hum': hum,
        'med_age': med_age,
        'Pedestrian_Count_Average_MADT': ped_count
    })

    # Save to Excel
    df.to_excel(output_path, sheet_name='Pedestrian Counters', index=False)
    print(f"Synthetic dataset saved successfully to: {output_path}")

if __name__ == "__main__":
    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(output_dir, "MDOT_Synthetic_Data.xlsx")
    generate_synthetic_data(output_file)
