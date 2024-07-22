# %% [markdown]
# >> Test Analysis

# %% [markdown]
# > Importing Dependences

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# %%
# impoting the data

data = pd.read_excel(r'C:\Users\RIMNA KABEER\Downloads\Test.xlsx')
data.head()

# %%
# Data Understanding

data.info()

# %% [markdown]
# > Creating DataFrame Removing The Non values and  evaluvating DataFrame 

# %%
df_claim_type_amount = data[['Claim Type', 'Claim Amount']].dropna()

df_claim_type_amount.info()

# %% [markdown]
# > Most Insurance Providing Company

# %%
insurance_company_counts = data['Insurance Company'].value_counts()

# Plot the data
plt.figure(figsize=(10, 6))
insurance_company_counts.plot(kind='bar', color='skyblue')
plt.title('Number of Claims by Insurance Company')
plt.xlabel('Insurance Company')
plt.ylabel('Number of Claims')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

print(insurance_company_counts)


# %% [markdown]
# >>**insight**
# 
# **!Most insurance Providing Company New India Company**
# 
# **!Low Insurance Providing Companys ICICI Prudential, Medi Assit (Int), Zuno General**
# 
# **Low insurance Providing Companys are more Depending TPA Companys** 

# %% [markdown]
# > Claim Type Vs Claim Amount Visulization

# %%
# Calculate mean claim amount for each claim type
claim_type_amount_mean = df_claim_type_amount.groupby('Claim Type')['Claim Amount'].mean().reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(data=claim_type_amount_mean, x='Claim Type', y='Claim Amount')
plt.title('Claim Type vs Claim Amount')
plt.xticks(rotation=45)
plt.xlabel('Claim Type')
plt.ylabel('Average Claim Amount')
plt.show()

# %% [markdown]
# >>**insight**
# 
# **!High Claim Amount Is  Retierment Coverage Fund(RCT)**
# 
# **!Less Claim Amount Is Road Side Coverage Assistance(RCA)**
# 
# 

# %% [markdown]
# >Lender with the Most Funds Raised

# %%
lender_funds = data.groupby('Lender Name')['Set 1 Lender Re-Nach Amount'].sum()

# data Ploting
plt.figure(figsize=(10, 6))
lender_funds.plot(kind='bar', color='green')
plt.title('Funds Raised by Lender')
plt.xlabel('Lender')
plt.ylabel('Funds Raised')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

print(lender_funds)


# %% [markdown]
# >>**insight**
# 
# **!Most Found Raised Lender is Lender 1**
# 
# **!Lowest is Lender 2**

# %% [markdown]
# > Visulization Of TPA Companys

# %%
tpa_company_counts = data['TPA'].value_counts()

# Ploting the data
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
tpa_company_counts.plot(kind='bar', color='orange')
plt.title('Number of Claims by TPA Company')
plt.xlabel('TPA Company')
plt.ylabel('Number of Claims')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

print(tpa_company_counts)


# %% [markdown]
# >>**insight**
# 
# **!MediAssist is the most Insurnace Claims TPA Company**
# 
# **!Lowest ICICI Prudential, Geninus and Liberty**
# 
# **!MediAssist and star Insurance companys Mostlly depending TPA**

# %% [markdown]
# > Comparison of Insurance Companies and TPA Companies

# %%
# Combine counts for insurance companies and TPA companies
insurance_company_counts = data['Insurance Company'].value_counts()
combined_counts = pd.concat([insurance_company_counts, tpa_company_counts], axis=1, keys=['Insurance Company', 'TPA Company'])

# Ploting the combined data
combined_counts.plot(kind='bar', figsize=(14, 7), color=['skyblue', 'orange'])
plt.title('Comparison of Insurance Companies and TPA Companies')
plt.xlabel('Company')
plt.ylabel('Number of Claims')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# %% [markdown]
# >>**insight**
# 
# **We Can See here More TPA Depending companys**


