[中文版项目介绍](https://shawvey.github.io/%E5%88%A9%E7%94%A8AWS%E5%92%8CFabric%E6%A8%A1%E6%8B%9F%E5%A4%9A%E5%8F%B0%E8%99%9A%E6%8B%9F%E6%9C%BA%E5%B9%B6%E8%A1%8C%E8%BF%9B%E8%A1%8C%E6%AF%94%E7%89%B9%E5%B8%81%E6%8C%96%E7%9F%BF%E9%AA%8C%E8%AF%81%E8%BF%87%E7%A8%8B/)
# Cloud Nonce Discovery System

Horizontal Scaling for an Embarrassingly Parallel Task: Blockchain Proof-of-Work in the Cloud



## Deploy CND system

1. Create a AWS account and paste your credentials from account details into the `~/.aws/credentials`

   ```shell
   aws_access_key_id= Yourawsaccesskeyid
   aws_secret_access_key= Yourawssecretaccesskey
   aws_session_token= Yourawssessiontoken
   ```

2. Create a new security group based on your current ip address and change the security group name of `CND.py` to your security group name:

        SecurityGroups= ['YourSecurityGroups']

3. Create a S3 bucket to store log files

4. Install `Boto3` and `Fabric`

   ```shell
   pip install Boto3
   pip install Fabric
   ```

5. Enter to the `Fabric` folder

6. Run the following command:

   ```shell
   fab -f CND.py start:T=200,D=2,N=8 
   ```



## Results

```shell
(base) vpn-user-246-228:fabric shawvey$ fab -f CND.py start:T=200,D=2,N=8
[3.83.191.153] Executing task 'RunInstances'
[100.24.5.46] Executing task 'RunInstances'
[18.207.211.76] Executing task 'RunInstances'
[52.201.233.152] Executing task 'RunInstances'
[34.203.218.191] Executing task 'RunInstances'
[100.26.104.84] Executing task 'RunInstances'
[3.84.45.62] Executing task 'RunInstances'
[52.91.85.180] Executing task 'RunInstances'
[100.26.104.84] put: PoW.py -> PoW.py
[52.91.85.180] put: PoW.py -> PoW.py
[52.201.233.152] put: PoW.py -> PoW.py
[18.207.211.76] put: PoW.py -> PoW.py
[100.24.5.46] put: PoW.py -> PoW.py
[3.84.45.62] put: PoW.py -> PoW.py
[34.203.218.191] put: PoW.py -> PoW.py
[100.26.104.84] run: python3 -c 'import PoW;PoW.goldennonce(2,5)'
[52.91.85.180] run: python3 -c 'import PoW;PoW.goldennonce(2,7)'
[3.83.191.153] put: PoW.py -> PoW.py
[52.201.233.152] run: python3 -c 'import PoW;PoW.goldennonce(2,3)'
[18.207.211.76] run: python3 -c 'import PoW;PoW.goldennonce(2,2)'
[100.24.5.46] run: python3 -c 'import PoW;PoW.goldennonce(2,1)'
[3.84.45.62] run: python3 -c 'import PoW;PoW.goldennonce(2,6)'
[34.203.218.191] run: python3 -c 'import PoW;PoW.goldennonce(2,4)'
[100.26.104.84] run: python3 -c 'import PoW;PoW.goldennonce(2,13)'
[52.91.85.180] run: python3 -c 'import PoW;PoW.goldennonce(2,15)'
[52.201.233.152] run: python3 -c 'import PoW;PoW.goldennonce(2,11)'
[3.83.191.153] run: python3 -c 'import PoW;PoW.goldennonce(2,0)'
[18.207.211.76] run: python3 -c 'import PoW;PoW.goldennonce(2,10)'
[100.24.5.46] run: python3 -c 'import PoW;PoW.goldennonce(2,9)'
[3.84.45.62] run: python3 -c 'import PoW;PoW.goldennonce(2,14)'
[34.203.218.191] run: python3 -c 'import PoW;PoW.goldennonce(2,12)'
[100.26.104.84] run: python3 -c 'import PoW;PoW.goldennonce(2,21)'
[52.91.85.180] run: python3 -c 'import PoW;PoW.goldennonce(2,23)'
[52.201.233.152] run: python3 -c 'import PoW;PoW.goldennonce(2,19)'
[18.207.211.76] run: python3 -c 'import PoW;PoW.goldennonce(2,18)'
[100.24.5.46] run: python3 -c 'import PoW;PoW.goldennonce(2,17)'
...............
[34.203.218.191] out: Lucky num is 116, its hash is 00a722b0e1eab12e68928824ce82e5bc7cec6740e6cd0d3ffbe63260badc53fa
[34.203.218.191] out: 

total runtime is 8.968298 seconds!
[34.203.218.191] download: /Users/shawvey/fabric/logs/Instance4.log <- /var/log/syslog

Warning: Local file /Users/shawvey/fabric/logs/Instance4.log already exists and is being overwritten.
...............
Done.

```

