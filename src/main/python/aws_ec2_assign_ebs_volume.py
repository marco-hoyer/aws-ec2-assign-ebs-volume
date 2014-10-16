__author__ = 'mhoyer'

from boto import ec2
from boto import utils
from boto.exception import EC2ResponseError


class Ec2Instance(object):

    EBS_VOLUME_TAG_NAME = "ebs_volume_id"

    def __init__(self, instance_id=None, region="eu-west-1"):
        self.aws = ec2.connect_to_region(region)
        assert self.aws, "Could not establish connection to ec2 api"
        self.id = instance_id or self._get_local_instance_id()

    def _get_ec2_instance_data(self):
        reservations = self.aws.get_all_reservations(instance_ids=[self.id])
        reservation = reservations[0]
        assert len(reservation.instances) == 1
        return reservation.instances[0]

    def _get_local_instance_id(self):
        return utils.get_instance_metadata()['instance-id']

    def _get_tags(self):
        return self._get_ec2_instance_data().tags

    def _get_ebs_volume_id_tag(self):
        tags = self._get_tags()

        try:
            volume_id = tags[self.EBS_VOLUME_TAG_NAME]
        except KeyError:
            return None

        assert self._volume_id_is_valid(volume_id), \
            "'{0}' is invalid value for {1} tag, expected 'vol-...'".format(volume_id, self.EBS_VOLUME_TAG_NAME)
        return volume_id

    @staticmethod
    def _volume_id_is_valid(volume_id):
        if volume_id and volume_id.startswith("vol-"):
            return True
        else:
            return False

    def attach_ebs_volume(self, dry_run=False):
        try:
            volume_id = self._get_ebs_volume_id_tag()
            if volume_id:
                self.aws.attach_volume(volume_id, self.id, '/dev/sdh', dry_run)
                print "Successfully attached ebs volume {0} to instance {1}".format(volume_id, self.id)
            else:
                print "No {0} tag found, doing nothing".format(self.EBS_VOLUME_TAG_NAME)
        except EC2ResponseError as e:
            if e.error_code == "VolumeInUse":
                print "Volume is already in use"
            else:
                print "Error attaching ebs volume, aws api response: " +  str(e.message)
        except Exception as e:
            print "Error attaching ebs volume: " + str(e)

if __name__ == "__main__":
    instance = Ec2Instance("i-f1653a14")
    instance.attach_ebs_volume()