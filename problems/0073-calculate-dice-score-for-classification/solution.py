
import numpy as np

def dice_score(y_true, y_pred):
	actual_tp = np.sum(y_true)
	pred_p = np.sum(y_pred)
	pred_tp = np.sum(y_true & y_pred)

	total = actual_tp + pred_p
	if total == 0:
		return 0.0
	
	res = (2 * pred_tp) / total
	return round(res, 3)