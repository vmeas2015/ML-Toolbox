def recommend_metrics(algorithm, multiclass=None):

##########################################
########## Classification metrics ########
##########################################
	# Average_precision
	metrics.average_precision_score

	# F1
	metrics.f1_score

	#neg_log_loss
	metrics.log_loss
	# Precision
	metrics.precision_score

	# Recall
	metrics.recall_score

	# Roc_auc
	metrics.roc_auc_score

	
	# Strictly binary classification

	# Compute precision-recall pairs for different probability thresholds
	precision_recall_curve(y_true, probas_pred)
	roc_curve(y_true, y_score[, pos_label, …])	Compute Receiver operating characteristic (ROC)
	
	Others also work in the multiclass case:	
	
	precision_score(y_true, y_pred[, labels, …])	Compute the precision
	recall_score(y_true, y_pred[, labels, …])	Compute the recall
	f1_score(y_true, y_pred[, labels, …])	Compute the F1 score, also known as balanced F-score or F-measure
	fbeta_score(y_true, y_pred, beta[, labels, …])	Compute the F-beta score
	accuracy_score(y_true, y_pred[, normalize, …])	Accuracy classification score.
	log_loss(y_true, y_pred[, eps, normalize, …])	Log loss, aka logistic loss or cross-entropy loss.

	classification_report(y_true, y_pred[, …])	Build a text report showing the main classification metrics
	confusion_matrix(y_true, y_pred[, labels, …])	Compute confusion matrix to evaluate the accuracy of a classification

##########################################
########## Regression metrics ############
##########################################

	# Explained_variance
	metrics.explained_variance_score	 
	# Neg_mean_absolute_error

	metrics.mean_absolute_error	 
	# neg_mean_squared_error
	metrics.mean_squared_error	 
	# neg_mean_squared_log_error
	metrics.mean_squared_log_error	 

	# neg_median_absolute_error’
	metrics.median_absolute_error	 
	# R2
	metrics.r2_score

def get_recommend_metrics(algorithm, multiclass=None):