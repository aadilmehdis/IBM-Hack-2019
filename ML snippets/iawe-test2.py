from __future__ import print_function, division
import time

from matplotlib import rcParams
import matplotlib.pyplot as plt

from nilmtk import DataSet, TimeFrame, MeterGroup, HDFDataStore
from shortseq2pointdisaggregator import ShortSeq2PointDisaggregator
import metrics

print("========== OPEN DATASETS ============")
train = DataSet('iawe.h5')
test = DataSet('iawe.h5')

# train.set_window(start="13-4-2013", end="1-1-2014")
# train.set_window(start="24-5-2013", end="5-7-2013")
train.set_window(start="5-24-2013", end="7-5-2013")
# test.set_window(start="1-1-2014", end="30-3-2014")
# test.set_window(start="5-7-2013", end="5-8-2013")
test.set_window(start="7-5-2013", end="8-5-2013")

train_building = 1
test_building = 1
sample_period = 6
meter_key = 'fridge'
train_elec = train.buildings[train_building].elec
test_elec = test.buildings[test_building].elec

train_meter = train_elec.submeters()[meter_key]
train_mains = train_elec.mains()
test_mains = test_elec.mains()
disaggregator = ShortSeq2PointDisaggregator()

disaggregator.import_model("IAWE-RNN-h{}-{}-{}epochs.h5".format(train_building,
                                                        meter_key,
                                                        10))

print("========== DISAGGREGATE ============")
disag_filename = "disag-out.h5"
output = HDFDataStore(disag_filename, 'w')
disaggregator.disaggregate(test_mains, output, train_meter, sample_period=sample_period)
output.close()

print("========== RESULTS ============")
result = DataSet(disag_filename)
res_elec = result.buildings[test_building].elec
rpaf = metrics.recall_precision_accuracy_f1(res_elec[meter_key], test_elec[meter_key])
print("============ Recall: {}".format(rpaf[0]))
print("============ Precision: {}".format(rpaf[1]))
print("============ Accuracy: {}".format(rpaf[2]))
print("============ F1 Score: {}".format(rpaf[2]))

print("============ Relative error in total energy: {}".format(metrics.relative_error_total_energy(res_elec[meter_key], test_elec[meter_key])))
print("============ Mean absolute error(in Watts): {}".format(metrics.mean_absolute_error(res_elec[meter_key], test_elec[meter_key])))
