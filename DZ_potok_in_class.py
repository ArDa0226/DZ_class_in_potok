# -*- coding: UTF-8 -*-


from threading import Thread
import time

class Bogatyr(Thread):
    def __init__(self, name, skills, *args, **kwargs):
        super(Bogatyr, self).__init__(*args, **kwargs)
        self.name = name
        self.skills = skills
        self.count = 1
        self.anamy = 100

    def run(self):
        one_skill_sleepping = 4
        print(f'{self.name}, на нас наппали! Их не меньше {self.anamy} воинов!', flush=True)
        for day in range(self.anamy + 1):
            sleeping = self.skills / one_skill_sleepping
            time.sleep(sleeping)
            print(f'Богатырь {self.name} сражается {self.count} дней..., осталось {self.anamy - self.skills} врагов.', flush=True)
            self.anamy -= self.skills
            if self.anamy == 0:
                break
            self.count += 1
bogatyr_1 = Bogatyr(name='Илья Мурромец', skills=20)
bogatyr_2 = Bogatyr(name='Алеша Попович', skills=10)

bogatyr_1.start()
bogatyr_2.start()


bogatyr_1.join()
bogatyr_2.join()
for bog in (bogatyr_1, bogatyr_2):
    print(f'Богатырь {bog.name} одержал победу спустя {bog.count} дней', flush=True)
print('Все битвы закончились.')