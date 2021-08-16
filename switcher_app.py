# main app
from getter import Getter
from writer import Writer
from deleter import Deleter
from copier import Copier
from runner import Runner


def main():
    my_runner = Runner(Getter(), Writer(), Deleter(), Copier())
    my_runner.run_it()


if __name__ == '__main__':
    main()
