from aws_ec2_assign_ebs_volume import Ec2Instance

if __name__ == "__main__":
    instance = Ec2Instance("i-f1653a14")
    instance.attach_ebs_volume()