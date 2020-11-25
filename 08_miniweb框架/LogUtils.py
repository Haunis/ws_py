import logging

# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
logging.basicConfig(level=logging.DEBUG, format='%(message)s')


def main():
    # logging.info('this is a loggging info message')
    # logging.debug('this is a loggging debug message')
    # logging.warning('this is loggging a warning message')
    # logging.error('this is an loggging error message')
    # logging.critical('this is a loggging critical message')

    logging.info("\033[1;28m this is color0 \033[0m")
    logging.info("\033[1;29m this is color1 \033[0m")
    logging.info("\033[1;30m this is color2 \033[0m")
    logging.info("\033[1;31m this is color3 \033[0m")
    logging.info("\033[1;32m this is color4 \033[0m")
    logging.info("\033[1;33m this is color5 \033[0m")
    logging.info("\033[1;34m this is color6 \033[0m")
    logging.info("\033[1;35m this is color7 \033[0m")
    logging.info("\033[1;36m this is color8 \033[0m")
    logging.info("\033[1;37m this is color9 \033[0m")
    logging.info("\033[1;38m this is color9 \033[0m")
    logging.info("\033[1;40m this is color9 \033[0m")
    logging.info("\033[1;41m this is color9 \033[0m")
    logging.info("\033[1;42m this is color9 \033[0m")
    logging.info("\033[1;43m this is color9 \033[0m")


if __name__ == "__main__":
    main()


def i(msg):
    logging.info("\033[1;36m%s\033[0m" % msg)


def d(msg):
    logging.debug("\033[1;34m%s\033[0m" % msg)


def w(msg):
    logging.warning("\033[1;32m%s\033[0m" % msg)


def e(msg):
    logging.error("\033[1;31m%s\033[0m" % msg)
