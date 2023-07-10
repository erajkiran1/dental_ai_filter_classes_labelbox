from argparse import ArgumentParser
from os.path import normpath
from warnings import filterwarnings
from utils.filter_json import filter_json


def main():
    filterwarnings("ignore")
    msg = """Please give input as """

    # Initialize parser
    parser = ArgumentParser(description = msg)
    parser.add_argument("-jr", "--json_file_to_read", help = "please give location path in string format of LABEL JSON FILE",required=True)
    parser.add_argument("-js", "--json_file_path_to_save", help="please give location path in string format of LABEL JSON FILE",required=True)
    parser.add_argument('-cl', '--list', nargs='+', help='Please give the list in the type of <value> in annotation[Label]["objects"][0]["value"]', required=True)
    args = parser.parse_args()
    json_read_path = normpath(args.json_file_to_read)
    json_save_path = normpath(args.json_file_path_to_save)
    given_list_to_filter = args.list
    result = filter_json(json_file_path=json_read_path,json_path_to_save=json_save_path,classes_to_filter=given_list_to_filter)
    print("File Stored in the given location {}".format(result))



if __name__ == '__main__':
	main()

