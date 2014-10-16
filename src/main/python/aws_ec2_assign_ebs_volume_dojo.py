__author__ = 'mhoyer'

from boto import ec2
from boto import utils


class Ec2Instance(object):

    EBS_VOLUME_TAG_NAME = "ebs_volume_id"

    def __init__(self, instance_id=None, region="eu-west-1"):
        self.aws = ec2.connect_to_region(region)
        self.id = instance_id or self._get_local_instance_id()

    @staticmethod
    def _get_local_instance_id():
        return utils.get_instance_metadata()['instance-id']

    # TODO: validate volume_id format to match unit tests
    @staticmethod
    def volume_id_is_valid(volume_id):
        pass

    # TODO: attach ebs volume to instance
    def attach_ebs_volume(self):
        pass


if __name__ == "__main__":
    instance = Ec2Instance("i-f1653a14")
    instance.attach_ebs_volume()