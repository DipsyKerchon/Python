# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.


from time import sleep


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        while True:
            for el in TrafficLight.__color:
                if el == 'Red':
                    print("\033[31m {}" .format(el))
                    sleep(7)
                elif el == 'Yellow':
                    print("\033[33m {}" .format(el))
                    sleep(2)
                elif el == 'Green':
                    print("\033[32m {}" .format(el))
                    sleep(4)
            print("\033[33m {}" .format(TrafficLight.__color[1]))
            sleep(2)
            continue


trafficlight = TrafficLight()
trafficlight.running()
