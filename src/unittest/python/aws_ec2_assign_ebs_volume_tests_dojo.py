from unittest import TestCase
from mock import Mock, patch, call
from boto import utils

from aws_ec2_assign_ebs_volume_dojo import Ec2Instance
import aws_ec2_assign_ebs_volume


class Ec2InstanceTests(TestCase):

    def setUp(self):
        self.boto_utils_mock = Mock(utils)
        self.instance = Ec2Instance("test_instance_id")

    def tearDown(self):
        patch.stopall()

    def test_volume_id_is_valid_returns_true_for_valid_id(self):
        RESULT = Ec2Instance.volume_id_is_valid("vol-db5064d0")
        self.assertTrue(RESULT, "Should return true if a valid volume id supplied")

    def test_volume_id_is_valid_returns_false_for_invalid_id(self):
        RESULT = Ec2Instance.volume_id_is_valid("ebs-db5064d0")
        self.assertFalse(RESULT, "Should return false if a invalid volume id supplied")

    def test_volume_id_is_valid_returns_false_for_empty_string(self):
        RESULT = Ec2Instance.volume_id_is_valid("")
        self.assertFalse(RESULT, "Should return false if empty string supplied")

    def test_volume_id_is_valid_returns_false_for_none(self):
        RESULT = Ec2Instance.volume_id_is_valid(None)
        self.assertFalse(RESULT, "Should return false if none supplied")

    @patch('aws_ec2_assign_ebs_volume.utils.get_instance_metadata')
    def test_get_id_calls_get_instance_metadata(self, get_instance_metadata_mock):
        INSTANCE_METADATA = {'instance-id': 'i-f1653a14'}
        get_instance_metadata_mock.return_value = INSTANCE_METADATA
        EXPECTED = "i-f1653a14"

        RESULT = self.instance._get_local_instance_id()

        self.assertEqual(EXPECTED, RESULT)
        get_instance_metadata_mock.assert_called()