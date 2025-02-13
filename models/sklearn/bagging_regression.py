import dataset.setbuilder as sb
import models.sklearn.evaluator as eval
from sklearn import svm

data = sb.SetBuilder(target='NumberOfSales').build().random_sampling(percentage=0.1)
clf = svm.SVR()
clf.fit(data.xtr, data.ytr.ravel())

ypred = clf.predict(data.xts)



print('R2 = %s' % eval.evaluate(data.yts, ypred))
