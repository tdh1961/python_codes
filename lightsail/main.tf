resource "aws_instance" "server1" {
    ami = "ami-0d7a109bf30624c99"
    instance_type = "t2.micro"
    key_name = "grandeeditions2"
    tags = {
        name = "terraform server"
        Team = "devops"
        env = "dev"  
    }
    user_data = file("script.sh")
}