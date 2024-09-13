import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t, norm

def generate_distribution_data(df, x_range=(-5, 5), num_points=1000):
    """Generate data for Student's t and normal distributions."""
    x = np.linspace(*x_range, num_points)
    student_t_pdf = t.pdf(x, df=df)
    normal_pdf = norm.pdf(x)
    return x, student_t_pdf, normal_pdf

def plot_distributions(x, student_t_pdf, normal_pdf, df):
    """Create and customize the distribution plot."""
    plt.figure(figsize=(12, 8))
    plt.plot(x, student_t_pdf, label=f"Student T (df={df})")
    plt.plot(x, normal_pdf, label="Normal")
    
    annotations = [
        ("1. Prevalence in finance", (1, 0.25), (2, 0.3), 
         "T-distribution is often used in financial modeling due to its heavier tails"),
        ("2. Approximation to Gaussian", (-2, 0.25), (-4, 0.3), 
         "As df increases, t-distribution approaches normal distribution"),
        ("3. Asymptotic convergence", (-1, 0.15), (0, 0.25), 
         "T-distribution converges to normal as df approaches infinity"),
        ("4. Tail behavior", (-3, 0.05), (-4, 0.15), 
         "T-distribution has heavier tails, accounting for extreme events more effectively")
    ]
    
    for text, xy, xytext, description in annotations:
        plt.annotate(f"{text}\n{description}", xy=xy, xytext=xytext,
                     arrowprops=dict(facecolor='black', shrink=0.05),
                     bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))
    
    plt.xlabel('x')
    plt.ylabel('Density')
    plt.title('Comparison of Student T and Normal Distribution')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    df = 3  # Degrees of freedom for t-distribution
    x, student_t_pdf, normal_pdf = generate_distribution_data(df)
    plot_distributions(x, student_t_pdf, normal_pdf, df)

if __name__ == "__main__":
    main()
