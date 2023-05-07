#!/usr/bin/python

import subprocess
import argparse
import os

def subscrapper_runner(tool_output_file_path, domain_name, output_file_path):
    cmd = f"subscraper -r {tool_output_file_path}" + "/subscraper_out1.txt " + f"{domain_name}" + " > /dev/null && cat " + f"{tool_output_file_path}" + "/subscraper_out1.txt " + "> " + f"{output_file_path}"
    print(cmd)
    subprocess.run(cmd, shell=True)

    cmd = f"subscraper -r {tool_output_file_path}" + "/subscraper_out2.txt " + f"{domain_name}" + " > /dev/null && cat " + f"{tool_output_file_path}" + "/subscraper_out2.txt " + ">> " + f"{output_file_path}"
    print(cmd)
    subprocess.run(cmd, shell=True)

    cmd = f"subscraper -r {tool_output_file_path}" + "/subscraper_out3.txt " + f"{domain_name}" + " > /dev/null && cat " + f"{tool_output_file_path}" + "/subscraper_out3.txt " + ">> " + f"{output_file_path}"
    print(cmd)
    subprocess.run(cmd, shell=True)

    cmd = f"subscraper -r {tool_output_file_path}" + "/subscraper_out4.txt " + f"{domain_name}" + " > /dev/null && cat " + f"{tool_output_file_path}" + "/subscraper_out4.txt " + ">> " + f"{output_file_path}"
    print(cmd)
    subprocess.run(cmd, shell=True)

    cmd = f"subscraper -r {tool_output_file_path}" + "/subscraper_out5.txt " + f"{domain_name}" + " > /dev/null && cat " + f"{tool_output_file_path}" + "/subscraper_out5.txt " + ">> " + f"{output_file_path}"
    print(cmd)
    subprocess.run(cmd, shell=True)

def subfinder_runner(tool_output_file_path, domain_name, output_file_path):
    cmd = f"subfinder -d {domain_name}" + " > /dev/null 2>&1 > " + f"{tool_output_file_path}" + "/subfinder_out1.txt && cat " + f"{tool_output_file_path}" + "/subfinder_out1.txt >> " + f"{output_file_path}"
    print(cmd)
    subprocess.run(cmd, shell=True)

    cmd = f"subfinder -d {domain_name}" + " > /dev/null 2>&1 > " + f"{tool_output_file_path}" + "/subfinder_out2.txt && cat " + f"{tool_output_file_path}" + "/subfinder_out2.txt >> " + f"{output_file_path}"
    print(cmd)
    subprocess.run(cmd, shell=True)

    cmd = f"subfinder -d {domain_name}" + " > /dev/null 2>&1 > " + f"{tool_output_file_path}" + "/subfinder_out3.txt && cat " + f"{tool_output_file_path}" + "/subfinder_out3.txt >> " + f"{output_file_path}"
    print(cmd)
    subprocess.run(cmd, shell=True)

    cmd = f"subfinder -d {domain_name}" + " > /dev/null 2>&1 > " + f"{tool_output_file_path}" + "/subfinder_out4.txt && cat " + f"{tool_output_file_path}" + "/subfinder_out4.txt >> " + f"{output_file_path}"
    print(cmd)
    subprocess.run(cmd, shell=True)

    cmd = f"subfinder -d {domain_name}" + " > /dev/null 2>&1 > " + f"{tool_output_file_path}" + "/subfinder_out5.txt && cat " + f"{tool_output_file_path}" + "/subfinder_out5.txt >> " + f"{output_file_path}"
    print(cmd)
    subprocess.run(cmd, shell=True)

def assetfinder_runner(tool_output_file_path, domain_name, output_file_path):
    cmd = "assetfinder " + f"{domain_name}" + " | grep " + f"{domain_name}" + " > " f"{tool_output_file_path}" + "/assetfinder_out1 && cat " + f"{tool_output_file_path}" + "/assetfinder_out1" + " >> " + f"{output_file_path}"
    print(cmd)
    subprocess.run(cmd, shell=True)

    cmd = "assetfinder " + f"{domain_name}" + " | grep " + f"{domain_name}" + " > " f"{tool_output_file_path}" + "/assetfinder_out2 && cat " + f"{tool_output_file_path}" + "/assetfinder_out2" + " >> " + f"{output_file_path}"
    print(cmd)
    subprocess.run(cmd, shell=True)

    cmd = "assetfinder " + f"{domain_name}" + " | grep " + f"{domain_name}" + " > " f"{tool_output_file_path}" + "/assetfinder_out3 && cat " + f"{tool_output_file_path}" + "/assetfinder_out3" + " >> " + f"{output_file_path}"
    print(cmd)
    subprocess.run(cmd, shell=True)

    cmd = "assetfinder " + f"{domain_name}" + " | grep " + f"{domain_name}" + " > " f"{tool_output_file_path}" + "/assetfinder_out4 && cat " + f"{tool_output_file_path}" + "/assetfinder_out4" + " >> " + f"{output_file_path}"
    print(cmd)
    subprocess.run(cmd, shell=True)

    cmd = "assetfinder " + f"{domain_name}" + " | grep " + f"{domain_name}" + " > " f"{tool_output_file_path}" + "/assetfinder_out5 && cat " + f"{tool_output_file_path}" + "/assetfinder_out5" + " >> " + f"{output_file_path}"
    print(cmd)
    subprocess.run(cmd, shell=True)

def sorter(output_file_path, current_path, domain_name):
    cmd = "cat " + f"{output_file_path}" + " | sort | sort -u > " + f"{current_path}" + "/" + f"{domain_name}" + "/sorted.txt"
    print(cmd)
    subprocess.run(cmd, shell=True)

def find_alive(current_path, domain_name, output_file_path):
    output_file_path_alive = f"{current_path}" + "/" + f"{domain_name}" + "/alive.txt"
    cmd = f"cat {output_file_path} | httprobe > {output_file_path_alive}"
    print(cmd)
    output = subprocess.run(cmd, shell=True)

def main(args):
    current_path = os.getcwd()
    if not os.path.exists(args.domain):
        os.makedirs(args.domain)

    current_path = os.getcwd()
    if not os.path.exists(args.domain + "/tool_output"):
        os.makedirs(args.domain + "/tool_output")

    domain_name = args.domain
    output_file_path = f"{current_path}" + "/" + f"{domain_name}" + "/found.txt"
    tool_output_file_path = f"{current_path}" + "/" + f"{domain_name}" + "/tool_output"

    subscrapper_runner(tool_output_file_path, domain_name, output_file_path)
    subfinder_runner(tool_output_file_path, domain_name, output_file_path)
    assetfinder_runner(tool_output_file_path, domain_name, output_file_path)
    sorter(output_file_path, current_path, domain_name)
    find_alive(current_path, domain_name, output_file_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Perform operations on a given domain name.')
    parser.add_argument('domain', type=str, help='The domain name to perform operations on')
    args = parser.parse_args()
    main(args)
