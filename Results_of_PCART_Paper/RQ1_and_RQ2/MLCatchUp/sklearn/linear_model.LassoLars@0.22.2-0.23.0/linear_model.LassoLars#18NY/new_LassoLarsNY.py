from sklearn import linear_model
reg = linear_model.LassoLars(1.0, normalize=True, precompute='auto', fit_intercept=True, verbose=False, jitter=None, random_state=None)
