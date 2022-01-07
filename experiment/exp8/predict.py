import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':

    data = pd.read_csv("income.csv")

    y_test = data['Income']
    x_test = data['Education']
    plt.scatter(x_test, y_test)
    plt.show()

    model = tf.keras.models.Sequential(
        tf.keras.layers.Dense(1, input_shape=(1,))
    )

    optimizer = tf.keras.optimizers.RMSprop(0.001)

    model.compile(loss='mse',
                  optimizer=optimizer,
                  metrics=['mae', 'mse'],
                  run_eagerly=True)

    class PrintDot(tf.keras.callbacks.Callback):
        def on_epoch_end(self, epoch, logs):
            if epoch % 100 == 0:
                print('')
            print('.', end='')

    history = model.fit(x_test, y_test, epochs=5000, validation_split=0.2, verbose=0, callbacks=PrintDot())
    print(model.predict([[20]]))
