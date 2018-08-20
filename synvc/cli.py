from synvc.syn_client import SynClient, _get_file_paths, _get_anno_p
from pathlib import Path
from synvc.utilities import (get_settings_md5, load_json, save_json,
                             check_or_create_dir)
import argparse


def upload():
    parser = argparse.ArgumentParser()
    parser.add_argument("local_dir", help="local directory to sync")
    parser.add_argument("remote_synid", help="remote project synid")
    args = parser.parse_args()
    local_dir = args.local_dir
    remote_synid = args.remote_synid
    sc = SynClient()
    sc.login()
    sc.parent_synid = remote_synid
    sc.sync_folder(local_dir, direction='up')