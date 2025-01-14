import os
import math
import argparse
import csv
import time
import subprocess

def main():
    DOMAIN = 'zenotravel'

    pb = '01'
    domain_problem_path = 'experiments/' + DOMAIN + '/' + DOMAIN + '-p' + pb

    domaind_ir = domain_problem_path + '/domain.pddl'
    hyps_dir = domain_problem_path + '/hyps.dat'
    template_dir = domain_problem_path + '/template.pddl'

    hyps_file = open(hyps_dir, 'r')
    new_hyps = []
    for l in hyps_file:
        new_l = l.replace('(and ', '')
        new_l = new_l.replace(') (', ')|(')
        new_l = new_l.replace('))', ') - 1.0')
        new_hyps.append(new_l)
        print(new_l)

    new_problem_file = open(domain_problem_path + '/goals.txt', 'w')
    for l in new_hyps:
        new_problem_file.write(l)
    new_problem_file.close()


def main_all_domains():
    DOMAINS = ['blocks-world', 'depots', 'driverlog', 'dwr', 'logistics', 'rovers', 'sokoban', 'zenotravel']
    NUMBER_OF_PROBLEMS = 10

    for DOMAIN in DOMAINS:
        for i in range(1,NUMBER_OF_PROBLEMS+1):
            pb = '0' + str(i) if i <= 9 else str(i)
            domain_problem_path = 'experiments/' + DOMAIN + '/' + DOMAIN + '-p' + pb
            
            domain_dir = domain_problem_path + '/domain.pddl'
            hyps_dir = domain_problem_path + '/hyps.dat'
            template_dir = domain_problem_path + '/template.pddl'

            print (domain_dir)

            hyps_file = open(hyps_dir, 'r')
            new_hyps = []
            for l in hyps_file:
                new_l = l.replace('(and ', '')
                new_l = new_l.replace('(AND ', '')
                new_l = new_l.replace(') (', ')|(')
                new_l = new_l.replace('))', ') - 1.0')
                new_hyps.append(new_l)
                print(new_l)

            new_problem_file = open(domain_problem_path + '/goals.txt', 'w')
            for l in new_hyps:
                new_problem_file.write(l)
            new_problem_file.close()      

def main_all_domains_no_real_hyp():
    DOMAINS = ['blocks-words', 'grid-navigation', 'logistics', 'ferry']
    NUMBER_OF_PROBLEMS = 10

    for DOMAIN in DOMAINS:
        for i in range(1,NUMBER_OF_PROBLEMS+1):
            pb = '0' + str(i) if i <= 9 else str(i)
            domain_problem_path = 'experiments/' + DOMAIN + '/' + 'p' + pb
            
            domain_dir = domain_problem_path + '/domain.pddl'
            hyps_dir = domain_problem_path + '/hyps.dat'

            print (domain_dir)

            real_hyp = ''
            real_hype_file = open(domain_problem_path + '/real_hyp.dat', 'r')

            for l in real_hype_file:
                real_hyp = l

            hyps_file = open(hyps_dir, 'r')
            new_hyps = []
            print(real_hyp)
            for l in hyps_file:
                if real_hyp in l:
                    continue
                new_l = l.replace('(and ', '')
                new_l = new_l.replace('(AND ', '')
                new_l = new_l.replace(') (', ')|(')
                new_l = new_l.replace('))', ') - 1.0')
                new_hyps.append(new_l)
                print(new_l)

            new_problem_file = open(domain_problem_path + '/goals-no_real_hyp.txt', 'w')
            for l in new_hyps:
                new_problem_file.write(l)
            new_problem_file.close()

if __name__ == '__main__':
    main_all_domains_no_real_hyp()
