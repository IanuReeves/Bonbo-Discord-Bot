# Class Libraries
import discord
import os
import random
from ec2_metadata import ec2_metadata

# Output to make sure the class libraries work.
print(ec2_metadata.region)
print(ec2_metadata.instance_id)