import numpy as np
from sklearn.datasets import load_diabetes
import pika
import json

X, y = load_diabetes(return_X_y=True)
random_row = np.random.randint(0, X.shape[0]-1)

while True:
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel = connection.channel()

        # Создадим очередь, с которой будем работать:
        channel.queue_declare(queue='Features')
        channel.queue_declare(queue='y_true')

        # Опубликуем сообщение
        # exchange определяет, в какую очередь отправляется сообщение,
        # параметр routing_key указывает имя очереди,
        # параметр body тело самого сообщения,

        X_pred_json = json.dumps(list(X[random_row, :]))
        y_true_json = json.dumps([y[random_row]])

        channel.basic_publish(exchange='',
                              routing_key='Features',
                              body=X_pred_json)
        print('Сообщение с вектором признаков, отправлено в очередь')

        channel.basic_publish(exchange='',
                              routing_key='y_true',
                              body=y_true_json)
        print('Сообщение с правильным ответом, отправлено в очередь')

        # Закроем подключение
        connection.close()

    except:
        print('Не удалось подключиться к очереди')
