import os
import boto3

client = boto3.client('ssm')


def get_secret(key, decrypted=False):
	response = client.get_parameter(
		Name=key,
		WithDecryption=decrypted
	)
	return response['Parameter']['Value']