import streamlit as st

# Data Governance Role Tab Column 1
def whatDataGov():
    st.write("")
    st.write("Data governance is the systematic management of an organization's data assets to ensure data quality, security, privacy, compliance, and usability while aligning with business objectives.")
    st.write("It has become increasingly important as organizations handle large volumes of data from various sources such as databases and policies")
    st.write("Key Components include: ")
    st.write("""
    - Data Quality:
        - Ensure accuracy, consistency, and reliability of data
        - Prevent poor outcomes from bad data

    - Security and Privacy:
        - Implement access controls to protect data
        - Use encryption 
        - Apply data masking (e.g., showing only the last four digits of credit card numbers)
        - Follow proper data disposal procedures

    - Compliance:
        - Ensure data handling adheres to relevant regulations
        - Reduce legal and regulatory risks

    - Usability:
        - Maintain data catalogs to document data availability and ownership
        - Use data dictionaries to define tables, columns, and measures
        - Track data lineage to trace the source of data
        - Implement metadata management tools for better data organization
    """)

# Data Governance Role Tab Column 2
def dataGovRR():
   st.write("""             
- **Data Governance Committee**:
  - Plans, implements, and manages the data governance program.
  - Develops policies and sets the strategic direction for data governance.
  - Advocates and communicates data governance initiatives across the organization.
  - Allocates resources (human and monetary) and monitors progress.
  - Manages change and risk related to data governance.
  - Composed of:
    - Data Governance Director (leader)
    - Data Stewards
    - Department Representatives (e.g., IT, Legal)
    - Data Governance Coordinator
    - Data Governance Analyst/Architect

- **Data Stewards**:
  - Responsible for applying data governance within different business units (e.g., sales, HR, finance).
  - Manage data domains (e.g., orders, leads, customers) and ensure proper data handling and policy application.

- **Data Owners**:
  - Own specific datasets and are responsible for supervising policies, approving security changes, and making decisions for their datasets.
  - Collaborate with the data governance committee to ensure policies are followed.

- **Other Roles Impacted by Data Governance**:
  - **IT Personnel**: Handle general security, storage, and data retention.
  - **Database Administrators**: Implement database-specific security measures such as encryption and masking policies.
  - **Business Knowledge Workers**: Interact with data regularly, ensuring its secure handling and providing feedback on data governance policies.""")
   
# DQ and MDM Tab Column 1
def dataGovDQ():
    st.write("""
    Components of Data Quality
- **Data Profiling**: 
  - Analyzes data to identify characteristics, patterns, and anomalies (e.g., duplication, inconsistencies).
  - Helps understand data and ensures alignment with expectations for improvement.

- **Data Validation**: 
  - Ensures data accuracy and completeness at the entry point (manual or automated).
  - Prevents errors from entering the system early.

- **Data Cleansing**: 
  - Corrects errors and removes duplicates.
  - Involves merging records or updating outdated information.

- **Data Completeness**: 
  - Addresses missing data by eliminating, annotating, or seeking additional information to maintain accuracy.

- **Data Documentation**: 
  - Includes data dictionaries, metadata, and lineage tracking.
  - Ensures clarity and helps resolve issues related to data origin and transformation.

- **Data Quality Monitoring**: 
  - Continuously evaluates data for accuracy, completeness, and consistency.
  - Uses automated tools to track anomalies and trends over time.
- **Data Governance**: 
  - Defines ownership, access permissions, and data management standards.
  - Ensures compliance, integrity, and security, especially in sensitive fields like healthcare.

**Impact of Poor Data Quality**:

- **Financial Losses**: 
  - Examples: 2008 financial crisis, a 2015 bank loss of 2.8 billion dollars, a US Airline losing 1 billion dollars due to overbooking.

- **Reputation Damage**: 
  - Inaccurate data can lead to bad decision-making, lost revenue, and damaged customer relationships.

- **Global Loss**: 
  - Poor data quality costs businesses an average of $15 million per year, impacting morale and opportunities.""")
    
#DQ and MDM Tab Column 2
def dataGovMDM():
    st.write("""
    Master Data Management is a comprehensive method of enabling an enterprise to link all of its critical data to one file, called a master file.
- **Best Practices**:
  - **Data Integration**: Combines data from different sources to ensure consistency.
  - **Data Stewardship**: Assigns responsibility for maintaining data quality and compliance.
  - **Data Quality Control**: Uses validation, cleansing, and monitoring to ensure accurate data.
  - **Data Governance**: Sets policies and rules for data management and access control.
  - **Master Data Modeling**: Standardizes key business data to align processes and systems.
  - **Data Security and Compliance**: Protects sensitive data and ensures regulatory compliance.
         
- **Impact of Poor MDM**:
  - **Operational Inefficiency**: Causes delays and redundant work.
  - **Increased Costs**: Leads to higher operational costs and resources spent fixing errors.
  - **Poor Customer Experience**: Affects service quality and customer retention.
  - **Regulatory Risks**: Non-compliance can result in legal consequences.
  - **Damaged Reputation**: Inconsistent data harms brand trust and customer loyalty.""")
