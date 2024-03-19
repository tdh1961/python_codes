
# Generate a secure private key and encodes it as PEM
resource "tls_private_key" "ec2_key" {
   algorithm = "RSA"
   rsa_bits    = 2048 
}
# Create they key pair 
resource "aws_key_pair" "ec2_key" { 
    key_name = "grandeeditions2"
    public_key = tls_private_key.ec2_key.public_key_openssh
}
# Save file
resource "local_file" "ssh_key" {
    filename = "grandeeditions2.pem"
    content = tls_private_key.ec2_key.private_key_pem
}