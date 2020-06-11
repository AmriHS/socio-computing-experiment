import os
import boto3

ssm_param = boto3.client('ssm')


def get_secret(key, decrypted=False):
	response = ssm_param.get_parameter(
		Name=key,
		WithDecryption=decrypted
	)
	return response['Parameter']['Value']