☁️ Cloud Resource Utilization & Cost Analytics Platform

An end-to-end cloud resource utilization and cost analytics platform that combines Python ETL, SQL-based analysis, AWS RDS PostgreSQL, Docker, and Grafana to identify resource inefficiencies and potential cloud cost optimization opportunities.

The project processes multi-cloud infrastructure data, engineers utilization and cost metrics, stores the cleaned dataset in PostgreSQL, and presents analytical insights through an interactive Grafana dashboard.

---

🚀 Project Overview

Cloud environments can contain resources that are over-provisioned, underutilized, or generating unnecessary costs.

This project analyzes infrastructure-level metrics such as:

- CPU utilization
- Memory utilization
- Network I/O
- Disk I/O
- VM type
- vCPU and RAM allocation
- Cloud provider
- Region
- Hourly pricing
- Resource cost
- Utilization
- Latency
- Throughput

The pipeline transforms raw infrastructure data into actionable indicators such as:

- Cost per vCPU
- Cost per GB of RAM
- High CPU usage
- High memory usage
- Underutilized resources
- Expensive VM resources

---

🏗️ Architecture

                    ┌──────────────────┐
                    │      Kaggle      │
                    │  Multi-Cloud     │
                    │     Dataset      │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   extract.py    │
                    │  KaggleHub API   │
                    └────────┬─────────┘
                             │
                             ▼
                       Raw CSV Data
                             │
                             ▼
                    ┌──────────────────┐
                    │  transform.py   │
                    │ Pandas ETL       │
                    └────────┬─────────┘
                             │
                             ▼
                     Cleaned CSV Data
                             │
                             ▼
                    ┌──────────────────┐
                    │     load.py     │
                    │ SQLAlchemy       │
                    └────────┬─────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │   AWS RDS           │
                  │ PostgreSQL          │
                  └─────────┬───────────┘
                            │
                            ▼
                  ┌─────────────────────┐
                  │    SQL Analysis     │
                  │ Views & Queries     │
                  └─────────┬───────────┘
                            │
                            ▼
                  ┌─────────────────────┐
                  │      Grafana        │
                  │ Interactive         │
                  │ Dashboard           │
                  └─────────────────────┘

                    🐳 Docker
              Containerized ETL Pipeline

---

🛠️ Technology Stack

Category| Technologies
Programming| Python
Data Processing| Pandas
Data Source| Kaggle / KaggleHub
Database| PostgreSQL
Cloud Database| AWS RDS
Database Access| SQLAlchemy, psycopg2
Analytics| SQL
Visualization| Grafana
Containerization| Docker
Configuration| python-dotenv
Version Control| Git / GitHub

---

📁 Project Structure

Cloud Resource Utilization and Cost Analytics Platform/
│
├── data/
│   ├── raw/
│   │   └── Cloud_Dataset.csv
│   └── processed/
│       └── cloud_dataset__cleaned.csv
│
├── grafana/
│   ├── screenshots/
│   │   ├── dashboard_overviews(1-4).png
│   │   └── dashboard_overviews(5-8).png
│   ├── dashboard.json
│   └── panel_queries
│
├── sql/
│   ├── 01_exploration.psql
│   ├── 02_views.psql
│   ├── 03_queries.psql
│   ├── 04_cost_optimization.psql
│   └── 05_analysis.psql
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── db_connection.py
│
├── .env
├── .env.example
├── .gitignore
├── .dockerignore
├── requirements.txt
├── Dockerfile
└── README.md

---

🔄 ETL Pipeline

1. Extract

"extract.py" downloads the latest version of the multi-cloud resource dataset using KaggleHub and stores the raw data under:

data/raw/

2. Transform

"transform.py" performs the following data-cleaning operations:

- Inspects the dataset
- Removes duplicate records
- Handles missing values
- Converts columns to appropriate data types
- Standardizes text fields
- Removes invalid CPU and memory values
- Removes invalid utilization values
- Removes negative resource metrics
- Performs feature engineering

Feature Engineering

The pipeline creates:

cost_per_vCPU
cost_per_RAM
High_cpu
high_memory
underutilized

These features support the project's cost and resource utilization analysis.

3. Load

"load.py" loads the processed dataset into the "cloud_data" table in AWS RDS PostgreSQL.

The pipeline uses environment variables for database credentials instead of storing credentials directly in the source code.

The loading process preserves existing database views by clearing existing table rows and appending the refreshed dataset rather than dropping and recreating the table.

---

🗄️ SQL Analysis

The SQL layer is organized into separate stages:

"01_exploration.psql"

Initial exploration and understanding of the dataset.

"02_views.psql"

Creates reusable analytical views, including:

- "underutilized_vms"
- "expensive_vms"

"03_queries.psql"

Performs analytical queries against the cloud resource dataset.

"04_cost_optimization.psql"

Identifies potential cost optimization opportunities based on resource utilization and pricing.

"05_analysis.psql"

Contains final analytical queries and reporting logic.

---

📊 Grafana Dashboard

Grafana is used to visualize cloud resource utilization and cost insights from PostgreSQL.

The dashboard includes visualizations for areas such as:

- Resource utilization
- CPU and memory usage
- Cloud provider distribution
- VM cost
- Underutilized resources
- Expensive resources
- Cost efficiency
- Resource performance

The repository includes:

grafana/dashboard.json

which can be imported into Grafana to recreate the dashboard.

Dashboard screenshots are available under:

grafana/screenshots/

---

🐳 Dockerization

The complete Python ETL pipeline has been containerized using Docker.

The Docker container runs:

extract.py
    ↓
transform.py
    ↓
load.py

The container can therefore reproduce the complete data-ingestion workflow without requiring the user to manually execute each ETL stage.

Build the Docker Image

docker build -t cloud-resource-analytics .

Run the Complete ETL Pipeline

docker run --rm --env-file .env cloud-resource-analytics sh -c "python src/extract.py && python src/transform.py && python src/load.py"

Database credentials are supplied through ".env" and are excluded from version control.

---

🔐 Environment Variables

Create a local ".env" file:

db_host=your-rds-endpoint
db_port=5432
db_name=postgres
db_user=your-db-user
db_password=your-db-password

Never commit ".env" to GitHub.

Use ".env.example" as a template for required configuration.

---

⚠️ AWS Network Configuration — Development Limitation

During development, the AWS RDS security configuration used an inbound rule allowing:

0.0.0.0/0

This was used to allow connectivity while testing from changing networks and environments.

Security Consideration

"0.0.0.0/0" allows connections from any IPv4 address and should not be used as a production configuration.

Before production deployment, the RDS security group should be restricted to trusted sources, such as:

- A specific application/server security group
- A fixed trusted IP address
- A private VPC connection
- Another controlled network path

The development configuration is documented here for transparency and reproducibility.

---

🔒 Security

Sensitive configuration is intentionally excluded from the repository.

The project uses:

.env
.env.example
.gitignore
.dockerignore

Database credentials are loaded through environment variables rather than hardcoded into the application.

Before publishing the repository, all credentials and secrets should be verified to ensure that no sensitive information is present in Git history.

---

▶️ Running the Project

Local Python Execution

Install dependencies:

pip install -r requirements.txt

Run the ETL pipeline:

python src/extract.py
python src/transform.py
python src/load.py

Docker Execution

Build:

docker build -t cloud-resource-analytics .

Run:

docker run --rm --env-file .env cloud-resource-analytics sh -c "python src/extract.py && python src/transform.py && python src/load.py"

---

📈 Key Analytical Questions

The project focuses on questions such as:

- Which cloud resources are underutilized?
- Which VMs have unusually high costs?
- Which resources have high CPU or memory usage?
- How does cost vary across cloud providers?
- Which VM configurations provide better cost efficiency?
- What resources could potentially be rightsized?
- How can utilization metrics be used to identify cost-saving opportunities?

---

🎯 Project Goals

This project demonstrates practical experience with:

- End-to-end ETL development
- Data cleaning and preprocessing
- Feature engineering
- SQL analytics
- PostgreSQL
- AWS cloud services
- Cloud resource and cost analysis
- Dashboard development
- Docker containerization
- Environment-based configuration
- Reproducible data pipelines

---

🚀 Future Improvements

Potential future improvements include:

- Restricting AWS RDS network access
- Automating ETL execution
- Adding CI/CD using GitHub Actions
- Adding automated data-quality tests
- Scheduling recurring data ingestion
- Infrastructure-as-Code using Terraform
- Container orchestration
- Monitoring and alerting
- Automated cloud cost recommendations

---

👩‍💻 Author

Archana Jayesh Pathak

Computer Science & Engineering | Data Analytics | Cloud & DevOps

Core Technologies

"Python" "SQL" "PostgreSQL" "AWS" "Docker" "Grafana" "Pandas" "Git"