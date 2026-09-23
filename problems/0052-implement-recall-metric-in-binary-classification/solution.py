import numpy as np

def recall(y_true, y_pred):
    """
    Calculate the recall metric for binary classification.
    
    Args:
        y_true: Array of true binary labels (0 or 1)
        y_pred: Array of predicted binary labels (0 or 1)
    
    Returns:
        Recall value as a float
    """
    true_positives = np.sum(y_true & y_pred)
    total_pred_positives = np.sum(y_true)

    if total_pred_positives == 0:
        return 0.0

    recall = true_positives / total_pred_positives
    return recall