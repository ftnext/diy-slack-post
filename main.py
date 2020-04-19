import argparse

from postslack import post_slack


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("channel")
    parser.add_argument("message")
    args = parser.parse_args()

    post_slack(args.channel, args.message)


if __name__ == "__main__":
    main()
