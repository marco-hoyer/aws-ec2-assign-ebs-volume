aws-ec2-assign-ebs-volume
=========================

Reads a volume id from instance tags and attaches the volume to the instance it runs on.

## Why another tool?
If you deploy your aws instances by exchanging the AMI (e.g. the instance at all) but need some persistency, a solution could be to use separate EBS volumes.
This needs you to dynamically attach EBS volumes to an instance during startup. This project is a proof of concept for this, actually not caring about many edge cases, device-mounting or filesystem handling.


## Prerequisites:

- python 2.6+ (but not python3 yet)

- [boto SDK](http://docs.pythonboto.org/en/latest/getting_started.html)

- AWS [credentials for boto](http://docs.pythonboto.org/en/latest/boto_config_tut.html#credentials) (e.g. a EC2 instance profile)

## Usage
```
./aws-ec2-assign-ebs-volume.py
```
