#!/usr/bin/env python

from aws_ec2_assign_ebs_volume import Ec2Instance

if __name__ == "__main__":
    instance = Ec2Instance()
    instance.attach_ebs_volume()