import os, logging
from datetime import datetime
# SEE: https://pythonrepo.com/repo/bw2-ConfigArgParse-python-command-line-interface-development
import configargparse

if not os.path.isdir("logs"):
    os.mkdir("logs")
log = logging.getLogger()


def logger(log_dir, parser):

    # Set run specific envirorment configurations
    # args.timestamp = time.strftime("run_%Y_%m_%d_%H_%M_%S") + "_{machine}".format(machine=socket.gethostname())
    # os.makedirs(args.model_directory, exist_ok=True)

    # Handle logging configurations
    log.handlers.clear()
    formatter = logging.Formatter('%(message)s')
    fh = logging.FileHandler(os.path.join(log_dir, \
        datetime.now().strftime('train_log_%H_%M_%d_%m_%Y.log')))
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    log.addHandler(fh)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    log.setLevel(logging.INFO)
    log.addHandler(ch)
    log.info(parser.format_values())

if __name__ == '__main__':

    parser = configargparse.ArgParser()
    parser.add('-num_arg', type=int)
    parser.add('-str_arg', type=str)
    args = parser.parse_args()
    logger('logs', parser)