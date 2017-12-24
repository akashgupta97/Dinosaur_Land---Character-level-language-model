from __future__ import print_function
from keras.callbacks import LambdaCallback
from keras.models import Model, load_model, Sequential
from keras.layers import Dense, Activation, Dropout, Input, Masking
from keras.layers import LSTM
from keras.utils.data_utils import get_file
from keras.preprocessing.sequence import pad_sequences
from shakespeare_utils import *
import sys
import io


print_callback = LambdaCallback(on_epoch_end=on_epoch_end)

model.fit(x, y, batch_size=128, epochs=1, callbacks=[print_callback])


# Run this cell to try with different inputs without having to re-train the model
generate_output()


'''
Write the beginning of the poem, the Shakespeare machine will complete it. The input is: One Love


Here is your poem: 

One Love the carve, oud bearing maly,
with ink falels me all trife' sey pely,
why of offore self-race spuse doth by kees,
not your have i mon chech should she wod,
in whensiigh nand it dellens a weld, ditnor shilun,
in himter felten stornt to sifpe thought,
thee is, mahe betier thite the shall ever looh.

sow god thumser to youl of choudcless spere.
 noe thou in whereoed to mer as one'er,
but mode my vier
'''