import os
import datetime
import configparser
import time

# функция получения текущего времени и даты
def get_time_date():
    today = datetime.datetime.today()
    return today.strftime("%H:%M:%S %d-%m-%Y")

# сама пинг функция
def ping(hostname):
    response = os.system("ping -c 1 " + hostname)

# проверяем ответ ...
    if response == 0:
        print('%s OK: host %s is up\n' % (get_time_date(), hostname))
        # if OK делаем паузу на ping_interval в секундах,
        # так как нам не нужно получать пинг очень быстро, мы же только проверяем, что хост не упал
        time.sleep(ping_interval)
        return('%s OK: host %s is up\n' % (get_time_date(), hostname))
    else:
        print('Warning: \n%s | host %s is down!\n' % (get_time_date(), hostname))
        return('Warning: \n%s | host %s is down!\n' % (get_time_date(), hostname))


# main process
if __name__ == '__main__':
    # init config parser
    config = configparser.ConfigParser()
    # Указываем ini file
    config.read('ping.ini')

    # считываем все параметры из ini файла
    hostname = config.get('default', 'hostname')
    ping_interval = config.getint('default', 'ping_interval')
    number_of_pings = config.getint('default', 'ping_attempts')

    file = os.getcwd() + "_log_" + get_time_date() + ".txt"

    try:
        with open(file, "w") as file_handler:
            print(f"File opened, log started to file: {file}")

            # начало лога - шапка
            file_handler.write("================ This is ping log file ================\n")
            file_handler.write(f"hostname:      {hostname}\n")
            file_handler.write(f"interval:      {ping_interval} sec.\n")
            file_handler.write(f"ping attempts: {number_of_pings}\n")
            file_handler.write(f"Start log at {get_time_date()}\n")
            file_handler.flush()

            i = 0
            while (i < number_of_pings):
                i += 1
                # делаем 1 пинг
                log_str = ping(hostname)
                # пишем в лог
                file_handler.write(log_str)
                file_handler.flush()


    except IOError:
        print("An IOError has occurred!")
