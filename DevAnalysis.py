import pandas as pd

# Read the main survey data and schema data into Pandas DataFrames using relative paths
df = pd.read_csv('survey_results_public.csv')
schema_df = pd.read_csv('survey_results_schema.csv')

# Extract relevant columns from the main DataFrame
new_df = df.loc[:, ('Respondent', 'YearsCode', 'ConvertedComp', 'JobSat', 'WorkWeekHrs', 'WorkRemote',
                    'LanguageWorkedWith', 'Country')]

# Set 'Respondent' column as the index of the DataFrame
new_df.set_index('Respondent', inplace=True)

# Replace categorical values in 'JobSat' column with numerical values for analysis
new_df.JobSat.replace('Slightly satisfied', '0.75', inplace=True)
new_df.JobSat.replace('Very satisfied', '1', inplace=True)
new_df.JobSat.replace('Slightly dissatisfied', '0.25', inplace=True)
new_df.JobSat.replace('Very dissatisfied', '0', inplace=True)
new_df.JobSat.replace('Neither satisfied nor dissatisfied', '0.5', inplace=True)

# Rename 'JobSat' column to 'JobSatConverted' for clarity and convert it to float
new_df.rename(columns={'JobSat': 'JobSatConverted'}, inplace=True)
new_df.JobSatConverted = new_df.JobSatConverted.astype('float')

# Create binary columns indicating whether respondents work with Python and C#
new_df['WorksWithPython'] = new_df.LanguageWorkedWith
new_df.loc[new_df.WorksWithPython.str.contains('Python', na=False), 'WorksWithPython'] = True
new_df.loc[~new_df.WorksWithPython.str.contains('Python', na=True), 'WorksWithPython'] = False
new_df['WorksWithC#'] = new_df.LanguageWorkedWith
new_df.loc[new_df['WorksWithC#'].str.contains('C#', na=False), 'WorksWithC#'] = True
new_df.loc[~new_df['WorksWithC#'].str.contains('C#', na=True), 'WorksWithC#'] = False

# Display mean 'ConvertedComp' and 'JobSatConverted' for respondents working with Python
print(new_df.groupby('WorksWithPython').mean()[['ConvertedComp', 'JobSatConverted']])

# Display mean 'ConvertedComp' and 'JobSatConverted' for respondents working with C#
print(new_df.groupby('WorksWithC#').mean()[['ConvertedComp', 'JobSatConverted']])
