from sklearn import linear_model
clf = linear_model.BayesianRidge(n_iter=300, tol=0.001, alpha_1=1e-06, alpha_init=None, lambda_init=None)
