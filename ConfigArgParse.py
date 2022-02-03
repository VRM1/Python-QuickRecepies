import argparse, sys, yaml

def _initialize_arguments(p):
    parser.add_argument('-config', help="configuration file *.yml", type=str, \
         required=False, default='config.yml')
    parser.add_argument('-args', help="learning rate", type=bool, required=False, default=False)
    # training parameters
    parser.add_argument('-epochs', help="num of epochs for train", type=int, \
         required=False, default=100)
    parser.add_argument('-lr', help="learning rate", type=float, required=False, default=0.00005)
    parser.add_argument('-batch_size', help="batch size", type=int, required=False, default=64)
    sys.argv = ['-f']
    args = parser.parse_args()

    if not args.args:  # args priority is higher than yaml
        opt = vars(args)
        args = yaml.load(open(args.config), Loader=yaml.FullLoader)
        opt.update(args)
        args = opt
    else:  # yaml priority is higher than args
        opt = yaml.load(open(args.config), Loader=yaml.FullLoader)
        opt.update(vars(args))
        args = opt
    return args

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    args = _initialize_arguments(parser)
    print("arguments: {}".format(str(args)))

