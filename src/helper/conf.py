import time

"""
These are the configurations and sources. 
"""

time_of_run = time.strftime('_%Y_%m_%d_%H_%M')

# Raw data location:
TRAIN_VALUES_PATH = "./data/raw/train_values.csv"
TRAIN_LABELS_PATH = "./data/raw/train_labels.csv"
TEST_VALUES_PATH = "./data/raw/test_values.csv"

# Pre-processed data location:
encoded_string_col_path = "./data/processed/encoded_string_columns.csv"
encoded_int_col_path = "./data/processed/encoded_int_columns.csv"
encoded_data_path = "./data/processed/encoded_data.csv"

FITTED_MODEL_PATH = './models/model.pickle'

string_columns = [
    'geo_level_1_id',
    'geo_level_2_id',
    'geo_level_3_id',
    'foundation_type',
    'roof_type',
    'ground_floor_type',
    'plan_configuration',
    'legal_ownership_status'  # parameter has no effect
]

one_hot_columns = [
    'land_surface_condition',
    'roof_type',
    'other_floor_type',
    'position',
]

int_columns = [
    'count_floors_pre_eq', 
    'age',
    'area_percentage',
    'has_superstructure_adobe_mud',
    'has_superstructure_mud_mortar_stone',
    'has_superstructure_stone_flag',
    'has_superstructure_cement_mortar_stone',
    'has_superstructure_mud_mortar_brick',
    'has_superstructure_cement_mortar_brick',
    'has_superstructure_timber',
    'has_superstructure_bamboo',
    'has_superstructure_rc_non_engineered',
    'has_superstructure_rc_engineered', 
    'has_superstructure_other',
    'count_families',
    'has_secondary_use',
    'has_secondary_use_agriculture',
    'has_secondary_use_hotel',
    'has_secondary_use_rental',
    'has_secondary_use_institution',
    'has_secondary_use_school',
    'has_secondary_use_industry',
    'has_secondary_use_health_post',
    'has_secondary_use_gov_office',
    'has_secondary_use_use_police',
    'has_secondary_use_other'
]
