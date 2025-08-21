import boto3

polly_client = boto3.client(
    "polly",
    aws_access_key_id="YOUR_ACCESS_KEY",
    aws_secret_access_key="YOUR_SECRET_KEY",
    region_name="us-east-1"
)

response = polly_client.synthesize_speech(
    Text="Hello! This is a test using AWS Polly with Terraform and Python.",
    OutputFormat="mp3",
    VoiceId="Ayanda"   # You can choose voices like Matthew, Amy, etc.
)

# Save audio stream to file
with open("output.mp3", "wb") as file:
    file.write(response["AudioStream"].read())

print("Saved speech to output.mp3")