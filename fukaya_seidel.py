import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import pdist, squareform
from itertools import combinations

def compute_composite_macro_factor(macro_df):
    """Compute composite macro factor from all macro variables."""
    if len(macro_df) < 2:
        return np.ones(len(macro_df)) * 0.5
    scaler = StandardScaler()
    macro_scaled = scaler.fit_transform(macro_df)
    pca = PCA(n_components=1)
    factor = pca.fit_transform(macro_scaled).flatten()
    factor = (factor - factor.min()) / (factor.max() - factor.min() + 1e-8)
    return factor

def lagrangian_embedding(returns, macro_factor):
    """
    Embed ETFs as Lagrangians in a symplectic manifold.
    Each ETF is represented as a curve in phase space (return, momentum).
    """
    if len(returns) < 5:
        return None
    # Compute momentum (first difference)
    momentum = np.diff(returns)
    # Pad to keep same length
    momentum = np.concatenate([[0], momentum])
    # Phase space: (return, momentum) for each time step
    phase_space = np.column_stack([returns, momentum])
    # Scale by macro factor to capture symplectic structure
    macro_scaled = macro_factor[:len(phase_space)] if len(macro_factor) >= len(phase_space) else np.ones(len(phase_space)) * 0.5
    phase_space = phase_space * (1 + macro_scaled.reshape(-1, 1) * 0.5)
    return phase_space

def floer_homology(lagrangian1, lagrangian2, threshold=0.3):
    """
    Compute Floer homology between two Lagrangians.
    Counts intersection points (stable pairings) between the curves.
    """
    if lagrangian1 is None or lagrangian2 is None:
        return 0
    # Compute pairwise distances between points on the two Lagrangians
    # We're looking for "intersections" - close points in phase space
    n1, n2 = len(lagrangian1), len(lagrangian2)
    if n1 == 0 or n2 == 0:
        return 0
    # For each point in lagrangian1, find nearest point in lagrangian2
    # Count as intersection if distance < threshold
    intersections = 0
    for i in range(n1):
        min_dist = np.min(np.linalg.norm(lagrangian1[i] - lagrangian2, axis=1))
        if min_dist < threshold:
            intersections += 1
    # Floer homology rank = number of intersections / 2 (symplectic pairing)
    floer_rank = intersections // 2
    return max(1, floer_rank)

def a_infinity_operations(lagrangians, order=3):
    """
    Compute A∞ operations: higher-order associative relationships.
    Returns a matrix of operation strengths between Lagrangians.
    """
    n = len(lagrangians)
    if n < 2:
        return np.ones((n, n))
    # Compute pairwise Floer homology
    floer_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                floer_matrix[i, j] = floer_homology(lagrangians[i], lagrangians[j], config.FLOER_THRESHOLD)
    # A∞ operations = higher-order products of Floer homology
    # Simplified: use powers of the Floer matrix
    a_infinity = np.eye(n)
    for _ in range(1, order):
        a_infinity = a_infinity + np.linalg.matrix_power(floer_matrix, _) / np.math.factorial(_)
    return a_infinity

def fukaya_score(returns, macro_df, threshold=0.3, a_order=3):
    """
    Compute per-ETF Fukaya-Seidel category score.
    Score = average Floer homology rank with all other ETFs.
    """
    if len(returns) < 10 or macro_df is None or len(macro_df) < 10:
        return 0.0
    # Align lengths
    min_len = min(len(returns), len(macro_df))
    returns = returns[:min_len]
    macro_df = macro_df.iloc[:min_len]
    # Remove NaN
    mask = ~(np.isnan(returns) | np.isnan(macro_df).any(axis=1))
    returns = returns[mask]
    macro_df = macro_df[mask]
    if len(returns) < 10:
        return 0.0
    # Compute macro factor
    macro_factor = compute_composite_macro_factor(macro_df)
    # Embed the ETF as a Lagrangian
    lagrangian = lagrangian_embedding(returns, macro_factor)
    if lagrangian is None:
        return 0.0
    # For a single ETF, we compute its Floer homology with itself
    # The Fukaya-Seidel category score is the rank of its Floer homology
    # (self-intersections measure internal structure)
    floer_self = floer_homology(lagrangian, lagrangian, threshold)
    # Score = Floer homology rank (self-intersections / 2)
    score = floer_self
    return float(score)
