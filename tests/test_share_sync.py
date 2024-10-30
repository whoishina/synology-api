from unittest import TestCase
import unittest
from synology_api.drive_admin_console import DriveShareSync
from setup_tests import parse_config
import os, pathlib
import json
import time

class TestShareSync(TestCase):
    config: dict[str, str]

    def setUp(self):
        self.config = parse_config(
            os.path.realpath(
                os.path.join(
                    pathlib.Path(__file__).parent.resolve(),
                    './resources/config-test.json'
                )
            )
        )

    def sign_in(self) -> DriveShareSync:
        return DriveShareSync(
            ip_address=self.config["synology_ip"],
            port=self.config["synology_port"],
            username=self.config["synology_user"],
            password=self.config["synology_password"],
            secure=bool(self.config["synology_secure"]), cert_verify=False,
            dsm_version=int(self.config["dsm_version"]), debug=True,
            otp_code=self.config["otp_code"]
        )

    def test_get_session_id(self):
        cs = self.sign_in()
        self.assertIsNotNone(cs)
        self.assertIsNotNone(cs.session)
        self.assertIsNotNone(cs.session.sid)
        print(cs.update_filter_paths(6, ['/Test-abc'], 'add'))
        print(cs.get_session_config(6))

if __name__ == '__main__':
    unittest.main()
