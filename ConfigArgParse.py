# documentation for configargparse: https://github.com/bw2/ConfigArgParse
import configargparse, sys, yaml
from configargparse import Namespace

def _initialize_arguments(parser):
    parser.add('-config', help="configuration file *.yml", type=str, \
         required=False, default='config.yml')
    parser.add_argument('-args', help="learning rate", type=bool, required=False, default=False)
    # training parameters
    parser.add('-epochs', help="num of epochs for train", type=int, \
         required=False, default=100)
    parser.add('-lr', help="learning rate", type=float, required=False, default=0.00005)
    parser.add('-batch_size', help="batch size", type=int, required=False, default=64)
    sys.argv = ['-f']
    args = parser.parse_args()

    if not args.args:  # args priority is higher than yaml
        opt = vars(args)
        args = yaml.load(open(args.config), Loader=yaml.FullLoader)
        opt.update(args)
    else:  # yaml priority is higher than args
        opt = yaml.load(open(args.config), Loader=yaml.FullLoader)
        opt.update(vars(args))
    args = Namespace(**args) 
    return args

if __name__ == '__main__':

    # parser = configargparse.ArgParser(default_config_files=['config.yml'])
    parser = configargparse.get_argument_parser()
    args = _initialize_arguments(parser)
    print("arguments: {}".format(str(args)))

