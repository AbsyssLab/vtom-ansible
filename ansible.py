import argparse
import os
import sys
import json
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    stream=sys.stdout,
    force=True
)

try:
    import ansible_runner
except ImportError:
    print("❌ The module ansible_runner is not installed. "
          "Please run: pip install ansible-runner")
    sys.exit(1)


def run_ansible_playbook(playbook_path, inventory=None, extra_vars=None,
                         limit=None, tags=None, log_file=None, check=False):
    """
    Run an Ansible playbook using ansible_runner.
    """

    # Check that the playbook exists
    if not os.path.isfile(playbook_path):
        print(f"❌ Error: Playbook '{playbook_path}' not found.")
        sys.exit(1)

    # If an inventory is provided, ensure it exists
    if inventory:
        if not os.path.isfile(inventory):
            print(f"❌ Error: Inventory file '{inventory}' not found.")
            sys.exit(1)

    # Prepare ansible_runner configuration
    runner_config = {
        "playbook": playbook_path,
        "verbosity": 1,
    }

    if inventory:
        runner_config["inventory"] = inventory

    if limit:
        runner_config["limit"] = limit

    # Tags and check mode (passed through cmdline)
    cmdline_opts = []
    if tags:
        cmdline_opts.append(f"--tags {tags}")
    if check:
        cmdline_opts.append("--check")
    if cmdline_opts:
        runner_config["cmdline"] = " ".join(cmdline_opts)

    # Extra variables (JSON format)
    if extra_vars:
        try:
            runner_config["extravars"] = json.loads(extra_vars)
        except json.JSONDecodeError as e:
            print(f"❌ Error: extra-vars is not valid JSON.\nDetails: {e}")
            sys.exit(1)

    try:
        r = ansible_runner.run(**runner_config)
    except Exception as e:
        print(f"❌ Error while running playbook: {e}")
        sys.exit(1)

    # Handle logs
    if log_file:
        try:
            with open(log_file, "w", encoding="utf-8") as f:
                for event in r.events:
                    if "stdout" in event:
                        f.write(event["stdout"] + "\n")
        except Exception as e:
            print(f"⚠️ Could not write to log file '{log_file}': {e}")
    else:
        for event in r.events:
            if "stdout" in event:
                print(event["stdout"])

    # Return code result
    if r.rc == 0:
        print("✅ Playbook executed successfully.")
    else:
        print(f"❌ Playbook failed with return code {r.rc}.")

    return r.rc


def main():
    parser = argparse.ArgumentParser(
        description="Run an Ansible playbook using ansible-runner (Python API)."
    )

    parser.add_argument("playbook", help="Path to the playbook.yml file")
    parser.add_argument("-i", "--inventory", help="Optional Ansible inventory file")
    parser.add_argument("-e", "--extra-vars", help="Extra variables in JSON format, e.g.: '{\"key\":\"value\"}'")
    parser.add_argument("-l", "--limit", help="Limit execution to specific hosts")
    parser.add_argument("-t", "--tags", help="Only run plays and tasks tagged with these values")
    parser.add_argument("--check", action="store_true", help="Run in check mode (dry-run)")
    parser.add_argument("-o", "--output", help="Log output file")

    args = parser.parse_args()

    run_ansible_playbook(
        playbook_path=args.playbook,
        inventory=args.inventory,
        extra_vars=args.extra_vars,
        limit=args.limit,
        tags=args.tags,
        log_file=args.output,
        check=args.check
    )


if __name__ == "__main__":
    main()
