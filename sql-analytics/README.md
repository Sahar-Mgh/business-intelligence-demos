# 🗄️ SQL Analytics Examples for Business Intelligence

**Advanced SQL query demonstrations for data warehouse optimization and BI dashboard development**

![SQL](https://img.shields.io/badge/SQL-Advanced-blue)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Database](https://img.shields.io/badge/Database-SQLite-green)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success)

---

## 🎯 **Project Overview**

This project demonstrates advanced SQL analytics capabilities through comprehensive business intelligence queries. Built to showcase expertise in complex data warehouse analysis, financial KPI calculations, and customer behavior analytics using production-quality SQL patterns.

**Key Learning**: *Good BI queries balance performance with readability - CTEs make complex logic maintainable and testable in production environments.*

---

## ✨ **Features**

### 📊 **Revenue Dashboard Analytics**
- Monthly revenue analysis with period-over-period growth calculations
- Subscription tier performance breakdown and comparison
- Window functions for trend analysis and forecasting
- Executive-level financial KPI tracking

### 🎯 **Customer Segmentation Analysis**
- Multi-dimensional customer behavioral analysis using CTEs
- Value-based segmentation with lifecycle stage classification
- Behavioral pattern recognition for targeted marketing
- Customer concentration analysis for business strategy

### ⚡ **Usage Optimization Queries**
- System performance analysis for infrastructure planning
- Peak vs average usage analysis for capacity planning
- Load variability calculations for cost optimization
- Day-of-week patterns for resource allocation

### 🚨 **Churn Risk Analysis**
- Multi-factor risk scoring combining behavioral signals
- Customer health monitoring with actionable risk categories
- Revenue-at-risk calculations for business impact assessment
- Intervention prioritization based on customer value

### 💰 **Financial KPI Dashboard**
- Executive-level financial metrics with growth analysis
- Revenue mix analysis and trend identification
- ARPU (Average Revenue Per User) calculations
- Customer acquisition and retention metrics

---

## 🛠️ **Technology Stack**

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Database** | SQLite | In-memory database for demonstrations |
| **Query Engine** | SQL (ANSI Standard) | Advanced analytics and aggregations |
| **Data Processing** | Pandas | Result analysis and presentation |
| **Sample Data** | NumPy | Realistic business data generation |
| **Framework** | Python 3.8+ | Application logic and execution |

---

## 🚀 **Quick Start**

### Prerequisites
```bash
Python 3.8 or higher
pandas library
numpy library
sqlite3 (built into Python)
```

### Installation & Execution
```bash
# Clone or download the project files
# Navigate to project directory

# Install dependencies (if needed)
pip install pandas numpy

# Run the SQL demonstrations
python sql_analytics_examples.py
```

### Expected Output
```
🔍 SQL Analytics Skills Demonstration
============================================================

📊 1. REVENUE DASHBOARD QUERY
📊 2. CUSTOMER SEGMENTATION QUERY  
⚡ 3. USAGE OPTIMIZATION QUERY
🚨 4. CHURN RISK ANALYSIS QUERY
💰 5. FINANCIAL KPI DASHBOARD QUERY
```

---

## 📋 **Project Structure**

```
sql-analytics/
├── sql_analytics_examples.py       # Main SQL demonstration script
├── requirements_dashboard_demo.txt  # Python dependencies
└── README_SQL_Analytics.md         # This documentation
```

---

## 💡 **Advanced SQL Techniques Demonstrated**

### **Common Table Expressions (CTEs)**
```sql
WITH customer_metrics AS (
    SELECT customer_id, 
           AVG(usage) as avg_usage,
           SUM(revenue) as total_revenue
    FROM transactions 
    GROUP BY customer_id
),
customer_segments AS (
    SELECT *,
           CASE WHEN total_revenue > 1000 THEN 'High Value'
                ELSE 'Standard' END as segment
    FROM customer_metrics
)
SELECT segment, COUNT(*) as customer_count
FROM customer_segments
GROUP BY segment;
```

### **Window Functions for Time Series**
```sql
SELECT month,
       revenue,
       LAG(revenue) OVER (ORDER BY month) as prev_month,
       (revenue - LAG(revenue) OVER (ORDER BY month)) / 
       LAG(revenue) OVER (ORDER BY month) * 100 as growth_rate
FROM monthly_revenue;
```

### **Multi-Factor Risk Scoring**
```sql
SELECT customer_id,
       CASE WHEN days_inactive > 14 THEN 3 ELSE 0 END +
       CASE WHEN avg_usage < 10 THEN 2 ELSE 0 END +
       CASE WHEN support_tickets > 5 THEN 1 ELSE 0 END as risk_score
FROM customer_activity;
```

---

## 🧠 **Analytical Insights & Design Decisions**

### **Data Generation Strategy**
> *"Creating realistic test data is crucial for SQL development. The data needs to have the right patterns and edge cases to test query logic properly."*

- **Beta Distribution**: Used for churn probability to create realistic right-skewed patterns
- **Seasonal Patterns**: Incorporated cyclical business trends in revenue data
- **Edge Cases**: Included inactive customers and varying usage patterns

### **Query Optimization Techniques**
> *"CTEs make complex queries maintainable and testable - essential for production BI systems."*

- **Modular Design**: Breaking complex logic into readable, testable components
- **Index-Friendly Patterns**: Query structures that work well with database indexes
- **NULL Handling**: Proper edge case management prevents dashboard errors

### **Business Metric Selection**
> *"Business context drives metric selection, not just technical capability."*

- **ARPU Calculations**: Average Revenue Per User for subscription business models
- **Cohort Analysis**: Customer lifecycle stage classification for targeted strategies
- **Risk Scoring**: Multi-dimensional behavioral analysis for proactive intervention

---

## 📊 **Query Categories & Business Applications**

### **1. Revenue Dashboard Queries**
**Business Use Case**: Executive financial reporting and trend analysis
```sql
-- Monthly revenue with growth calculations
-- Subscription tier performance breakdown
-- Period-over-period comparison analysis
```

### **2. Customer Segmentation Queries**
**Business Use Case**: Marketing campaign targeting and customer strategy
```sql
-- Behavioral pattern identification
-- Value-based customer classification
-- Lifecycle stage analysis
```

### **3. Usage Optimization Queries**
**Business Use Case**: Infrastructure planning and cost optimization
```sql
-- Peak usage identification
-- Capacity planning analysis
-- Resource allocation optimization
```

### **4. Churn Risk Analysis Queries**
**Business Use Case**: Customer retention and intervention planning
```sql
-- Multi-factor risk scoring
-- Revenue-at-risk calculations
-- Intervention prioritization
```

### **5. Financial KPI Queries**
**Business Use Case**: Executive dashboards and investor reporting
```sql
-- Growth rate calculations
-- Revenue mix analysis
-- Customer acquisition metrics
```

---

## 🎯 **Production Deployment Considerations**

### **Performance Optimization**
- **Indexing Strategy**: Proper indexes on date columns and customer IDs
- **Query Caching**: Results caching for frequently accessed metrics
- **Partitioning**: Date-based partitioning for large historical datasets

### **Data Warehouse Integration**
```sql
-- Example production deployment pattern
CREATE VIEW monthly_kpis AS
WITH base_metrics AS (
    -- Complex aggregation logic
)
SELECT * FROM base_metrics
WHERE month >= CURRENT_DATE - INTERVAL '12 months';
```

### **Error Handling & Monitoring**
- **NULL Safety**: Comprehensive NULL handling in all calculations
- **Data Quality Checks**: Validation queries for data integrity
- **Performance Monitoring**: Query execution time tracking

---

## 📈 **Sample Query Results**

### **Customer Segmentation Output**
```
value_segment | lifecycle_stage | customer_count | avg_ltv
High Value    | Established     | 150           | $2,450
Medium Value  | Growing         | 300           | $1,200  
Low Value     | New Customer    | 200           | $450
```

### **Churn Risk Analysis Output**
```
customer_id | risk_category | annual_revenue_at_risk | intervention_priority
12345      | High Risk     | $2,999.88             | 1
67890      | Medium Risk   | $1,199.88             | 2
```

### **Financial KPI Output**
```
month   | total_revenue | growth_rate | arpu   | customer_count
2024-10 | $125,450     | 8.5%        | $89.50 | 1,402
2024-09 | $115,680     | 6.2%        | $87.20 | 1,326
```

---

## 🔧 **Customization & Extension**

### **Adding New Business Metrics**
```python
def custom_kpi_query(self):
    """Template for adding new KPI calculations."""
    query = '''
    WITH metric_calculation AS (
        -- Custom business logic here
    )
    SELECT * FROM metric_calculation
    '''
    return pd.read_sql_query(query, self.conn)
```

### **Database Adaptation**
```python
# Easy adaptation to different database systems
def adapt_to_postgresql(query):
    # Replace SQLite-specific functions with PostgreSQL equivalents
    return query.replace("strftime('%Y-%m'", "DATE_TRUNC('month'")
```

### **Real Data Integration**
```python
# Template for connecting to production databases
def connect_to_production():
    return psycopg2.connect(
        host="your-warehouse-host",
        database="analytics_db",
        user="readonly_user"
    )
```

---

## 🏆 **Skills Demonstrated**

### **Advanced SQL Capabilities**
- ✅ Complex JOINs and subqueries for multi-table analysis
- ✅ Window functions (LAG, ROW_NUMBER) for time-series analysis  
- ✅ CTEs (Common Table Expressions) for readable complex queries
- ✅ Conditional aggregations (CASE WHEN) for segmented analysis
- ✅ Date/time functions for temporal analysis
- ✅ NULL handling and edge case management

### **Business Intelligence Expertise**
- ✅ Financial KPI calculations and growth metrics
- ✅ Customer behavior analysis and segmentation
- ✅ Risk assessment and scoring methodologies
- ✅ Performance optimization and capacity planning
- ✅ Executive-level reporting and dashboard queries

### **Production Readiness**
- ✅ Error handling and graceful degradation
- ✅ Performance optimization techniques
- ✅ Maintainable and documented code structure
- ✅ Scalable query patterns for large datasets

---

## 🔮 **Future Enhancements**

### **Advanced Analytics**
- [ ] **Cohort Analysis**: Customer retention and engagement tracking
- [ ] **Predictive Scoring**: ML-integrated risk prediction queries
- [ ] **Real-time Metrics**: Streaming data integration patterns
- [ ] **Advanced Segmentation**: RFM analysis and behavioral clustering

### **Performance & Scalability**
- [ ] **Query Optimization**: Advanced indexing and partitioning strategies
- [ ] **Caching Layer**: Redis integration for frequently accessed metrics
- [ ] **Parallel Processing**: Multi-threaded query execution
- [ ] **Cloud Integration**: BigQuery/Snowflake adaptation

---

## 🤝 **For Employers & Technical Reviewers**

### **This Project Demonstrates**
- **Production SQL Skills**: Complex queries ready for enterprise data warehouses
- **Business Acumen**: Understanding of key business metrics and KPIs
- **Analytical Thinking**: Data-driven approach to business problem solving
- **Code Quality**: Well-documented, maintainable, and testable SQL code

### **Real-World Applications**
- **BI Dashboard Backend**: Queries powering executive dashboards
- **Data Warehouse Analytics**: Production-ready analytical queries
- **Customer Intelligence**: Behavioral analysis for business strategy
- **Financial Reporting**: Automated KPI calculation and monitoring

---

## 📞 **Contact & Portfolio**

**Developer**: Sahar Moghtaderi  
**Specialization**: SQL Analytics & Business Intelligence  
**Skills**: Advanced SQL, Data Warehousing, Python, Machine Learning  

*This project demonstrates production-ready SQL analytics capabilities for business intelligence and data warehouse optimization.*

---

## 📄 **License**

This project is available for educational and portfolio purposes. Please provide attribution if used as a reference or template for SQL analytics development.

---

<div align="center">

**⭐ If these SQL examples were helpful, please give it a star! ⭐**

*Built with 🧠 and lots of ☕ for the data analytics community*

</div></div>
