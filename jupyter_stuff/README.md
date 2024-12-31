1. Launch instances
2. Name it whatever you want
3. Click allow http traffic from the internet
4. Click 'edit' on network settings
   (a) Click "add security group rule", give the rule port 8000, and add 0.0.0.0/0 as the source
   (b) Click "add security group rule" again, and give the rule port 8000, and add 172.17.0.0/16 as the source
   
5. Press launch instance
6. Connect to the instance
7. Note down the public ip address
8. Run 'sudo yum install git' and then run 'git clone https://github.com/sigalrmp/Puzzle-Hunt.git'
9. cd Puzzle-Hunt/jupyter_stuff/
10. chmod +x setup.sh run.sh
11. ./setup.sh
12. ./run.sh (should take about a minute the first time)
13. You will be able to find jupyterhub on http://<ec2_public_ip_address>:8000
14. In a new tab, run "python leaderboard.py"

Troubleshooting:
setup.sh can be rerun. Often this will fix the issue, especially if it says something isn't installed.
