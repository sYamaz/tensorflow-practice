# トレーニングとモデルのエクスポート
import tensorflow as tf
print("tensorflow launch. version="+tf.__version__)


def get_model(num_params:int):
    # layerの定義
    inputs = tf.keras.layers.Input(shape = num_params)
    x = tf.keras.layers.Dense(units=16, activation="relu")(inputs)
    x = tf.keras.layers.Dense(units=32, activation="relu")(x)
    x = tf.keras.layers.Dense(units=32, activation="relu")(x)
    outputs = tf.keras.layers.Dense(units = 1, activation="linear")(x)

    # model
    model = tf.keras.models.Model(inputs=inputs, outputs=outputs)

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=5e-3),
        loss="mse"
    )
    return model


def main():
    # 学習用データ取得
    num_params = "TODO"

    # モデルの作成
    model = get_model(num_params)

    # トレーニング開始
    model.fit()

    model.j
    pass

if __name__ == "__main__":
    main()