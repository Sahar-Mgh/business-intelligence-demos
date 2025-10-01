#!/usr/bin/env python3
"""
Interactive BI Dashboard Demo - Customer Analytics Dashboard
Demonstrates Plotly Dash skills for dashboard development

This dashboard showcases data visualization and analysis capabilities
relevant to business intelligence and finance dashboard requirements.

Note to self: Building this taught me that interactive dashboards require 
different thinking than static charts - you need to consider user workflows 
and real-time data updates, not just visual appeal.
"""

import dash
from dash import dcc, html, Input, Output, dash_table
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Customer Analytics Dashboard - Interactive BI Demo"

# Generate sample data similar to real business scenarios
np.random.seed(42)

# Customer data (realistic business metrics)
n_customers = 1000
customer_data = pd.DataFrame({
    'customer_id': range(1, n_customers + 1),
    'monthly_charges': np.random.normal(65, 20, n_customers),
    'tenure_months': np.random.exponential(24, n_customers),
    'total_charges': np.random.normal(1500, 800, n_customers),
    'churn_probability': np.random.beta(2, 8, n_customers),
    'segment': np.random.choice(['Budget', 'Premium', 'Enterprise'], n_customers, p=[0.5, 0.3, 0.2]),
    'acquisition_date': pd.date_range(start='2020-01-01', periods=n_customers, freq='D')
})

# Note to self: Using beta distribution for churn probability was key - 
# it naturally creates the right-skewed distribution we see in real churn data
# where most customers have low churn risk, few have high risk.

# Financial metrics over time
dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
financial_data = pd.DataFrame({
    'date': dates,
    'revenue': np.random.normal(50000, 10000, len(dates)) + np.sin(np.arange(len(dates)) * 2 * np.pi / 365) * 5000,
    'costs': np.random.normal(30000, 5000, len(dates)),
    'active_users': np.random.poisson(8000, len(dates)) + np.sin(np.arange(len(dates)) * 2 * np.pi / 365) * 1000,
    'new_signups': np.random.poisson(150, len(dates))
})
financial_data['profit'] = financial_data['revenue'] - financial_data['costs']
financial_data['month'] = financial_data['date'].dt.to_period('M')

# Note to self: Adding seasonal patterns with sine waves makes the data more realistic.
# Real business metrics often have cyclical patterns - this is crucial for testing
# dashboard responsiveness to different data shapes.

# App layout
app.layout = html.Div([
    html.Div([
        html.H1("📊 Customer Analytics Dashboard", 
                style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': 30}),
        html.P("Interactive BI Dashboard Demo - Built with Plotly Dash", 
               style={'textAlign': 'center', 'color': '#7f8c8d', 'fontSize': 16})
    ]),
    
    # KPI Cards Row
    html.Div([
        html.Div([
            html.H3(f"€{financial_data['revenue'].sum()/1000000:.1f}M", 
                    style={'color': '#27ae60', 'margin': 0}),
            html.P("Total Revenue", style={'margin': 0, 'color': '#7f8c8d'})
        ], className='kpi-card', style={'backgroundColor': '#ecf0f1', 'padding': 20, 'borderRadius': 10, 'textAlign': 'center'}),
        
        html.Div([
            html.H3(f"{customer_data['churn_probability'].mean():.1%}", 
                    style={'color': '#e74c3c', 'margin': 0}),
            html.P("Avg Churn Risk", style={'margin': 0, 'color': '#7f8c8d'})
        ], className='kpi-card', style={'backgroundColor': '#ecf0f1', 'padding': 20, 'borderRadius': 10, 'textAlign': 'center'}),
        
        html.Div([
            html.H3(f"{len(customer_data):,}", 
                    style={'color': '#3498db', 'margin': 0}),
            html.P("Active Customers", style={'margin': 0, 'color': '#7f8c8d'})
        ], className='kpi-card', style={'backgroundColor': '#ecf0f1', 'padding': 20, 'borderRadius': 10, 'textAlign': 'center'}),
        
        html.Div([
            html.H3(f"€{customer_data['monthly_charges'].mean():.0f}", 
                    style={'color': '#9b59b6', 'margin': 0}),
            html.P("Avg Monthly Revenue", style={'margin': 0, 'color': '#7f8c8d'})
        ], className='kpi-card', style={'backgroundColor': '#ecf0f1', 'padding': 20, 'borderRadius': 10, 'textAlign': 'center'})
    ], style={'display': 'flex', 'justifyContent': 'space-around', 'marginBottom': 30}),
    
    # Charts Row 1
    html.Div([
        html.Div([
            dcc.Graph(id='revenue-trend')
        ], style={'width': '48%', 'display': 'inline-block'}),
        
        html.Div([
            dcc.Graph(id='customer-segments')
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),
    
    # Charts Row 2
    html.Div([
        html.Div([
            dcc.Graph(id='churn-analysis')
        ], style={'width': '48%', 'display': 'inline-block'}),
        
        html.Div([
            dcc.Graph(id='financial-metrics')
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),
    
    # Data Table
    html.Div([
        html.H3("🔍 High-Risk Customers", style={'color': '#2c3e50'}),
        dash_table.DataTable(
            id='high-risk-table',
            columns=[
                {'name': 'Customer ID', 'id': 'customer_id'},
                {'name': 'Monthly Charges', 'id': 'monthly_charges', 'type': 'numeric', 'format': {'specifier': '€,.0f'}},
                {'name': 'Tenure (Months)', 'id': 'tenure_months', 'type': 'numeric', 'format': {'specifier': '.1f'}},
                {'name': 'Churn Risk', 'id': 'churn_probability', 'type': 'numeric', 'format': {'specifier': '.1%'}},
                {'name': 'Segment', 'id': 'segment'}
            ],
            data=customer_data.nlargest(10, 'churn_probability').to_dict('records'),
            style_cell={'textAlign': 'left', 'padding': '10px'},
            style_header={'backgroundColor': '#3498db', 'color': 'white', 'fontWeight': 'bold'},
            style_data_conditional=[
                {
                    'if': {'filter_query': '{churn_probability} > 0.7'},
                    'backgroundColor': '#ffebee',
                    'color': 'black',
                }
            ]
        )
    ], style={'marginTop': 30, 'marginBottom': 30}),
    
    html.Div([
        html.P("📈 Built with Plotly Dash | Demonstrates interactive BI dashboard capabilities", 
               style={'textAlign': 'center', 'color': '#95a5a6', 'marginTop': 30})
    ])
], style={'margin': '20px'})

# Note to self: Conditional formatting in data tables is powerful for highlighting
# actionable insights. The red highlighting for high churn risk immediately draws
# attention to customers who need intervention.

# Callbacks for interactive charts
@app.callback(
    Output('revenue-trend', 'figure'),
    Input('revenue-trend', 'id')
)
def update_revenue_trend(_):
    monthly_revenue = financial_data.groupby('month').agg({
        'revenue': 'sum',
        'profit': 'sum'
    }).reset_index()
    monthly_revenue['month_str'] = monthly_revenue['month'].astype(str)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=monthly_revenue['month_str'], 
        y=monthly_revenue['revenue']/1000,
        mode='lines+markers',
        name='Revenue',
        line=dict(color='#3498db', width=3)
    ))
    fig.add_trace(go.Scatter(
        x=monthly_revenue['month_str'], 
        y=monthly_revenue['profit']/1000,
        mode='lines+markers',
        name='Profit',
        line=dict(color='#27ae60', width=3)
    ))
    
    fig.update_layout(
        title='📈 Monthly Revenue & Profit Trend (€K)',
        xaxis_title='Month',
        yaxis_title='Amount (€K)',
        hovermode='x unified',
        template='plotly_white'
    )
    return fig

# Note to self: Using 'x unified' hover mode was a game-changer for multi-line charts.
# It shows all values at once when hovering, much better UX than individual hovers.

@app.callback(
    Output('customer-segments', 'figure'),
    Input('customer-segments', 'id')
)
def update_customer_segments(_):
    segment_stats = customer_data.groupby('segment').agg({
        'monthly_charges': 'mean',
        'customer_id': 'count'
    }).reset_index()
    
    fig = px.pie(
        segment_stats, 
        values='customer_id', 
        names='segment',
        title='🎯 Customer Distribution by Segment',
        color_discrete_map={'Budget': '#e74c3c', 'Premium': '#f39c12', 'Enterprise': '#27ae60'}
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig

@app.callback(
    Output('churn-analysis', 'figure'),
    Input('churn-analysis', 'id')
)
def update_churn_analysis(_):
    fig = px.scatter(
        customer_data, 
        x='tenure_months', 
        y='monthly_charges',
        color='churn_probability',
        size='total_charges',
        title='🚨 Churn Risk Analysis',
        labels={
            'tenure_months': 'Tenure (Months)',
            'monthly_charges': 'Monthly Charges (€)',
            'churn_probability': 'Churn Risk'
        },
        color_continuous_scale='Reds'
    )
    fig.update_layout(template='plotly_white')
    return fig

# Note to self: Scatter plots with size and color encoding can show 4 dimensions
# simultaneously. This churn analysis reveals the pattern that new customers
# with high charges are often at highest risk - actionable insight!

@app.callback(
    Output('financial-metrics', 'figure'),
    Input('financial-metrics', 'id')
)
def update_financial_metrics(_):
    monthly_metrics = financial_data.groupby('month').agg({
        'active_users': 'mean',
        'new_signups': 'sum'
    }).reset_index()
    monthly_metrics['month_str'] = monthly_metrics['month'].astype(str)
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=monthly_metrics['month_str'],
        y=monthly_metrics['new_signups'],
        name='New Signups',
        marker_color='#9b59b6'
    ))
    
    # Add secondary y-axis for active users
    fig.add_trace(go.Scatter(
        x=monthly_metrics['month_str'],
        y=monthly_metrics['active_users'],
        mode='lines+markers',
        name='Active Users',
        yaxis='y2',
        line=dict(color='#e67e22', width=3)
    ))
    
    fig.update_layout(
        title='👥 User Acquisition & Retention Metrics',
        xaxis_title='Month',
        yaxis=dict(title='New Signups', side='left'),
        yaxis2=dict(title='Active Users', side='right', overlaying='y'),
        template='plotly_white'
    )
    return fig

# Note to self: Dual y-axis charts are tricky - the scales need to be meaningful.
# Here, bars for signups (smaller numbers) and line for active users (larger numbers)
# works well visually and tells the retention story.

if __name__ == '__main__':
    print("🚀 Starting Interactive Dashboard Demo...")
    print("📊 Navigate to http://127.0.0.1:8050 to view the dashboard")
    print("💡 This demonstrates Plotly Dash skills for BI dashboard development")
    print("\n🧠 Key Learning: Interactive dashboards require thinking about user workflows,")
    print("   not just data visualization. Each chart should answer specific business questions.")
    app.run_server(debug=True, port=8050)
