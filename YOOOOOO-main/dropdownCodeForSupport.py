import streamlit as st
def dropdownAnswers():
    col1,col2 = st.columns(2)
    with col1:
            choice = st.selectbox("Overview Questions: ", [
            " ",
            "Why Collibra?",
            "How can my department benefit from Collibra?",
            "What are the high-level capabilities of Collibra?",
            "What can Collibra Catalog do for my team?",
            "How can Collibra help with reporting needs?",
            "How much time will Collibra take away from my team?",
            ])

            if choice == "Why Collibra?":
                st.write("Collibra is the Aflac adopted Enterprise Data Governance Center platform selected due to its capabilities and functionality, and the ease of use for our data steward community.")
            
            if choice == "How can my department benefit from Collibra?":
                st.write("Collibra maintains your department’s metadata about your data in its catalog. This collection of data is maintained and vetted by your team’s Data Steward(s). "
               "Your Data Steward(s), working with the DGC team, also identify and link reverential data (business glossary of terms and descriptions where available) so that you can identify and use the correct asset in your reports."
                "Your Data Steward(s) also get a data quality report that identifies assets that have errors, allowing them to correct that data at the source."
                "The metadata also identifies the assets that are classified (PII, PHI) as well as provide a section for tagging assets that have special meaning to your department.")
            
            if choice == "What are the high-level capabilities of Collibra?":
                st.write("Collibra is the Aflac adopted Enterprise Data Governance Center platform selected due to its capabilities and functionality, and the ease of use for our data steward community.")
            
            if choice == "What can Collibra Catalog do for my team?":
                st.write("Collibra is a centralized catalog of data assets with key characteristics that can make discovering, accessing, and interacting with data easier for end users."
                "It also acts as a business glossary of terms that provide context to the technical data. By offering these, Collibra streamlines the process for data access and distribution")

            if choice == "How can Collibra help with reporting needs?":
                st.write("For reporting, Collibra acts as a one-stop shop for finding information to include: ")
                st.write("o Catalog of reports with their characteristics and related workbooks, worksheets, views, etc.")
                st.write("o Repository of the key KPIs and metrics with their descriptions and calculation formulas")
                st.write("o End-to-end data lineage with data flow from the primary data source to the report and data transformation")
                st.write("o Configured roles and responsibilities and automated report certification processes ")

            if choice == "How much time will Collibra take away from my team?":
                st.write("Below is a breakdown of the roles that may require some time commitments. These are estimates that reflect the amount of activity for a newly engaged business area."
                "Time commitments are typically lower for well-established business areas. It is a best practice to validate business terms, reports, and metrics on an annual basis. This is an automated process within Collibra that is easier than manual validation.")
                st.write("o Data Stewards ~ 15% weekly")
                st.write("o Data Owners ~ 5% monthly")
                st.write("o Technical Stewards ~ 15% weekly")


            choice = st.selectbox("Technical Questions: ",[
            " ",
            "How do the search functions work?",
            "How is my team’s data imported into Collibra?",
            "What are the methods of ingestion?",
            "Who's managing my team’s data?",
            "How secure is Collibra?"
            "What are my options for user group permissions? (Roles & Responsibilities)",
            "What is the difference between Asset level permissions and Domain level permissions?",
            "Why is Lineage important to my data?",
            "Lineage Vs Traceability",
            "What does Reference Data help us see?",
            "Is there a way to make bulk changes in Collibra?",
            "How do I use workflows in Collibra?",
            "What asset types are available to us?",
            "How is the data in Collibra maintained?"
            ])

            if choice == "How do the search functions work?":
                st.write("There are multiple ways to find your data. You can use the search or the global search box which help to find the resources. You can also use data marketplace to search for the data.")
            
            if choice == "How is my team’s data imported into Collibra?":
                st.write("Data can be imported in several ways, depending on what data is being ingested. Our Business Glossary was imported via Excel files initially based on data collected from our business partners, but additional data has been added through the Collibra platform."
                "Metadata and Data Lineage is imported via ‘connectors’ so data from our source systems is brought into Collibra automatically and refreshed through AutoSys scheduled jobs and internal Collibra workflows to ensure data is accurate and up to date.")

            if choice == "What are the methods of ingestion?":
                st.write("Metadata can be ingested into Collibra using multiple types of Edge connections. We select from the appropriate available connections such as JDBC, Rest APIs, SSIS, proprietary custom methods, etc")
            
            if choice == "Who's managing my team’s data?":
                st.write("You do! We are all champions of our data and the responsibility for maintaining the data is with each business unit. Data Owners and Data Stewards are identified across the enterprise, but anyone in the business can help maintain the integrity of the data."
                 "Simple workflows for connecting with us through Collibra to make suggested changes makes")
            
            if choice == "How secure is Collibra?":
                st.write("Collibra is accessed through Single Sign On (SSO) which is very secure and standard for accessing Aflac applications."
                "SSO allows us to effectively limit access if an employee is no longer ith the company, but the Data Governance team also manages the list of active employees to ensure we manually remove a user from Collibra as needed")
            
            if choice == "What are my options for user group permissions? (Roles & Responsibilities)":
                st.write("Everyone has access to view in Collibra, others are placed in a corresponding user group according to their roles – for instance, Claims Data Steward – those identified as a Data Steward in Claims would be part of this user group."
                         "Any user who will participate in a Workflow for approving or managing assets are placed in a user group. We have a limited number of licenses in Collibra, so those are assigned as needed for individuals who will be participating in a workflow task or responsible for creating connections to their data.")
            
            if choice == "What is the difference between Asset level permissions and Domain level permissions?":
                st.write(" Permission is the right to see a resource of any child of that resource including assets as inherited permissions. If the user has domain level permissions, then they can see the assets in that domain. The permission can be assigned on domain or community level to users and groups."
                         " If the user is added as an owner of the domain but if the user doesn’t have the view permission, then the user cannot see the asset or act on her responsibility like workflows")
            
            if choice == "Why is Lineage important to my data?":
                st.write(" Lineage is important because it allows us to not only see sample data within a database, but it allows us to see how data moves between the source database and downstream locations."
                         " This allows for a more thorough impact assessment prior to making changes to a specific data element in an application. Benefits include:")
                st.write("▪ Data Quality – Understand data origins, transformations, and processing.") 
                st.write("▪ Transparency – Visualize data flow, relationships, dependencies, and processing across its entire lifecycle.")
                st.write("▪ Regulatory compliance – Meet data governance requirements ")
                st.write("▪ Decision Making – Make informed decisions with accurate data")
                st.write("▪ Risk Management – Identify potential data errors and anomalies")
                st.write("▪ Data Governance – Establish accountability and ownership")
                st.write("▪ Troubleshooting data issues, auditing data changes, migrating data systems.")
            
            if choice == "Lineage Vs Traceability":
                st.write("• Traceability refers to the ability to track data changes, updates or deletion across systems ensuring accountability and auditing ")
                st.write("• Lineage focuses on the data’s origin, processing history and transformations. It shows how tables and columns are used and how they relate to each other.")
            
            if choice == "What does Reference Data help us see?":
                st.write("Reference data helps identifies the code values that are a part of a code set that is allowed/populated in a specific field." 
                         "In the example below, ‘5’ is a code value that is a part of the ‘Account Termination Reason’ code set. Each code value represents a different business term/reason." 
                         "Collibra helps identify and link these relationships and provides allthe values in one place. ")
            
            if choice == "Is there a way to make bulk changes in Collibra?":
                st.write("This is a feature within Collibra that can be used to mass import/export resources into a specific community. It requires that you have a global role. You will need assistance from the Data Governance Team to use this feature."
                "By default, the exported file type is Excel, but you can change it to CSV.")

            if choice == "How do I use workflows in Collibra":
                st.write("Workflows are actions within Collibra used to trigger certain activities. There are workflows that streamline processes within the system."
                         "For example, there is a workflow that the Data Governance Team uses to trigger the annual validation process for the Data Stewards. Please reach out to the Data Governance Office if you would like to have a specific workflow created.")

            if choice == "What asset types are available to us?":
                st.write("• There are 5 asset types that are used in Collibra:")
                st.write("1. Business Assets - A type of asset that is exclusively used and governed by the business user community (Ex: Acronyms, Business Terms, KPIs, Metrics, Reports, etc.)")
                st.write("2. Data Assets - A type of asset that represents details of organizational data in two layers. One layer is independent of any technology for non-technical stakeholder communication." 
                         "The other one is taking the implementation system for technical stakeholder communication into account. (Ex: Code Sets, Columns, Report Attributes, etc.)")
                
            if choice == "How is the data in Collibra maintained?":
                st.write("• Business glossaries are maintained by the Data Stewards through ongoing maintenance and the annual validation process")
                st.write("• Metadata is ingested into Collibra from the data source and is not modified. The data is pulled in to show what is available, where it lives, its relationships to other data elements, and who owns it.")
            
            choice = st.selectbox("Contacting Collibra: ",[
            " ",
            "Who's the point of contact for Collibra?",
            "What are the requirements for onboarding my team into Collibra?",
            "User Guide Items: "
        ])
            
            if choice == "Who's the point of contact for Collibra?":
                st.write("DataGovernance@aflac.com")
            
            if choice == "What are the requirements for onboarding my team into Collibra?":
                st.write(" For business glossaries:")
                st.write("o Reach out to the Data Governance Office for a demo")
                st.write("For data sources/technical lineage:")
                st.write("o System permissions – read access to metadata")
                st.write("o Service Account access (via the IAM Team)")
                st.write("o Database Type (where is the data hosted)")
                st.write("• Getting Started in Collibra E-learning Courses (Link in Resources)")
            
            if choice == "User Guide Items: ":
                st.write("Workflows in Collibra allow you to define the process, steps in Business Process Modeling & Notation (BPMN) standards to get work done from start to finish while at the same time defining ownership of every individual step." 
                         "It allows users to complete tasks in a guided and controlled way. (LS)")
                st.write("Collibra Navigation Tips & Tricks (More info on Collibra Link)")

        