import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from datetime import datetime, timedelta

def generate_fitness_data():
    """Generate sample fitness data for a month"""
    np.random.seed(42)
    date_range = pd.date_range(end=datetime.today(), periods=30)
    data = {
        'date': date_range,
        'weight': np.linspace(75, 72, 30) + np.random.normal(0, 0.3, 30),
        'calories_burnt': np.random.randint(1800, 3000, 30),
        'steps': np.random.randint(4000, 15000, 30)
    }
    return pd.DataFrame(data)

def create_fitness_dashboard():
    # Create assets directory if it doesn't exist
    os.makedirs('assets', exist_ok=True)
    
    # Generate sample data
    df = generate_fitness_data()
    
    # Create figure with subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))
    fig.suptitle('Fitness Progress Dashboard', fontsize=16, y=1.05)
    
    # Scatter Plot: Weight vs Calories
    scatter = ax1.scatter(
        df['calories_burnt'], 
        df['weight'],
        c=df['steps'],
        cmap='viridis',
        s=100,
        alpha=0.7
    )
    ax1.set_title('Weight vs Calories Burnt (Color by Steps)')
    ax1.set_xlabel('Calories Burnt')
    ax1.set_ylabel('Weight (kg)')
    
    # Add colorbar
    cbar = plt.colorbar(scatter, ax=ax1)
    cbar.set_label('Daily Steps')
    
    # Highlight best and worst days
    best_day = df.loc[df['steps'].idxmax()]
    worst_day = df.loc[df['steps'].idxmin()]
    
    ax1.annotate(f"Best: {best_day['steps']} steps",
                xy=(best_day['calories_burnt'], best_day['weight']),
                xytext=(10, 10), textcoords='offset points',
                bbox=dict(boxstyle='round,pad=0.5', fc='green', alpha=0.5),
                arrowprops=dict(arrowstyle='->'))
    
    ax1.annotate(f"Worst: {worst_day['steps']} steps",
                xy=(worst_day['calories_burnt'], worst_day['weight']),
                xytext=(-60, -30), textcoords='offset points',
                bbox=dict(boxstyle='round,pad=0.5', fc='red', alpha=0.5),
                arrowprops=dict(arrowstyle='->'))
    
    # Histogram: Daily Steps
    ax2.hist(df['steps'], bins=15, color='skyblue', edgecolor='black')
    ax2.set_title('Daily Step Count Distribution')
    ax2.set_xlabel('Steps')
    ax2.set_ylabel('Frequency')
    ax2.grid(True, linestyle='--', alpha=0.6)
    
    # Add mean line
    mean_steps = df['steps'].mean()
    ax2.axvline(mean_steps, color='red', linestyle='dashed', linewidth=1)
    ax2.text(mean_steps+500, ax2.get_ylim()[1]*0.9, 
             f'Mean: {mean_steps:.0f} steps',
             color='red')
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig('assets/fitness_dashboard.png', dpi=120, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    create_fitness_dashboard()