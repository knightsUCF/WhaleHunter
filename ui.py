import argparse


parser = argparse.ArgumentParser()
parser.add_argument("echo", help="live, demo, feed")
args = parser.parse_args()

# print (args.echo) # example of how to grab echo

if args.echo == 'live':
    print('Live mode selected')

if args.echo == 'demo':
    print('Demo mode selected')

if args.echo == 'feed':
    print('Feed mode selected')
