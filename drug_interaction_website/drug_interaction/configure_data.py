import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the paths to your CSV files
atc_agent_csv = os.path.join(BASE_DIR, '/Users/Abdullah_Elgabry/Desktop/Drug_interaction/drug_interaction_website/drug_interaction/DrugBankParse/agent-productname.csv', 'atc-agent.csv')
atc_productname_csv = os.path.join(BASE_DIR, '/Users/Abdullah_Elgabry/Desktop/Drug_interaction/drug_interaction_website/drug_interaction/DrugBankParse/agent-productname.csv', 'atc-productname.csv')
agent_productname_csv = os.path.join(BASE_DIR, '/Users/Abdullah_Elgabry/Desktop/Drug_interaction/drug_interaction_website/drug_interaction/DrugBankParse/agent-productname.csv', 'agent-productname.csv')