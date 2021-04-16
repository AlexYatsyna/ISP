import argparse
import configparser

def Create_Parser():

    parser = argparse.ArgumentParser(description="Output format , input and output files")
    parser.add_argument('--output_format',type=str,default="json",help=" output format")
    parser.add_argument('--input_file',type=str,default="/home/alex/lab2/files/datafile.pickle",help="input file")
    parser.add_argument('--output_file',type=str,default="/home/alex/lab2/files/datafile.json",help="output file")
    parser.add_argument('--config',type=str,help="path to config file")

    return parser

def read_from_config(path_to_config):
    
    config = configparser.ConfigParser()
    config.read(path_to_config)
    default_values = {}
    default_values['output_format'] = "json"
    default_values['input_file'] = "/home/alex/lab2/files/datafile.json"
    default_values['output_file'] = "/home/alex/lab2/files/datafile.toml"

    value_1 = config.get("Parametrs","output_format")
    value_2 = config.get("Parametrs","input_file")
    value_3 = config.get("Parametrs","output_file")
    default_values['output_format'] = value_1
    default_values['input_file'] = value_2
    default_values['output_file'] = value_3

    return default_values

