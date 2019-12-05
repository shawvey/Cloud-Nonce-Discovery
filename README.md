# Deploy CND system

1. Create a AWS account and paste your credentials from account details into the `~/.aws/credentials`

   ```shell
   aws_access_key_id= Yourawsaccesskeyid
   aws_secret_access_key= Yourawssecretaccesskey
   aws_session_token= Yourawssessiontoken
   ```

2.  Create a new security group based on your current ip address and change the security group name of `CND.py` to your security group name:

         `SecurityGroups`= ['YourSecurityGroups']

3. Create a S3 bucket to store log files

4. Install `Boto3` and `Fabric`

5. Enter to the `Fabric` folder

6. Run the following command:

   ```shell
   fab -f CND.py start:T=200,D=2,N=8 SecurityGroups=['YourSecurityGroups']
   ```
