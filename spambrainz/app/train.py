import numpy as np
from tensorflow.keras.layers import Input, Dense, Embedding, LSTM, Dropout, Reshape, concatenate
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical


def get_model() -> Model:
    main_input = Input(shape=(9,), name="main_input")
    email_input = Input(shape=(1,), dtype="int32", name="email_input")
    website_input = Input(shape=(1,), dtype="int32", name="website_input")
    bio_input = Input(shape=(512,), name="bio_input")

    email_embedding = Embedding(
        output_dim=256, input_dim=1025, input_length=1, name="email_embedding")(email_input)
    website_embedding = Embedding(
        output_dim=256, input_dim=1025, input_length=1, name="website_embedding")(website_input)
    bio_reshape = Reshape((1, 512), input_shape=(512,),
                          name="bio_reshape")(bio_input)

    email_lstm = LSTM(32, name="email_lstm")(email_embedding)
    website_lstm = LSTM(32, name="website_lstm")(website_embedding)
    bio_lstm = LSTM(64, name="bio_lstm")(bio_reshape)

    merge = concatenate(
        [website_lstm, email_lstm, bio_lstm, main_input], name="merge")

    dropout1 = Dropout(0.5, name="dropout_1")(merge)
    dense1 = Dense(64, activation="tanh", name="dense_1")(dropout1)
    dropout2 = Dropout(0.5, name="dropout_2")(dense1)
    dense2 = Dense(64, activation="tanh", name="dense_2")(dropout2)

    output = Dense(2, activation="softmax", name="output")(dense2)

    model = Model(inputs=[main_input, website_input,
                  email_input, bio_input], outputs=[output])

    adam = Adam()

    model.compile(optimizer=adam, loss="mse", metrics=["acc"])

    return model

# the model is retrained using this function with low epochs
# and static learning rate


def train_model(model: Model, dataset: np.ndarray, callbacks: list = None) -> None:
    model.fit(
        {
            "main_input": dataset[:, 1:10],
            "email_input": dataset[:, 10],
            "website_input": dataset[:, 11],
            "bio_input": dataset[:, 12:]
        },
        to_categorical(dataset[:, 0], 2),
        epochs=2,
        batch_size=1,
    )


def load_model(path: str) -> Model:
    model = get_model()
    model.load_weights(path)
    return model


def retrain_model(training_data):
    import datetime
    from tensorflow.keras.callbacks import TensorBoard

    tensorboard = TensorBoard(
        log_dir="./logs", write_graph=True, histogram_freq=0)

    # loading the model with previous weights
    m = load_model('static/models/weights/current_lodbrok.h5')

    # set model optimizer learning rate to a smaller static value to avoid
    # cateshtrophic forgetting
    m.optimizer.lr = 0.001

    # saving the previous weights before training for future reference
    m.save('static/models/weights/previous_lodbrok.h5')

    # training the model with new data obtained
    train_model(m, training_data, [tensorboard])

    # saving the new model for future use
    m.save("static/models/weights/current_lodbrok.h5")

    return True
    # print("Successfully retrianed the model")
